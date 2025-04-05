from selenium.webdriver.common.by import By
from behave import given, when, then


CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify cart has correct product')
def verify_product_name(context):
    context.app.cart_page.verify_product_name_in_cart(context.product_name)
    # context.product_name => stored before
    #product_name_in_cart = context.driver.find_element(*CART_ITEM_TITLE).text
    #print('Name in cart: ', product_name_in_cart)
    #assert context.product_name[:20] == product_name_in_cart[:20], \
    #    f'Expected {context.product_name[:20]} did not match {product_name_in_cart[:20]}'


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    context.app.cart_page.verify_cart_items(amount)
    #cart_summary = context.driver.find_element(*CART_SUMMARY).text
    #assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()


@then('Verify cart page opens')
def verify_cart_page_opens(context):
    context.app.cart_page.verify_cart_page_opens()