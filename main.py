from markdown import Markdown
from slugify import slugify


post_paths = ('post_1.md', 'post_2.md')
links = ['<ul>']
for post_path in post_paths:
	md = Markdown(extensions=['markdown.extensions.meta'])
	with open('posts/{}'.format(post_path)) as f:
		html = md.convert(f.read())
		title = md.Meta['title'][0]
		slug = slugify(title)
		links.append('<li><a href=pages/{slug}.html>{title}</a></li>'.format(**locals()))
links.append('</ul>')

for post_path in post_paths:
	md = Markdown(extensions=['markdown.extensions.meta'])
	with open('posts/{}'.format(post_path)) as f:
		html = md.convert(f.read())
		title = md.Meta['title'][0]
		slug = slugify(title)
		html_title = '<h2 id="{slug}">{title}</h2>'.format(**locals())
		with open('static/header.html') as header, open('static/footer.html') as footer, open('pages/{}.html'.format(slug),'w+') as p:
			p.write('\n'.join([header.read()] + links + [html_title] + [html] + [footer.read()]))

with open('static/header.html') as header, open('static/footer.html') as footer, open('index.html','w') as index:
	index.write('\n'.join([header.read()] + links + [footer.read()]))