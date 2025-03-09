from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get("https://www.target.com/")

#Click SignIn button
driver.find_element(By.XPATH, "//a[@id='account']")

#Click SignIn from side navigation
driver.find_element(By.XPATH, "//a[contains(text(),'Sign in')]")

#Verify SignIn page opened:
driver.find_element(By.XPATH, "//h1[text()='Sign into your Target account']")

#SignIn button is shown (you can just use driver.find_element() to check for element’s presence, no need to assert here)
driver.find_element(By.XPATH,"//button[contains(@type,'submit') and contains(text(),'Sign in')]")


driver.quit()
