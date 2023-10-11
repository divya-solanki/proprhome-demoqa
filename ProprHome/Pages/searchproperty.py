from selenium.webdriver.common.by import By
from Utilities.CommonFunction import CommonFunction


class SearchProperty:

    def __init__(self, driver):
        self.driver = driver
        self.cf = CommonFunction(self.driver)

    locator_property_type = (By.XPATH, "//span[@class='home-finder__form__button__title is-type']")
    locator_property_type_house = (By.XPATH, "//span[contains(text(),'House')]")
    locator_property_type_house_next = (By.CSS_SELECTOR, "button[class='home-finder__panel__navigation__btn is-next']")
    locator_property_type_house_bedroom = (By.XPATH, "(//button[@id='bedroom'])[2]")
    locator_property_type_house_bathroom = (By.XPATH, "(//button[@id='bathroom'])[2]")
    locator_property_type_house_price = (By.XPATH, "//span[contains(text(),'200k – 400k')]")
    locator_property_type_house_parking = (By.XPATH, "//span[contains(text(),'Parking')]")
    locator_property_location = (By.XPATH, "//h4[contains(text(),'Abrantes')]")
    location_property_filter = (By.XPATH, "//button[@class='home-finder__panel__type__show-more']")
    location_search_property_button = (By.CSS_SELECTOR, "button[class='home-finder__form__submit']")
    locator_verify_search_result = (By.TAG_NAME, "(//h1)[2]")

    def select_property_type(self):
        self.cf.wait_and_click(self.locator_property_type)

    def select_property_type_house(self):
        self.cf.wait_and_click(self.locator_property_type_house)

    def click_next(self):
        self.cf.wait_and_click(self.locator_property_type_house_next)

    def select_no_of_bedrooms(self):
        self.cf.wait_and_click(self.locator_property_type_house_bedroom)

    def select_no_of_bathrooms(self):
        self.cf.wait_and_click(self.locator_property_type_house_bathroom)

    def select_price_range(self):
        self.cf.wait_and_click(self.locator_property_type_house_price)

    def select_key_feature(self):
        self.cf.wait_and_click(self.locator_property_type_house_parking)

    def select_location(self):
        self.cf.wait_and_click(self.locator_property_location)

    def select_property_feature(self):
        self.cf.wait_and_click(self.location_property_filter)

    def click_search_property_button(self):
        self.cf.wait_and_click(self.location_search_property_button)

    def verify_search_result(self):
        self.cf.verify_page(self.locator_verify_search_result, "Your search results")