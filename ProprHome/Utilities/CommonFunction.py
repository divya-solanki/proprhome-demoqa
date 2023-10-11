import random
import string
import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommonFunction:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 1

    def wait_and_input_text(self, locator, text, timeout=None):
        try:
            with allure.step("Enter text " + text):
                WebDriverWait(self.driver, self.default_timeout).until(
                    EC.presence_of_element_located(locator))
                WebDriverWait(self.driver, self.default_timeout).until(
                    EC.visibility_of_element_located(locator)).send_keys(text)
                self.get_png_allure_image()
                return True
        except Exception as e:
            with allure.step('Input Failed'):
                self.get_png_allure_image()
                time.sleep(2)
                return False

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            with allure.step("attachment"):
                WebDriverWait(self.driver, self.default_timeout).until(
                    EC.visibility_of_element_located(locator)).click()
                self.get_png_allure_image()
                return True
        except Exception as e:
            with allure.step("Unsuccessful"):
                self.get_png_allure_image()
                time.sleep(2)
                return False

    @staticmethod
    def random_email():
        random_name = ''.join(random.choice(string.ascii_lowercase) for x in range(7))
        email_id = random_name + '@testmail.com'
        return email_id

    def verify_page(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            with allure.step("attachment"):
                web_element = WebDriverWait(self.driver, self.default_timeout).until(
                    EC.visibility_of_element_located(locator))
                assert web_element.text == text
                self.get_png_allure_image()
                return True
        except Exception as e:
            with allure.step("Unsuccessful"):
                self.get_png_allure_image()
                time.sleep(2)
                return False

    def get_records_from_table(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        return WebDriverWait(self.driver, self.default_timeout).until(
            EC.visibility_of_all_elements_located(locator))

    def get_png_allure_image(self):
        allure.attach(self.driver.get_screenshot_as_png(), name='f_screenshot',
                      attachment_type=AttachmentType.PNG)

    def wait_and_hover(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        web_element = WebDriverWait(self.driver, self.default_timeout).until(
            EC.visibility_of_element_located(locator))
        action = ActionChains(self.driver)
        action.move_to_element(web_element)
        action.perform()

    def verify_image_present(self, locator):
        try:
            with allure.step("Magnified Image Found"):
                WebDriverWait(self.driver, self.default_timeout).until(
                    EC.presence_of_element_located(locator))
                WebDriverWait(self.driver, self.default_timeout).until(
                    EC.visibility_of_element_located(locator))
                self.get_png_allure_image()
                return True
        except Exception as e:
            with allure.step('Input Failed'):
                self.get_png_allure_image()
                time.sleep(2)
                return False
