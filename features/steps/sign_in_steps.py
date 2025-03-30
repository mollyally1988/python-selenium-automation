from behave import given, when, then


#@given('Open Target main page')
#def open_target_main_page(context):
#    context.driver.get("https://www.target.com")  # Assuming you want to open the main page here

@when('Click Sign In in header')
def click_header_sign_in(context):
    context.app.header.open_sign_in_menu()

@when('Click Sign In from side menu')
def click_side_menu_sign_in(context):
    context.app.header.click_side_menu_sign_in()

@then('Verify Sign In page is opened')
def verify_sign_in_page(context):
    context.app.sign_in_page.verify_sign_in_page_opened()