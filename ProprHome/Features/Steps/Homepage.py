import time
import allure
from allure_commons.types import AttachmentType
from behave import *
from Pages.Signup import Signup
from Pages.searchproperty import SearchProperty


@given(u'Open the website in the chrome Browser')
def step_impl(context):

    allure.attach(context.driver.get_screenshot_as_png(), name='f_screenshot',
                  attachment_type=AttachmentType.PNG)


@when(u'Select the property from the "Property Type"')
def step_impl(context):
    context.searchproperty = SearchProperty(context.driver)
    context.searchproperty.select_property_type()
    context.searchproperty.select_property_type_house()
    context.searchproperty.click_next()
    context.searchproperty.select_no_of_bedrooms()
    context.searchproperty.select_no_of_bathrooms()
    context.searchproperty.click_next()
    context.searchproperty.select_price_range()
    context.searchproperty.click_next()
    context.searchproperty.select_key_feature()
    context.searchproperty.click_next()


@then(u'Select the location where you want to find the  property')
def step_impl(context):
    context.searchproperty.select_location()


@then(u'filter the Property and Click on search')
def step_impl(context):
    context.searchproperty.select_property_feature()


@then(u'Enter the required details and complete then Click on "Search"')
def step_impl(context):
    context.searchproperty.click_search_property_button()
    time.sleep(5)


@then(u'User to be navigated to "property-results" page with list of properties.')
def step_impl(context):
    context.searchproperty.verify_search_result()


@then(u'Click on ""Sign Up"" and select user type ""buyer"".')
def step_impl(context):
    context.signup = Signup(context.driver)
    context.signup.click_login_signup()
    context.signup.click_signup()
    context.signup.click_user_type()


@then(u'Click on Continue')
def step_impl(context):
    context.signup.click_continue_button()


@then(u'all the required details for Signup and Click on Next')
def step_impl(context):
    context.signup.enter_first_name()
    context.signup.enter_last_name()
    context.signup.enter_email()
    context.signup.enter_password()
    context.signup.select_terms_and_conditions()


@then(u'it is created after clicking the sign up')
def step_impl(context):
    context.signup.click_signup_button()

    context.signup.verify_signup()
