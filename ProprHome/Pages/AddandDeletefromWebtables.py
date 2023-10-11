import time
from selenium.webdriver.common.by import By
from Utilities.CommonFunction import CommonFunction


class addanddeletefromwebtables:

    def __init__(self, driver):
        self.driver = driver
        self.cf = CommonFunction(self.driver)

    locator_add_button = (By.ID, "addNewRecordButton")
    locator_firstname = (By.ID, "firstName")
    locator_lastname = (By.ID, "lastName")
    locator_age = (By.ID, "age")
    locator_email = (By.ID, "userEmail")
    locator_salary = (By.ID, "salary")
    locator_dept = (By.ID, "department")
    locator_submit_button = (By.ID, "submit")
    locator_verify_data_1 = "//div[@class='rt-tbody']/div["
    locator_verify_data_2 = "]/div/div[4]"
    locator_data_table = (By.XPATH, "//div[@class='rt-tbody']")
    locator_row = (By.CLASS_NAME, "rt-tr-group")
    locator_delete_row_button = (By.XPATH, "//div[@class='rt-tbody']/div/div/div[7]/div/span[2]")
    email = "testmail@gmail.com"

    def get_webpage(self):
        self.driver.get("https://demoqa.com/webtables")

    def click_add_button(self):
        self.cf.wait_and_click(self.locator_add_button)

    def add_details(self):
        self.cf.wait_and_input_text(self.locator_firstname, "Rebecca")
        self.cf.wait_and_input_text(self.locator_lastname, "Meredith")

        self.cf.wait_and_input_text(self.locator_email, self.email)
        self.cf.wait_and_input_text(self.locator_age, "30")
        self.cf.wait_and_input_text(self.locator_salary, "25000")
        self.cf.wait_and_input_text(self.locator_dept, "IT")
        self.cf.wait_and_click(self.locator_submit_button)

        time.sleep(5)

    def verify_data(self):
        records = self.cf.get_records_from_table(self.locator_row)
        no_of_rows = len(records)

        for i in range(1, no_of_rows):
            get_email_from_table = (By.XPATH, self.locator_verify_data_1 + str(i) + self.locator_verify_data_2)
            if get_email_from_table == self.email:
                break
        self.cf.get_png_allure_image()

    def delete_row(self):
        self.cf.wait_and_click(self.locator_delete_row_button)
        time.sleep(5)
