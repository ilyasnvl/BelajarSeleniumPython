from turtle import clear
from typing_extensions import assert_type
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
    button = driver.find_element(By.ID,"login-button").click()
    message = driver.find_element(By.CSS_SELECTOR, "[data-test=error]").text
    assert "Epic sadface: Username and password do not match any user in this service" in message
    btn_close_ticker = driver.find_element(By.CLASS_NAME, "error-button").click()
    time.sleep(2)
    driver.refresh()



