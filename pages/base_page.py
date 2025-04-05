from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.target.com/'
        self.wait = WebDriverWait(self.driver, timeout=10)

    def open_url(self, url):
        """Open the given URL in the browser."""
        self.driver.get(url)

    def find_element(self, *locator):
        """Find a single element."""
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        """Find multiple elements."""
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        """Input text into an input field."""
        self.find_element(*locator).send_keys(text)

    def wait_until_clickable(self, *locator):
        """Wait until an element is clickable."""
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable by {locator}'
        )

    def wait_until_clickable_click(self, *locator):
        """Wait for an element to be clickable and then click it."""
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable by {locator}'
        ).click()

    def wait_until_visible(self, *locator):
        """Wait until an element is visible."""
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element not visible by {locator}'
        )

    def wait_until_invisible(self, *locator):
        """Wait until an element is invisible."""
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element still visible by {locator}'
        )

    def verify_text(self, expected_text, *locator):
        """Verify that the text of an element matches the expected text."""
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, f'Expected text "{expected_text}" did not match actual "{actual_text}"'

    def verify_partial_text(self, expected_text, *locator):
        """Verify that the expected partial text is found in the element's text."""
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f'Expected text "{expected_text}" not found in actual "{actual_text}"'

    def verify_url(self, expected_url):
        """Verify that the current URL matches the expected URL."""
        self.wait.until(EC.url_to_be(expected_url), message=f'URL does not match {expected_url}')

    def verify_partial_url(self, expected_partial_url):
        """Verify that the current URL contains the expected partial URL."""
        self.wait.until(EC.url_contains(expected_partial_url), message=f'URL does not contain {expected_partial_url}')