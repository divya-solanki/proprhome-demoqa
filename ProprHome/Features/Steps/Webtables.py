
from behave import *
from Pages.AddandDeletefromWebtables import addanddeletefromwebtables


@when(u'Navigate to demoqa "https://demoqa.com/webtables" website')
def step_impl(context):
    context.webtables = addanddeletefromwebtables(context.driver)
    context.webtables.get_webpage()


@then(u'Click the add button')
def step_impl(context):
    context.webtables.click_add_button()


@then(u'Fill in the register form and submit')
def step_impl(context):
    context.webtables.add_details()


@then(u'Verifydata in the webtable')
def step_impl(context):
    context.webtables.verify_data()


@then(u'delete a row by clicking the delete butoon in a web table')
def step_impl(context):
    context.webtables.delete_row()
