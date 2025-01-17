from selenium import webdriver
from selenium.webdriver.common.by import By
from locator import element
from locator import url
from inputData import data
import unittest
import baseLogin
import time

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    #OHRM08
    def test_logout_success(self):
        driver = self.browser
        baseLogin.positive_login(driver)

        driver.find_element(By.CLASS_NAME, element.userProfil).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.logoutBtn).click()
        time.sleep(3)

        response_url = driver.current_url
        self.assertEqual(response_url, url.baseUrl)
        response_data = driver.find_element(By.CLASS_NAME, element.loginPage).text
        self.assertIn(data.loginTxt, response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()