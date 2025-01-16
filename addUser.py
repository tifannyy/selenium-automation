from selenium import webdriver
from selenium.webdriver.common.by import By
from locator import element
from locator import url
from inputData import data
import unittest
import baseLogin
import time

class TestAddUser(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    #OHRM09 - Add User
    def test_a_adduser_success(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtn).click()
        time.sleep(1)

        #user role
        driver.find_element(By.CLASS_NAME, element.selectUser).click()
        time.sleep(2)
        driver.find_element(By.XPATH, element.userRole).click()
        time.sleep(1)

        #employee name
        driver.find_element(By.CLASS_NAME, element.employee).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.hintEmployee).send_keys(data.employee)
        time.sleep(3)
        driver.find_element(By.XPATH, element.listEmployee).click()
        time.sleep(1)

        #status
        driver.find_element(By.XPATH, element.selectStatus).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.enable).click()
        time.sleep(1)

        #username & password
        driver.find_element(By.XPATH, element.newUsername).send_keys(data.newUsername) 
        time.sleep(1)
        driver.find_element(By.XPATH, element.newPassword).send_keys(data.newPassword)
        time.sleep(1)
        driver.find_element(By.XPATH, element.confirmPassword).send_keys(data.confirmPassword) 
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtn).click() 
        time.sleep(5)

        #validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.addUserUrl)

    #OHRM10
    def test_b_failed_usnexist(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtn).click()
        time.sleep(1)

        #user role
        driver.find_element(By.CLASS_NAME, element.selectUser).click()
        time.sleep(2)
        driver.find_element(By.XPATH, element.userRole).click()
        time.sleep(1)

        #employee name
        driver.find_element(By.CLASS_NAME, element.employee).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.hintEmployee).send_keys(data.employee)
        time.sleep(3)
        driver.find_element(By.XPATH, element.listEmployee).click()
        time.sleep(1)

        #status
        driver.find_element(By.XPATH, element.selectStatus).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.enable).click()
        time.sleep(1)

        #username & password
        driver.find_element(By.XPATH, element.newUsername).send_keys(data.newUsername) 
        time.sleep(1)
        driver.find_element(By.XPATH, element.newPassword).send_keys(data.newPassword)
        time.sleep(1)
        driver.find_element(By.XPATH, element.confirmPassword).send_keys(data.confirmPassword) 
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtn).click() 
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH, element.existUser).text
        self.assertIn(data.existUser, response_data)

    #OHRM11
    def test_c_failed_blank_userrole(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtn).click()
        time.sleep(1)

        #employee name
        driver.find_element(By.CLASS_NAME, element.employee).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.hintEmployee).send_keys(data.employee)
        time.sleep(3)
        driver.find_element(By.XPATH, element.listEmployee).click()
        time.sleep(1)

        #status
        driver.find_element(By.XPATH, element.selectStatus).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.enable).click()
        time.sleep(1)

        #username & password
        driver.find_element(By.XPATH, element.newUsername).send_keys(data.newUser2) 
        time.sleep(1)
        driver.find_element(By.XPATH, element.newPassword).send_keys(data.newPassword)
        time.sleep(1)
        driver.find_element(By.XPATH, element.confirmPassword).send_keys(data.confirmPassword) 
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtn).click() 
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH, element.blankRole).text
        self.assertIn(data.requiredAdd, response_data)

    #OHRM12
    def test_d_failed_blank_employee(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtn).click()
        time.sleep(1)

        #user role
        driver.find_element(By.CLASS_NAME, element.selectUser).click()
        time.sleep(2)
        driver.find_element(By.XPATH, element.userRole).click()
        time.sleep(1)

        #status
        driver.find_element(By.XPATH, element.selectStatus).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.enable).click()
        time.sleep(1)

        #username & password
        driver.find_element(By.XPATH, element.newUsername).send_keys(data.newUser2) 
        time.sleep(1)
        driver.find_element(By.XPATH, element.newPassword).send_keys(data.newPassword)
        time.sleep(1)
        driver.find_element(By.XPATH, element.confirmPassword).send_keys(data.confirmPassword) 
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtn).click() 
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH, element.blankEmployee).text
        self.assertIn(data.requiredAdd, response_data)

    #OHRM13
    def test_e_failed_blank_status(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtn).click()
        time.sleep(1)

        #user role
        driver.find_element(By.CLASS_NAME, element.selectUser).click()
        time.sleep(2)
        driver.find_element(By.XPATH, element.userRole).click()
        time.sleep(1)

        #employee name
        driver.find_element(By.CLASS_NAME, element.employee).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.hintEmployee).send_keys(data.employee)
        time.sleep(3)
        driver.find_element(By.XPATH, element.listEmployee).click()
        time.sleep(1)

        #username & password
        driver.find_element(By.XPATH, element.newUsername).send_keys(data.newUser2) 
        time.sleep(1)
        driver.find_element(By.XPATH, element.newPassword).send_keys(data.newPassword)
        time.sleep(1)
        driver.find_element(By.XPATH, element.confirmPassword).send_keys(data.confirmPassword) 
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtn).click() 
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH, element.blankStatus).text
        self.assertIn(data.requiredAdd, response_data)

    #OHRM14
    def test_f_failed_blank_username(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtn).click()
        time.sleep(1)

        #user role
        driver.find_element(By.CLASS_NAME, element.selectUser).click()
        time.sleep(2)
        driver.find_element(By.XPATH, element.userRole).click()
        time.sleep(1)

        #employee name
        driver.find_element(By.CLASS_NAME, element.employee).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.hintEmployee).send_keys(data.employee)
        time.sleep(3)
        driver.find_element(By.XPATH, element.listEmployee).click()
        time.sleep(1)

        #status
        driver.find_element(By.XPATH, element.selectStatus).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.enable).click()
        time.sleep(1)

        #username & password
        driver.find_element(By.XPATH, element.newPassword).send_keys(data.newPassword)
        time.sleep(1)
        driver.find_element(By.XPATH, element.confirmPassword).send_keys(data.confirmPassword) 
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtn).click() 
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH, element.blankUsername).text
        self.assertIn(data.requiredAdd, response_data)

    #OHRM15
    def test_g_failed_blank_password(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtn).click()
        time.sleep(1)

        #user role
        driver.find_element(By.CLASS_NAME, element.selectUser).click()
        time.sleep(2)
        driver.find_element(By.XPATH, element.userRole).click()
        time.sleep(1)

        #employee name
        driver.find_element(By.CLASS_NAME, element.employee).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.hintEmployee).send_keys(data.employee)
        time.sleep(3)
        driver.find_element(By.XPATH, element.listEmployee).click()
        time.sleep(1)

        #status
        driver.find_element(By.XPATH, element.selectStatus).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.enable).click()
        time.sleep(1)

        #username & password
        driver.find_element(By.XPATH, element.newUsername).send_keys(data.newUser2) 
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtn).click() 
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH, element.blankPassword).text
        self.assertIn(data.requiredAdd, response_data)

    #OHRM16
    def test_h_failed_invalid_username(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtn).click()
        time.sleep(1)

        #user role
        driver.find_element(By.CLASS_NAME, element.selectUser).click()
        time.sleep(2)
        driver.find_element(By.XPATH, element.userRole).click()
        time.sleep(1)

        #employee name
        driver.find_element(By.CLASS_NAME, element.employee).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.hintEmployee).send_keys(data.employee)
        time.sleep(3)
        driver.find_element(By.XPATH, element.listEmployee).click()
        time.sleep(1)

        #status
        driver.find_element(By.XPATH, element.selectStatus).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.enable).click()
        time.sleep(1)

        #username & password
        driver.find_element(By.XPATH, element.newUsername).send_keys(data.invUser) 
        time.sleep(1)
        driver.find_element(By.XPATH, element.newPassword).send_keys(data.newPassword)
        time.sleep(1)
        driver.find_element(By.XPATH, element.confirmPassword).send_keys(data.confirmPassword) 
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtn).click() 
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH, element.invalidUser).text
        self.assertIn(data.userInv, response_data)

    #OHRM17
    def test_i_failed_invalid_password(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtn).click()
        time.sleep(1)

        #user role
        driver.find_element(By.CLASS_NAME, element.selectUser).click()
        time.sleep(2)
        driver.find_element(By.XPATH, element.userRole).click()
        time.sleep(1)

        #employee name
        driver.find_element(By.CLASS_NAME, element.employee).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.hintEmployee).send_keys(data.employee)
        time.sleep(3)
        driver.find_element(By.XPATH, element.listEmployee).click()
        time.sleep(1)

        #status
        driver.find_element(By.XPATH, element.selectStatus).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.enable).click()
        time.sleep(1)

        #username & password
        driver.find_element(By.XPATH, element.newUsername).send_keys(data.newUser2)
        time.sleep(1)
        driver.find_element(By.XPATH, element.newPassword).send_keys(data.invPass)
        time.sleep(1)
        driver.find_element(By.XPATH, element.confirmPassword).send_keys(data.invPass)
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtn).click()
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH, element.invalidPassword).text
        self.assertIn(data.passInv, response_data)

    #OHRM18
    def test_j_failed_invalid_confpass(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtn).click()
        time.sleep(1)

        #user role
        driver.find_element(By.CLASS_NAME, element.selectUser).click()
        time.sleep(2)
        driver.find_element(By.XPATH, element.userRole).click()
        time.sleep(1)

        #employee name
        driver.find_element(By.CLASS_NAME, element.employee).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.hintEmployee).send_keys(data.employee)
        time.sleep(3)
        driver.find_element(By.XPATH, element.listEmployee).click()
        time.sleep(1)

        #status
        driver.find_element(By.XPATH, element.selectStatus).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.enable).click()
        time.sleep(1)

        #username & password
        driver.find_element(By.XPATH, element.newUsername).send_keys(data.newUser2)
        time.sleep(1)
        driver.find_element(By.XPATH, element.newPassword).send_keys(data.newPassword)
        time.sleep(1)
        driver.find_element(By.XPATH, element.confirmPassword).send_keys(data.invPass)
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtn).click()
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH, element.invalidConfPass).text
        self.assertIn(data.confirmInv, response_data)

    #OHRM19
    def test_k_failed_blankall(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.XPATH, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtn).click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.XPATH, element.blankField).text
        self.assertIn(data.requiredAdd, response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()