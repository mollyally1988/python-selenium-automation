from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

def browser_init(context):

    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)



def before_scenario(context, scenario):
    """Hook executed before each test scenario"""
    browser_init(context)  # Initialize the browser


def after_scenario(context, scenario):
    """Hook executed after each test scenario"""
    context.driver.quit()  # Quit the browser after scenario


def before_all(context):
    # Initialize the browser instance here (e.g., Chrome WebDriver).
    context.browser = webdriver.Chrome()  # Use the appropriate WebDriver for your setup.


def after_all(context):
    # Quit the browser after all tests complete to clean up resources.
    if context.browser:
        context.browser.quit()
