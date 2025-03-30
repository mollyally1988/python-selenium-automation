from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
    CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")

    def verify_cart_empty(self):
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

    def verify_cart_page_opens(self):
        self.verify_url(f'{self.base_url}cart')  # 'https://www.target.com/' + 'cart'

    def verify_product_name_in_cart(self, expected_product_name):
        product_name_in_cart = self.find_element(*self.CART_ITEM_TITLE).text
        assert expected_product_name[:20] == product_name_in_cart[:20], \
            f'Expected {expected_product_name[:20]} did not match {product_name_in_cart[:20]}'

    def verify_cart_items(self, amount):
        cart_summary = self.find_element(*self.CART_SUMMARY).text
        assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"