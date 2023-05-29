
from logging import PlaceHolder
from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

kunci = [
    ("standard_user", "secret"),                 # username benar password salah
    ("standard", "secret_sauce"),                # username salah password benar
    ("testing", "testing")                       # username salah password salah
]
kunci_valid = [                                                 
    ("standard_user", "secret_sauce")            # username benar password benar
]
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Testing Negative Case Login
@pytest.mark.parametrize("un, pw", kunci)
def test_login_negative(un, pw):
    driver.find_element(By.CSS_SELECTOR,"#user-name").send_keys(un)
    driver.find_element(By.ID,"password").send_keys(pw)
    driver.find_element(By.ID,"login-button").click()
    message = driver.find_element(By.CSS_SELECTOR, "[data-test=error]").text

    assert message == "Epic sadface: Username and password do not match any user in this service"
    driver.refresh()

# Testing Positive Case Login
@pytest.mark.parametrize("us, ps", kunci_valid)
def test_positive_login(us, ps):
    driver.find_element(By.CSS_SELECTOR,"#user-name").send_keys(us)
    driver.find_element(By.ID,"password").send_keys(ps)
    driver.find_element(By.ID,"login-button").click()
    exp_login = ("https://www.saucedemo.com/inventory.html")
    assert exp_login == driver.current_url

    time.sleep(5)

# Testing Logout
def test_logout():
    btn_menu = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "bm-burger-button")))
    btn_menu.click()
    btn_logout = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))
    btn_logout.click()
    login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "login-button")))
    assert login_button.is_displayed()
    time.sleep(10)
