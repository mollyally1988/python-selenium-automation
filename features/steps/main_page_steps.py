from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignInPage:
    def __init__(self, driver):
        self.driver = driver
        self.SIGN_IN_BUTTON = (By.XPATH, "//*[@data-test='accountNav-signIn']")
        self.HEADER_TEXT = (By.XPATH, "//h1[contains(@class, 'styles_ndsHeading')]")
        self.EMAIL_INPUT = (By.ID, "username")
        self.PASSWORD_INPUT = (By.ID, "password")
        self.LOGIN_BUTTON = (By.ID, "login")

    def click_sign_in(self):
        # Wait for the Sign In button and click it
        sign_in_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SIGN_IN_BUTTON)
        )
        sign_in_button.click()

    def verify_sign_in_page(self):
        # Verify the header text is correct
        header_text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.HEADER_TEXT)
        ).text
        assert header_text == 'Sign into your Target account', f'Expected "Sign into your Target account", but got {header_text}'

    def is_login_button_visible(self):
        # Check if the login button is visible
        login_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LOGIN_BUTTON)
        )
        return login_button.is_displayed()

    def enter_credentials(self, email, password):
        # Enter email and password into the respective input fields
        email_input = self.driver.find_element(*self.EMAIL_INPUT)
        email_input.send_keys(email)

        password_input = self.driver.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)

    def click_login(self):
        # Click the login button
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()
