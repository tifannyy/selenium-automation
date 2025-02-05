from selenium import webdriver
from selenium.webdriver.common.by import By
from locator import element
from locator import url
from inputData import data
import unittest
import baseLogin

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    
    #OHRM01
    def test_a_login_success(self):
        driver = self.browser
        baseLogin.positive_login(driver)

        #validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.dashboardUrl)
        response_data = driver.find_element(By.CLASS_NAME, element.dashboard).text
        self.assertIn(data.dashboardTxt, response_data)

    #OHRM02
    def test_b_login_invalid_username(self):
        driver = self.browser
        baseLogin.negative_login_invalid_username(driver)

        #validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.baseUrl)
        response_data = driver.find_element(By.CLASS_NAME, element.invalidCred).text
        self.assertIn(data.invalidCred, response_data)

    #OHRM03
    def test_c_login_invalid_password(self):
        driver = self.browser
        baseLogin.negative_login_invalid_password(driver)

        #validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.baseUrl)
        response_data = driver.find_element(By.CLASS_NAME, element.invalidCred).text
        self.assertIn(data.invalidCred, response_data)

    #OHRM04
    def test_d_login_empty_username(self):
        driver = self.browser
        baseLogin.negative_login_empty_username(driver)

        #validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.baseUrl)
        response_data = driver.find_element(By.CLASS_NAME, element.required).text
        self.assertIn(data.required, response_data)

    #OHRM05
    def test_e_login_empty_password(self):
        driver = self.browser
        baseLogin.negative_login_empty_password(driver)

        #validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.baseUrl)
        response_data = driver.find_element(By.CLASS_NAME, element.required).text
        self.assertIn(data.required, response_data)

    #OHRM06
    def test_f_login_blank_all(self):
        driver = self.browser
        baseLogin.negative_login_blank_all(driver)

        #validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.baseUrl)
        response_data = driver.find_element(By.CLASS_NAME, element.required).text
        self.assertIn(data.required, response_data)

    #OHRM07
    def test_g_login_upcase_username(self):
        driver = self.browser 
        baseLogin.negative_login_upcase_username(driver)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.dashboardUrl)
        response_data = driver.find_element(By.CLASS_NAME,element.dashboard).text
        self.assertIn(data.dashboardTxt, response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
    