import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()
driver.get("https://www.tokopedia.com/")

def test_login():
        driver.find_element(By.CSS_SELECTOR, "[data-testid=btnHeaderLogin]").click()
        WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "css-1f0x5lg-unf-modal.e1nc1fa21")))
        driver.find_element(By.ID, "email-phone").send_keys("pbs-ilyas+pmb1@tokopedia.com")
        driver.find_element(By.ID, "email-phone-submit").click()
        time.sleep(5)
        driver.find_element(By.ID, "password-input").send_keys("tokopedia789")
        driver.find_element(By.CSS_SELECTOR, "span[aria-label='login-button']").click()
        time.sleep(5)

def test_logout():
        driver.find_element()
     
    
    