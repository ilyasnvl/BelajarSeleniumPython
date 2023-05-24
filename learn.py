from turtle import clear
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = ChromeService(executable_path="chromedriver")

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.saucedemo.com/")

# Negative Case Login
def test_negative_login():
    driver.find_element(By.CSS_SELECTOR,"#user-name").send_keys("standard_users")
    driver.find_element(By.ID,"password").send_keys("secret_sauces")
    driver.find_element(By.ID,"login-button").click()
    message = driver.find_element(By.CSS_SELECTOR, "[data-test=error]").text
    assert "Epic sadface: Username and password do not match any user in this service" in message
    driver.find_element(By.CLASS_NAME, "error-button").click()
    time.sleep(5)

def test_eight_components():
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    time.sleep(10)




