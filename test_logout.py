import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    # Inisialisasi webdriver
    driver = webdriver.Chrome()
    yield driver
    # Tutup browser setelah pengujian selesai
    driver.quit()

# Tes login
def test_login(browser):
    # Buka halaman login
    browser.get("https://www.saucedemo.com/")
    # Masukkan username dan password
    username = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    password = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    # Submit form login
    browser.find_element(By.ID, "login-button").click()
    # Verifikasi bahwa login berhasil
    inventory_title = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )
    assert "Products" in inventory_title.text

# Tes logout
def test_logout(browser):
    # Buka halaman login
    browser.get("https://www.saucedemo.com/")
    # Masukkan username dan password
    username = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    password = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    # Submit form login
    browser.find_element(By.ID, "login-button").click()
    # Logout
    menu_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bm-burger-button"))
    )
    menu_button.click()
    logout_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "logout_sidebar_link"))
    )
    logout_button.click()
    # Verifikasi bahwa logout berhasil
    login_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "login-button"))
    )
    assert login_button.is_displayed()