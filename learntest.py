
from logging import PlaceHolder
from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
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
    expected_login = driver.find_element(By.XPATH, "//span[@class='title']").text

    assert expected_login == "Products"

    time.sleep(2)

# Testing Logout
def test_logout():
    inventory_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))

    # Klik tombol Menu
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()

    # Klik tombol Logout
    logout_button = driver.find_element(By.ID, "logout_sidebar_link")
    logout_button.click()

    # Tunggu hingga halaman Login kembali terbuka
    login_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login_logo")))

    # Menutup WebDriver
    driver.quit()
    # menuBtn = driver.find_element(By.CLASS_NAME, "bm-burger-button")
    # menuBtn.click()
    # logout_button = driver.find_element(By.ID, "logout_sidebar_link")
    # logout_button.click()
    # test_logout()
    # time.sleep(5)
    # driver.find_element(By.ID, "logout_sidebar_link").click
    # result = driver.current_url

    # assert result == "https://www.saucedemo.com"

