"""
Locators for user login page.
"""

from screenpy_selenium import Target

SIGNUP_GENDER_MALE_CHECKBOX = Target.the("gender male checkbox").located_by("input#id_gender1")
SIGNUP_GENDER_FEMALE_CHECKBOX = Target.the("gender female checkbox").located_by("input#id_gender2")
SIGNUP_PASSWORD_TEXT_BOX = Target.the("password field").located_by("input#password")
SIGNUP_DAY_OF_BIRTH_3_OPTION = Target.the("select day of birth").located_by("select#days > option[value='3']")
SIGNUP_MONTH_OF_BIRTH_3_OPTION = Target.the("select month of birth").located_by("select#months > option[value='3']")
SIGNUP_YEAR_OF_BIRTH_1996_OPTION = Target.the("select year of birth").located_by("select#years > option[value='1996']")
SIGNUP_ADDRESS_INFO_FIRST_NAME = Target.the("first name field").located_by("input#first_name")
SIGNUP_ADDRESS_INFO_LAST_NAME = Target.the("last name field").located_by("input#last_name")
SIGNUP_ADDRESS_INFO_ADDRESS_1 = Target.the("address 1 field").located_by("input#address1")
SIGNUP_ADDRESS_INFO_ADDRESS_2 = Target.the("address 2 field").located_by("input#address2")
SIGNUP_COUNTRY_UNITES_STATES_OPTION = Target.the("select country united states").located_by("select#country > option[value='United States']")
SIGNUP_ADDRESS_INFO_STATE = Target.the("state field").located_by("input#state")
SIGNUP_ADDRESS_INFO_CITY = Target.the("city field").located_by("input#city")
SIGNUP_ADDRESS_INFO_ZIPCODE = Target.the("zipcode field").located_by("input#zipcode")
SIGNUP_ADDRESS_INFO_MOBILE_NUMBER = Target.the("mobile number field").located_by("input#mobile_number")
SIGNUP_ADDRESS_INFO_CREATE_ACCOUNT_BUTTON = Target.the("create account button").located_by("button[data-qa='create-account']")