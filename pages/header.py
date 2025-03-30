from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    #SIGN_IN_BTN = (By.XPATH, "//*[@data-test='accountNav-signIn']")
    SIDE_MENU_SIGN_IN = (By.XPATH, "//*[@data-test='accountNav-signIn']")
    SIGN_IN_BTN = ((By.XPATH, "//*[@data-test='@web/AccountLink']"))

    def open_sign_in_menu(self):
        """Click 'Sign In' to open side menu"""
        self.click(*self.SIGN_IN_BTN)

    def click_side_menu_sign_in(self):
        """Click 'Sign In' inside the side menu"""
        self.click(*self.SIDE_MENU_SIGN_IN)


    def search(self, text):
        print(f'Searching for {text}')
        self.input_text(text, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

    def click_cart(self):
        self.click(*self.CART_ICON)

    def click_sign_in(self):
        """Click the Sign In button in the header."""
        self.click(*self.SIGN_IN_BTN)

    def is_sign_in_button_visible(self):
        """Check if the Sign In button is visible in the header."""
        return self.is_element_visible(*self.SIGN_IN_BTN)
