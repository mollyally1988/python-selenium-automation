from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'search')

    def open_main_page(self):
        self.open_url(self.base_url)
        self.wait_until_clickable(*self.SEARCH_FIELD)

    def __init__(self, driver):
        super().__init__(driver)
        self.sign_in_button = (By.CSS_SELECTOR, '[data-test="header-sign-in"]')

    def click_sign_in_button(self):
        self.click(*self.sign_in_button)

    def click_element(self, locator):
        self.driver.find_element(*locator).click()