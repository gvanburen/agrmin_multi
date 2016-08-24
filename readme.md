# Agrmin_Multi: Simple Websites
[Sample Site](https://gvanburen.github.io/agrmin_multi/)

Inspired by the [Agrmin](https://github.com/travisjungroth/argmin) project, I decided to update the one page website generating script to allow for a the generation of a multiple page website from MultiMarkdown files. For more robust solutions check out [Pelican](http://blog.getpelican.com/) and [MkDocs](http://www.mkdocs.org/). As with [Agrmin](https://github.com/travisjungroth/argmin) the CSS was taken from [bettermotherfuckingwebsite.com](http://bettermotherfuckingwebsite.com/) and slightly modified.

### Setup
To build a site with agrmin_multi, the easiest thing is to clone from GitHub and delete the local repo.

    git clone https://github.com/gvanburen/agrmin_multi.git project_name
    cd project_name
    rm -rf .git
    
You can then start a new repo with `git init`, make your first commit and [push your code to GitHub](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/).

### Usage
The code includes a sample site that can be modified as needed. To generate the web page, `main.py`. This creates `index.html` and pages: `pages/post_1.html`, and `pages/post_2.html`.

    python3 main.py

`static/header.html` and `static/footer.html` are static files that get added to the top and bottom of `index.html`, `pages/post_1.html`, and `pages/post_2.html`. Modify the static files directly.

Posts are content such as articles and stories saved as MultiMarkdown files. The links at the top of the page and separate pages are generated from the Title meta attribute in the file.

Posts are added by creating a MultiMarkdown file in `posts` and adding the file name to the `post_paths` tuple in `main.py`. They appear in the same order on the web page as they do in the tuple.

