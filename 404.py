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
def page_not_found(error):
    return "Custom 404 error page", 404

# Register custom error handling for 500 errors
@app.errorhandler(500)
def internal_server_error(error):
    return "Custom 500 error page", 500

# Register a view that raises a 500 error
@app.route('/raise_error')
def raise_error():
    raise Exception("Simulated internal server error")