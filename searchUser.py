from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locator import element
from locator import url
from inputData import data
import unittest
import baseLogin
import time

class TestAddUser(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    #OHRM44 - Search User
    def test_a_search_by_username(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.usernameSearch).send_keys(data.newUsername)
        time.sleep(1)
        driver.find_element(By.XPATH, element.searchButton).click()
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH, element.searchFoundUser).text
        self.assertIn("Record Found", response_data)

    #OHRM45
    def test_b_search_by_userrole(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.userRoleSearch).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.adminSearch).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.searchButton).click()
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH, element.searchFoundUser).text
        self.assertIn(data.searchFound, response_data)

    #OHRM46
    def test_c_search_by_status(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.statusSearch).click()
        driver.find_element(By.XPATH, element.enableSearch).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.searchButton).click()
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH, element.searchFoundUser).text
        self.assertIn(data.searchFound, response_data)

    #OHRM47
    def test_d_search_by_invalid_username(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.usernameSearch).send_keys(data.invUser)
        time.sleep(1)
        driver.find_element(By.XPATH, element.searchButton).click()
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH, element.searchNotFoundUser).text
        self.assertIn(response_data, data.searchNotFound)

    #OHRM48
    def test_e_cancel_search(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.usernameSearch).send_keys(data.newUsername)
        time.sleep(1)
        driver.find_element(By.XPATH, element.userRoleSearch).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.adminSearch).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.statusSearch).click()
        driver.find_element(By.XPATH, element.enableSearch).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.resetButton).click()
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH, element.reset).text
        self.assertIn(response_data, data.reset)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()