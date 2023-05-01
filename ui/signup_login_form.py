"""
Locators for user login page.
"""

from screenpy_selenium import Target

LOGIN_FORM_HEADING = Target.the("login form heading").located_by("//h2[contains(text(),'Login to your account')]")
SIGNUP_FORM_HEADING = Target.the("signup form heading").located_by("//h2[contains(text(),'New User Signup!')]")
SIGNUP_FORM_USER_NAME = Target.the("signup form username").located_by("input[data-qa='signup-name']")
SIGNUP_FORM_EMAIL_ADDRESS = Target.the("signup form username").located_by("input[data-qa='signup-email']")
SIGNUP_FORM_SIGNUP_BUTTON = Target.the("signup form username").located_by("button[data-qa='signup-button']")
