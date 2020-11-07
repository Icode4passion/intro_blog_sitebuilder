





import  pygments ,markdown ,sys
from flask import Flask , render_template ,render_template_string, request, url_for
from flask_flatpages import FlatPages ,pygmented_markdown, pygments_style_defs
from flask_frozen import Freezer


# def my_markdown(text):
#     markdown_text = render_template_string(text)
#     pygmented_text = markdown.markdown(markdown_text, extensions=["codehilite", "fenced_code", "tables"])
#     return pygmented_text


DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'



app = Flask(__name__)
app.config.from_object(__name__)
#FLATPAGES_MARKDOWN_EXTENSION =["codehilite", "fenced_code", "tables"]
pages = FlatPages(app)
freezer = Freezer(app)
#app.config["FLATPAGES_HTML_RENDERER"] = my_markdown




# @app.route('/pygments.css')
# def pygments_css():
#     return pygments_style_defs("monokai"), 200, {"Content-Type":"text/css"}


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/blog')
def blog():
    return  render_template('blog.html',pages=pages)

    
@app.route('/about')
def about():
    return  render_template('about.html' )



@app.route('/contact')
def contact():
    return  render_template('contact.html' )

@app.route('/<path:path>')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@freezer.register_generator
def pagelist():
    for page in pages:
        yield url_for('page',path=page.path)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host="0.0.0.0")
