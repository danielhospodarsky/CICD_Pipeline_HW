#Issue Title: Custom 404 Error Page and Error Handling
#Labels:
#bug
#enhancement
#error-handling
#pytest
#Description:
#Our web application needs a custom 404 error page and error handling for page not found errors. 
# This will improve the user experience and help us diagnose and fix issues more efficiently.

#We will create a new view to handle 404 errors and render a custom template. 
# We will also add appropriate error-handling middleware to catch page not found errors and return the custom error page.

#To ensure that the error-handling works as expected, 
# we will write a pytest to simulate a page not found error and verify that the custom error page is displayed.

#Acceptance Criteria:
#A custom 404 error page is displayed when a page not found error occurs
#Error-handling middleware is added to catch page not found errors and return the custom error page
#A pytest is written and passes to verify the error-handling and custom error page functionality

import pytest

@pytest.fixture
def client():
    app = Flask(__name__)
    # Register custom error handling for 404 errors
    @app.errorhandler(404)
    def page_not_found(error):
        return "Custom 404 error page", 404

    client = app.test_client()
    return client

def test_custom_404_page(client):
    response = client.get('/non_existent_page')
    assert response.status_code == 404
    assert b'Custom 404 error page' in response.data
