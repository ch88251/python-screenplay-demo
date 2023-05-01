import json
from time import sleep
import unittest
import requests

from screenpy_selenium.abilities import BrowseTheWeb
from screenpy import AnActor, given, then, when
from screenpy.pacing import act, scene
from screenpy.actions import See
from screenpy_selenium.actions import Click, Open, Enter, Wait
from screenpy_selenium.questions import TheText
from screenpy.resolutions import ReadsExactly
from ui.account_created_page import ACCOUNT_CREATED_HEADING

from ui.homepage import (
    URL
)

from ui.menu_bar import MENU_BAR_SIGNUP_LOGIN
from ui.signup_login_form import (
    SIGNUP_FORM_EMAIL_ADDRESS, 
    SIGNUP_FORM_HEADING,
    SIGNUP_FORM_SIGNUP_BUTTON, 
    SIGNUP_FORM_USER_NAME
)
from ui.signup_page import (
    SIGNUP_ADDRESS_INFO_ADDRESS_1,
    SIGNUP_ADDRESS_INFO_CITY,
    SIGNUP_ADDRESS_INFO_CREATE_ACCOUNT_BUTTON,
    SIGNUP_ADDRESS_INFO_FIRST_NAME,
    SIGNUP_ADDRESS_INFO_LAST_NAME,
    SIGNUP_ADDRESS_INFO_MOBILE_NUMBER,
    SIGNUP_ADDRESS_INFO_STATE,
    SIGNUP_ADDRESS_INFO_ZIPCODE,
    SIGNUP_COUNTRY_UNITES_STATES_OPTION,
    SIGNUP_DAY_OF_BIRTH_3_OPTION,
    SIGNUP_GENDER_MALE_CHECKBOX,
    SIGNUP_MONTH_OF_BIRTH_3_OPTION, 
    SIGNUP_PASSWORD_TEXT_BOX,
    SIGNUP_YEAR_OF_BIRTH_1996_OPTION
)

class TestSignupLogin(unittest.TestCase):


    def setUp(self) -> None:
        self.actor = AnActor.named("Susan").who_can(BrowseTheWeb.using_chrome())
        self.user_name = 'johndoe'
        self.user_email = 'john.doe@testing.com'
        self.user_password = 'P@ssW0rd'

    @act("Perform")
    @scene("Signup")
    def test_signup(self) -> None:

        Susan = self.actor

        given(Susan).was_able_to(Open.their_browser_on(URL))

        when(Susan).attempts_to(Click.on_the(MENU_BAR_SIGNUP_LOGIN))
        
        then(Susan).should(See(TheText.of_the(SIGNUP_FORM_HEADING), ReadsExactly("New User Signup!")))

        then(Susan).attempts_to(Enter.the_text(self.user_name).into_the(SIGNUP_FORM_USER_NAME))

        then(Susan).attempts_to(Enter.the_text(self.user_email).into_the(SIGNUP_FORM_EMAIL_ADDRESS))

        then(Susan).should(Wait.for_the(SIGNUP_FORM_SIGNUP_BUTTON).to_contain_text("Signup"))

        then(Susan).attempts_to(Click.on_the(SIGNUP_FORM_SIGNUP_BUTTON))

        then(Susan).attempts_to(Click.on_the(SIGNUP_GENDER_MALE_CHECKBOX))

        then(Susan).attempts_to(Enter.the_text(self.user_password).into_the(SIGNUP_PASSWORD_TEXT_BOX))

        then(Susan).attempts_to(Click.on_the(SIGNUP_DAY_OF_BIRTH_3_OPTION))

        then(Susan).attempts_to(Click.on_the(SIGNUP_MONTH_OF_BIRTH_3_OPTION))

        then(Susan).attempts_to(Click.on_the(SIGNUP_YEAR_OF_BIRTH_1996_OPTION))

        then(Susan).attempts_to(Enter.the_text("John").into_the(SIGNUP_ADDRESS_INFO_FIRST_NAME))

        then(Susan).attempts_to(Enter.the_text("Doe").into_the(SIGNUP_ADDRESS_INFO_LAST_NAME))

        then(Susan).attempts_to(Enter.the_text("123 Fake Street").into_the(SIGNUP_ADDRESS_INFO_ADDRESS_1))

        then(Susan).attempts_to(Click.on_the(SIGNUP_COUNTRY_UNITES_STATES_OPTION))

        then(Susan).attempts_to(Enter.the_text("Colorado").into_the(SIGNUP_ADDRESS_INFO_STATE))

        then(Susan).attempts_to(Enter.the_text("Denver").into_the(SIGNUP_ADDRESS_INFO_CITY))

        then(Susan).attempts_to(Enter.the_text("80123").into_the(SIGNUP_ADDRESS_INFO_ZIPCODE))

        then(Susan).attempts_to(Enter.the_text("303-222-4444").into_the(SIGNUP_ADDRESS_INFO_MOBILE_NUMBER))

        then(Susan).should(Wait.for_the(SIGNUP_ADDRESS_INFO_CREATE_ACCOUNT_BUTTON).to_be_clickable())

        then(Susan).attempts_to(Click.on_the(SIGNUP_ADDRESS_INFO_CREATE_ACCOUNT_BUTTON))

        then(Susan).should(See(TheText.of_the(ACCOUNT_CREATED_HEADING), ReadsExactly("ACCOUNT CREATED!")))



    def tearDown(self) -> None:
        self.actor.exit()
        url = "https://automationexercise.com/api/deleteAccount"

        payload = {
            'email': self.user_email,
            'password': self.user_password
        }
        files=[]
        headers = {}

        response = requests.request("DELETE", url, headers=headers, data=payload, files=files)

        print(response.text)

        # assert response.content == 'Account deleted!', 'Request to delete account failed.'
    