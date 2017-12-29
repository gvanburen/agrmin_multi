#!/usr/bin/python3
from markdown import Markdown
from slugify import slugify
import glob

global post_paths

index_links = ['<ul>']
links = ['<ul>']


def main():
    build_posts()
    build_links()
    build_pages()
    write_index()


def build_posts():
    global post_paths
    post_paths = glob.glob("posts/*.md")
    for idx, post in enumerate(post_paths):
        post_paths[idx] = post.replace("posts/", "")


def build_links():
    for post_path in post_paths:
        html, title, slug = get_post_details(post_path)
        index_links.append('<li><a href=pages/{slug}.html>{title}</a></li>'.format(**locals()))
        links.append('<li><a href=../pages/{slug}.html>{title}</a></li>'.format(**locals()))
    index_links.append('</ul>')
    links.append('</ul>')


def build_pages():
    for post_path in post_paths:
        html, title, slug = get_post_details(post_path)
        html_title = '<h2 id="{slug}">{title}</h2>'.format(**locals())
        with open('static/header.html') as header, open('static/footer.html') as footer, open('pages/{}.html'.format(slug), 'w+') as p:
            p.write('\n'.join([header.read()] + links + [html_title] + [html] + [footer.read()]))


def get_post_details(post_path):
    md = Markdown(extensions=['markdown.extensions.meta'])
    with open('posts/{}'.format(post_path)) as f:
        html = md.convert(f.read())
        title = md.Meta['title'][0]
        slug = slugify(title)
    return html, title, slug


def write_index():
    with open('static/header.html') as header, open('static/footer.html') as footer, open('index.html', 'w') as index:
        index.write('\n'.join([header.read()] + index_links + [footer.read()]))


if __name__ == "__main__":
    main()
