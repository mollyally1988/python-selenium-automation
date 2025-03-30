from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class SearchResultsPage(Page):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
    LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
    PRODUCT_IMG = (By.CSS_SELECTOR, 'img')

    def add_product_to_cart(self):
        self.find_element(*self.ADD_TO_CART_BTN).click()

    def store_product_name(self):
        product_name = self.find_element(*self.SIDE_NAV_PRODUCT_NAME).text
        return product_name

    def confirm_add_to_cart_from_side_nav(self):
        self.find_element(*self.SIDE_NAV_ADD_TO_CART_BTN).click()

    def verify_search_results(self, expected_text):
        assert expected_text in self.find_element(*self.SEARCH_RESULTS_TEXT).text, \
            f"Expected {expected_text} in search results, but got {self.find_element(*self.SEARCH_RESULTS_TEXT).text}"

    def verify_results_url(self, expected_text):
        assert expected_text in self.driver.current_url, \
            f"Expected {expected_text} in URL, but got {self.driver.current_url}"