from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/about')
def about():
    return 'This is the about page'

# Register custom error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

