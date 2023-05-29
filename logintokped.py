import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://staging.tokopedia.com/")

def test_login():
        driver.find_element(By.CSS_SELECTOR, "[data-testid=btnHeaderLogin]").click()
        WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "css-1f0x5lg-unf-modal.e1nc1fa21")))
        driver.find_element(By.ID, "email-phone").send_keys("pbs-ilyas+ext.pms5@tokopedia.com")
        driver.find_element(By.ID, "email-phone-submit").click()
        time.sleep(2)
        driver.find_element(By.ID, "password-input").send_keys("tokopedia789")
        driver.find_element(By.CSS_SELECTOR, "span[aria-label='login-button']").click()
        time.sleep(10)

def test_logout():
        # Cara 1
        # menu = driver.find_element(By.ID, "my-profile-header")
        # hover = ActionChains(driver).move_to_element(menu)
        # hover.perform()
        WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "[aria-labelledby=unf-modal-title]")))
        driver.find_element(By.CLASS_NAME, "css-12huuhu").click()

        # Cara 2
        ActionChains(driver).move_to_element((driver.find_element(By.CSS_SELECTOR, "[data-testid=btnHeaderMyProfile]"))).perform()
        driver.find_element(By.XPATH, "//div[@class='css-1juts7j']").click()
        time.sleep(10)

 
    