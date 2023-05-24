import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="session")
def browser():
    # Menentukan path ke ChromeDriver
    webdriver_service = Service('path/to/chromedriver')

    # Inisialisasi WebDriver
    driver = webdriver.Chrome(service=webdriver_service)
    yield driver

    # Menutup WebDriver setelah selesai
    driver.quit()

def test_logout(browser):
    wait = WebDriverWait(browser, 10)

    # Membuka website Saucedemo.com
    browser.get("https://www.saucedemo.com/")

    # Masukkan username dan password
    username = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")

    # Klik tombol Login
    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()

    # Tunggu hingga halaman Inventory terbuka
    inventory_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))

    # Klik tombol Menu
    menu_button = browser.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()

    # Klik tombol Logout
    logout_button = browser.find_element(By.ID, "logout_sidebar_link")
    logout_button.click()

    # Tunggu hingga halaman Login kembali terbuka
    login_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login_logo")))
    
