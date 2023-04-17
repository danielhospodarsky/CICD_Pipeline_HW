#Issue Title: Custom 500 Error Page and Error Handling
#Labels:
#bug
#enhancement
#error-handling
#pytest
#Description:
#Our web application needs a custom 500 error page and error handling for internal server errors. This will improve the user experience and help us diagnose and fix issues more efficiently.

#We will create a new view to handle 500 errors and render a custom template. We will also add appropriate error-handling middleware to catch exceptions and return the custom error page.

#To ensure that the error-handling works as expected, we will write a pytest to simulate a 500 error and verify that the custom error page is displayed.

#Acceptance Criteria:
#A custom 500 error page is displayed when an internal server error occurs
#Error-handling middleware is added to catch exceptions and return the custom error page
#A pytest is written and passes to verify the error-handling and custom error page functionality