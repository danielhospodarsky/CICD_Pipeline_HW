#Issue Title: Custom 500 Error Page and Error Handling
#Labels:
#bug
#enhancement
#error-handling
#pytest
#Description:
#Our web application needs a custom 500 error page and error handling for internal server errors. 
# This will improve the user experience and help us diagnose and fix issues more efficiently.

#We will create a new view to handle 500 errors and render a custom template. 
# We will also add appropriate error-handling middleware to catch exceptions and return the custom error page.

#To ensure that the error-handling works as expected, 
# we will write a pytest to simulate a 500 error and verify that the custom error page is displayed.

#Acceptance Criteria:
#A custom 500 error page is displayed when an internal server error occurs
#Error-handling middleware is added to catch exceptions and return the custom error page
#A pytest is written and passes to verify the error-handling and custom error page functionality

import pytest
from app import app

@pytest.fixture
def client():
    app = Flask(__name__)
    # Register custom error handling for 500 errors
    @app.errorhandler(500)
    def internal_server_error(error):
        return "Custom 500 error page", 500

    # Register a view that raises a 500 error
    @app.route('/raise_error')
    def raise_error():
        raise Exception("Simulated internal server error")

    client = app.test_client()
    return client

def test_custom_500_page(client):
    response = client.get('/raise_error')
    assert response.status_code == 500
    assert b'Custom 500 error page' in response.data