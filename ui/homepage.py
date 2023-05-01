"""
Locators and URL for the zerobank application home page.
"""

from screenpy_selenium import Target


URL = "https://www.automationexercise.com"

MENU_BAR = Target.the("brand logo").located_by("#header > div > div > div > div.col-sm-8 > div > ul")
ALL_OWNERS_MENU = Target.the("home menu").located_by("nav > div > ul > li.dropdown.open > ul > li:nth-child(1) > a")
