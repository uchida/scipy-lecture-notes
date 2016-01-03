import os.path
from jinja2 import Template

sitemap_template = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{% for link in links -%}
<url><loc>{{ link|safe }}</loc></url>
{% endfor -%}
</urlset>
"""

def add_html_link(app, pagename, templatename, context, doctree):
    base_url = app.config.sitemap_baseurl
    if base_url:
        link = os.path.join(base_url, "%s.html" % pagename)
        app.sitemap_links.append(link)


def create_sitemap(app, exception):
    if exception is not None:
        return
    if app.sitemap_links:
        filename = os.path.join(app.outdir, "sitemap.xml")
        template = Template(sitemap_template)
        print("Generating sitemap.xml in %s" % filename)
        with open(filename, 'w') as f:
            f.write(template.render(links=app.sitemap_links))

def setup(app):
    app.add_config_value('sitemap_baseurl', '', 'html')
    app.connect('html-page-context', add_html_link)
    app.connect('build-finished', create_sitemap)
    app.sitemap_links = []
