from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):
    HEADER_TEXT = (By.XPATH, "//h1[contains(@class, 'styles_ndsHeading')]")
    LOGIN_BUTTON = (By.ID, "login")

    def verify_sign_in_page_opened(self):
        # Update expected text to match actual page text
        self.verify_text('Sign in or create account', *self.HEADER_TEXT)
        assert self.find_element(*self.LOGIN_BUTTON).is_displayed(), 'Login button is not visible'


