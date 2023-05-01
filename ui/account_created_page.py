"""
Locators and URL for the zerobank application home page.
"""

from screenpy_selenium import Target


ACCOUNT_CREATED_HEADING = Target.the("account created heading").located_by("h2[data-qa='account-created']")
