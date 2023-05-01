"""
Locators for the menubar.
"""

from screenpy_selenium import Target

MENU_BAR_SIGNUP_LOGIN = Target.the("Signup / Login link").located_by("//a[contains(text(), 'Signup / Login')]")

