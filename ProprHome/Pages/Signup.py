import time
from selenium.webdriver.common.by import By
from Utilities.CommonFunction import CommonFunction


class Signup:

    def __init__(self, driver):
        self.driver = driver
        self.cf = CommonFunction(self.driver)

    locator_homepage_signup = (By.XPATH, "//button[@class='header__nav__login']")
    locator_signup = (By.LINK_TEXT, "Sign up")
    locator_buyer = (By.XPATH, "//i[@class='is-home-sell']")
    locator_continue_button = (By.CSS_SELECTOR, "button[type='button']")
    locator_firstname = (By.XPATH, "//input[@placeholder='Enter your first name']")
    locator_lastname = (By.XPATH, "//input[@placeholder='Enter your surname']")
    locator_email = (By.XPATH, "//input[@placeholder='Enter your email']")
    locator_password = (By.NAME, "password")
    locator_terms_and_conditions = (By.XPATH, "//span[@class='checkmark']")
    locator_signup_button = (By.CSS_SELECTOR, "button[type='submit']")
    locator_verify_sign_up = (By.XPATH, "//span[@class = 'register__form__thanks']")

    def click_login_signup(self):
        self.cf.wait_and_click(self.locator_homepage_signup)

    def click_signup(self):
        self.cf.wait_and_click(self.locator_signup)

    def click_user_type(self):
        self.cf.wait_and_click(self.locator_buyer)

    def click_continue_button(self):
        self.cf.wait_and_click(self.locator_continue_button)

    def enter_first_name(self):
        self.cf.wait_and_input_text(self.locator_firstname, "Kevin")

    def enter_last_name(self):
        self.cf.wait_and_input_text(self.locator_lastname, "Hart")

    def enter_email(self):
        email = self.cf.random_email()
        self.cf.wait_and_input_text(self.locator_email, email)

    def enter_password(self):
        self.cf.wait_and_input_text(self.locator_password, "Welcome123")

    def select_terms_and_conditions(self):
        self.cf.wait_and_click(self.locator_terms_and_conditions)

    def click_signup_button(self):
        self.cf.wait_and_click(self.locator_signup_button)
        time.sleep(2)

    def verify_signup(self):
        self.cf.verify_page(self.locator_verify_sign_up, "Thank you for registering")