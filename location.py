from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locator import element
from locator import url
from inputData import data
import unittest
import baseLogin
import time

class TestLocation(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    #OHRM20 - Add Location
    def test_a_add_location_success(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtnLoc).click()
        time.sleep(1)

        #add location
        driver.find_element(By.XPATH, element.nameLoc).send_keys(data.name)
        time.sleep(1)
        driver.find_element(By.XPATH, element.city).send_keys(data.city)
        time.sleep(1)
        driver.find_element(By.XPATH, element.state).send_keys(data.state)
        time.sleep(1)
        driver.find_element(By.XPATH, element.pCode).send_keys(data.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys("i")
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.phone).send_keys(data.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, element.fax).send_keys(data.fax)
        time.sleep(1)
        driver.find_element(By.XPATH, element.address).send_keys(data.address)
        time.sleep(1)
        driver.find_element(By.XPATH, element.notes).send_keys(data.notes)
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtnLoc).click()
        time.sleep(5)
        
        #validasi
        response_url = driver.current_url
        self.assertEqual(url.addLocUrl, response_url)

    #OHRM21
    def test_b_failed_blank_name(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtnLoc).click()
        time.sleep(1)

        #blank name
        driver.find_element(By.XPATH, element.city).send_keys(data.city)
        time.sleep(1)
        driver.find_element(By.XPATH, element.state).send_keys(data.state)
        time.sleep(1)
        driver.find_element(By.XPATH, element.pCode).send_keys(data.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys("i")
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.phone).send_keys(data.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, element.fax).send_keys(data.fax)
        time.sleep(1)
        driver.find_element(By.XPATH, element.address).send_keys(data.address)
        time.sleep(1)
        driver.find_element(By.XPATH, element.notes).send_keys(data.notes)
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtnLoc).click()
        time.sleep(5)

        #validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.failedAddLoc)

    #OHRM22
    def test_c_blank_city_success(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtnLoc).click()
        time.sleep(1)

        #blank city
        driver.find_element(By.XPATH, element.nameLoc).send_keys("kim2")
        time.sleep(1)
        driver.find_element(By.XPATH, element.state).send_keys(data.state)
        time.sleep(1)
        driver.find_element(By.XPATH, element.pCode).send_keys(data.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys("i")
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.phone).send_keys(data.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, element.fax).send_keys(data.fax)
        time.sleep(1)
        driver.find_element(By.XPATH, element.address).send_keys(data.address)
        time.sleep(1)
        driver.find_element(By.XPATH, element.notes).send_keys(data.notes)
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtnLoc).click()
        time.sleep(5)
        
        #validasi
        response_url = driver.current_url
        self.assertEqual(url.addLocUrl, response_url)
        
    #OHRM23        
    def test_d_blank_state_success(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtnLoc).click()
        time.sleep(1)

        #blank state
        driver.find_element(By.XPATH, element.nameLoc).send_keys("kim3")
        time.sleep(1)
        driver.find_element(By.XPATH, element.city).send_keys(data.city)
        time.sleep(1)
        driver.find_element(By.XPATH, element.pCode).send_keys(data.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys("i")
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.phone).send_keys(data.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, element.fax).send_keys(data.fax)
        time.sleep(1)
        driver.find_element(By.XPATH, element.address).send_keys(data.address)
        time.sleep(1)
        driver.find_element(By.XPATH, element.notes).send_keys(data.notes)
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtnLoc).click()
        time.sleep(5)
        
        #validasi
        response_url = driver.current_url
        self.assertEqual(url.addLocUrl, response_url)

    #OHRM24
    def test_e_blank_pcode_success(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtnLoc).click()
        time.sleep(1) 

        #blank pcode
        driver.find_element(By.XPATH, element.nameLoc).send_keys("kim4")
        time.sleep(1)
        driver.find_element(By.XPATH, element.city).send_keys(data.city)
        time.sleep(1)
        driver.find_element(By.XPATH, element.state).send_keys(data.state)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys("i")
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.phone).send_keys(data.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, element.fax).send_keys(data.fax)
        time.sleep(1)
        driver.find_element(By.XPATH, element.address).send_keys(data.address)
        time.sleep(1)
        driver.find_element(By.XPATH, element.notes).send_keys(data.notes)
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtnLoc).click()
        time.sleep(5)
        
        #validasi
        response_url = driver.current_url
        self.assertEqual(url.addLocUrl, response_url)   

    #OHRM25
    def test_f_failed_blank_country(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtnLoc).click()
        time.sleep(1)

        #blank country
        driver.find_element(By.XPATH, element.nameLoc).send_keys("kim5")
        time.sleep(1)
        driver.find_element(By.XPATH, element.city).send_keys(data.city)
        time.sleep(1)
        driver.find_element(By.XPATH, element.state).send_keys(data.state)
        time.sleep(1)
        driver.find_element(By.XPATH, element.pCode).send_keys(data.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, element.phone).send_keys(data.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, element.fax).send_keys(data.fax)
        time.sleep(1)
        driver.find_element(By.XPATH, element.address).send_keys(data.address)
        time.sleep(1)
        driver.find_element(By.XPATH, element.notes).send_keys(data.notes)
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtnLoc).click()
        time.sleep(5)
        
        #validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.failedAddLoc)

    #OHRM26
    def test_g_blank_phone_success(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtnLoc).click()
        time.sleep(1)

        #blank phone
        driver.find_element(By.XPATH, element.nameLoc).send_keys("kim6")
        time.sleep(1)
        driver.find_element(By.XPATH, element.city).send_keys(data.city)
        time.sleep(1)
        driver.find_element(By.XPATH, element.state).send_keys(data.state)
        time.sleep(1)
        driver.find_element(By.XPATH, element.pCode).send_keys(data.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys("i")
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.fax).send_keys(data.fax)
        time.sleep(1)
        driver.find_element(By.XPATH, element.address).send_keys(data.address)
        time.sleep(1)
        driver.find_element(By.XPATH, element.notes).send_keys(data.notes)
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtnLoc).click()
        time.sleep(5)
        
        #validasi
        response_url = driver.current_url
        self.assertEqual(url.addLocUrl, response_url)

    #OHRM27
    def test_h_blank_fax_success(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtnLoc).click()
        time.sleep(1)

        #blank fax
        driver.find_element(By.XPATH, element.nameLoc).send_keys("kim7")
        time.sleep(1)
        driver.find_element(By.XPATH, element.city).send_keys(data.city)
        time.sleep(1)
        driver.find_element(By.XPATH, element.state).send_keys(data.state)
        time.sleep(1)
        driver.find_element(By.XPATH, element.pCode).send_keys(data.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys("i")
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.phone).send_keys(data.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, element.address).send_keys(data.address)
        time.sleep(1)
        driver.find_element(By.XPATH, element.notes).send_keys(data.notes)
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtnLoc).click()
        time.sleep(5)
        
        #validasi
        response_url = driver.current_url
        self.assertEqual(url.addLocUrl, response_url)

    #OHRM28
    def test_i_blank_address_success(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtnLoc).click()
        time.sleep(1)

        #blank address
        driver.find_element(By.XPATH, element.nameLoc).send_keys("kim8")
        time.sleep(1)
        driver.find_element(By.XPATH, element.city).send_keys(data.city)
        time.sleep(1)
        driver.find_element(By.XPATH, element.state).send_keys(data.state)
        time.sleep(1)
        driver.find_element(By.XPATH, element.pCode).send_keys(data.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys("i")
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.phone).send_keys(data.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, element.fax).send_keys(data.fax)
        time.sleep(1)
        driver.find_element(By.XPATH, element.notes).send_keys(data.notes)
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtnLoc).click()
        time.sleep(5)
        
        #validasi
        response_url = driver.current_url
        self.assertEqual(url.addLocUrl, response_url)

    #OHRM29
    def test_k_blank_notes_success(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtnLoc).click()
        time.sleep(1)

        #blank notes
        driver.find_element(By.XPATH, element.nameLoc).send_keys("kim9")
        time.sleep(1)
        driver.find_element(By.XPATH, element.city).send_keys(data.city)
        time.sleep(1)
        driver.find_element(By.XPATH, element.state).send_keys(data.state)
        time.sleep(1)
        driver.find_element(By.XPATH, element.pCode).send_keys(data.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys("i")
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.phone).send_keys(data.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, element.fax).send_keys(data.fax)
        time.sleep(1)
        driver.find_element(By.XPATH, element.address).send_keys(data.address)
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtnLoc).click()
        time.sleep(5)
        
        #validasi
        response_url = driver.current_url
        self.assertEqual(url.addLocUrl, response_url)

    #OHRM30
    def test_l_failed_blank_all(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtnLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtnLoc).click()
        time.sleep(5)
        
        #validasi
        response_url = driver.current_url
        self.assertEqual(url.failedAddLoc, response_url)

    #OHRM31
    def test_m_failed_invalid_phone(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtnLoc).click()
        time.sleep(1)

        #invalid phone
        driver.find_element(By.XPATH, element.nameLoc).send_keys("kim10")
        time.sleep(1)
        driver.find_element(By.XPATH, element.city).send_keys(data.city)
        time.sleep(1)
        driver.find_element(By.XPATH, element.state).send_keys(data.state)
        time.sleep(1)
        driver.find_element(By.XPATH, element.pCode).send_keys(data.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys("i")
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.phone).send_keys(data.invPhone)
        time.sleep(1)
        driver.find_element(By.XPATH, element.fax).send_keys(data.fax)
        time.sleep(1)
        driver.find_element(By.XPATH, element.address).send_keys(data.address)
        time.sleep(1)
        driver.find_element(By.XPATH, element.notes).send_keys(data.notes)
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtnLoc).click()
        time.sleep(5)
        
        #validasi
        response_url = driver.current_url
        self.assertEqual(url.failedAddLoc, response_url)

    #OHRM32
    def test_n_failed_invalid_fax(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtnLoc).click()
        time.sleep(1)

        #invalid fax
        driver.find_element(By.XPATH, element.nameLoc).send_keys("kim11")
        time.sleep(1)
        driver.find_element(By.XPATH, element.city).send_keys(data.city)
        time.sleep(1)
        driver.find_element(By.XPATH, element.state).send_keys(data.state)
        time.sleep(1)
        driver.find_element(By.XPATH, element.pCode).send_keys(data.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys("i")
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.phone).send_keys(data.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, element.fax).send_keys(data.invFax)
        time.sleep(1)
        driver.find_element(By.XPATH, element.address).send_keys(data.address)
        time.sleep(1)
        driver.find_element(By.XPATH, element.notes).send_keys(data.notes)
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveBtnLoc).click()
        time.sleep(5)
        
        #validasi
        response_url = driver.current_url
        self.assertEqual(url.failedAddLoc, response_url)

    #OHRM33
    def test_o_cancel_add_location(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.addBtnLoc).click()
        time.sleep(1)

        #cancel add loc
        driver.find_element(By.XPATH, element.nameLoc).send_keys("kim12")
        time.sleep(1)
        driver.find_element(By.XPATH, element.city).send_keys(data.city)
        time.sleep(1)
        driver.find_element(By.XPATH, element.state).send_keys(data.state)
        time.sleep(1)
        driver.find_element(By.XPATH, element.pCode).send_keys(data.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys("i")
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.country).send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.phone).send_keys(data.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, element.fax).send_keys(data.fax)
        time.sleep(1)
        driver.find_element(By.XPATH, element.address).send_keys(data.address)
        time.sleep(1)
        driver.find_element(By.XPATH, element.notes).send_keys(data.notes)
        time.sleep(1)
        driver.find_element(By.XPATH, element.cancelBtnLoc).click()
        time.sleep(5)
        
        #validasi
        response_url = driver.current_url
        self.assertEqual(url.addLocUrl, response_url)

    #OHRM34 - Search Location
    def test_p_search_location_success(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)

        #search location
        driver.find_element(By.XPATH, element.nameSearch).send_keys(data.name)
        time.sleep(1)
        driver.find_element(By.XPATH, element.citySearch).send_keys(data.city)
        time.sleep(1)
        driver.find_element(By.XPATH, element.countrySearch).send_keys("iii")
        time.sleep(1)
        driver.find_element(By.XPATH, element.countrySearch).send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.searchBtn).click()
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH, element.searchFound).text
        self.assertIn(data.searchFound, response_data)

    #OHRM35
    def test_q_search_location_by_name(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)

        #search by name
        driver.find_element(By.XPATH, element.nameSearch).send_keys(data.name)
        time.sleep(1)
        driver.find_element(By.XPATH, element.searchBtn).click()
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH, element.searchFound).text
        self.assertIn(data.searchFound, response_data)

    #OHRM36
    def test_r_search_location_by_city(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)

        #search by city
        driver.find_element(By.XPATH, element.citySearch).send_keys(data.city)
        time.sleep(1)
        driver.find_element(By.XPATH, element.searchBtn).click()
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH, element.searchFound).text
        self.assertIn(data.searchFound, response_data)

    #OHRM37
    def test_s_search_location_by_country(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)

        #search by country
        driver.find_element(By.XPATH, element.countrySearch).send_keys("iii")
        time.sleep(1)
        driver.find_element(By.XPATH, element.countrySearch).send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.searchBtn).click()
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH, element.searchFound).text
        self.assertIn(data.searchFound, response_data)

    #OHRM38
    def test_t_search_location_by_invname(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)

        #search by invalid name
        driver.find_element(By.XPATH, element.nameSearch).send_keys(data.invName)
        time.sleep(1)
        driver.find_element(By.XPATH, element.searchBtn).click()
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH, element.searchNotFound).text
        self.assertIn(data.searchNotFound, response_data)

    #OHRM39
    def test_u_search_location_by_invcity(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)

        #search by invalid city
        driver.find_element(By.XPATH, element.citySearch).send_keys(data.invCity)
        time.sleep(1)
        driver.find_element(By.XPATH, element.searchBtn).click()
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH, element.searchNotFound).text
        self.assertIn(data.searchNotFound, response_data)

    #OHRM40 - Edit Location
    def test_v_edit_location_success(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)

        #search location
        driver.find_element(By.XPATH, element.nameSearch).send_keys(data.name)
        time.sleep(1)
        driver.find_element(By.XPATH, element.citySearch).send_keys(data.city)
        time.sleep(1)
        driver.find_element(By.XPATH, element.countrySearch).send_keys("iii")
        time.sleep(1)
        driver.find_element(By.XPATH, element.countrySearch).send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.searchBtn).click()
        time.sleep(2)

        #edit location
        driver.find_element(By.XPATH, element.editBtn).click()
        time.sleep(1)
        cityEdit = driver.find_element(By.XPATH, element.cityEdit)
        cityEdit.send_keys(Keys.CONTROL + "a")
        cityEdit.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        cityEdit.send_keys(data.cityEdit)
        time.sleep(1)
        stateEdit = driver.find_element(By.XPATH, element.stateEdit)
        stateEdit.send_keys(Keys.CONTROL + "a")
        stateEdit.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        stateEdit.send_keys(data.stateEdit)
        time.sleep(1)
        driver.find_element(By.XPATH, element.saveEdit).click()
        time.sleep(5)

        #validasi
        response_url = driver.current_url
        self.assertEqual(url.addLocUrl, response_url)

    #OHRM41
    def test_w_cancel_edit_location(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)

        #search location
        driver.find_element(By.XPATH, element.nameSearch).send_keys(data.name)
        time.sleep(1)
        driver.find_element(By.XPATH, element.citySearch).send_keys(data.city)
        time.sleep(1)
        driver.find_element(By.XPATH, element.countrySearch).send_keys("iii")
        time.sleep(1)
        driver.find_element(By.XPATH, element.countrySearch).send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.searchBtn).click()
        time.sleep(2)

        #edit location
        driver.find_element(By.XPATH, element.editBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.cancelEdit).click()
        time.sleep(5)

        #validasi
        response_url = driver.current_url
        self.assertEqual(url.addLocUrl, response_url)

    #OHRM42 - Delete Location
    def test_x_delete_location_success(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)

        #search location
        driver.find_element(By.XPATH, element.nameSearch).send_keys(data.name)
        time.sleep(1)
        driver.find_element(By.XPATH, element.citySearch).send_keys(data.city)
        time.sleep(1)
        driver.find_element(By.XPATH, element.countrySearch).send_keys("iii")
        time.sleep(1)
        driver.find_element(By.XPATH, element.countrySearch).send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.searchBtn).click()
        time.sleep(2)

        #delete location
        driver.find_element(By.XPATH, element.deleteBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.confirmDelete).click()
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5').text
        self.assertIn(response_data, "Locations")

    #OHRM43
    def test_y_cancel_delete_location(self):
        driver = self.browser
        baseLogin.positive_login(driver)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, element.adminBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.selectLocations).click()
        time.sleep(1)

        #search location
        driver.find_element(By.XPATH, element.nameSearch).send_keys(data.name)
        time.sleep(1)
        driver.find_element(By.XPATH, element.citySearch).send_keys(data.city)
        time.sleep(1)
        driver.find_element(By.XPATH, element.countrySearch).send_keys("iii")
        time.sleep(1)
        driver.find_element(By.XPATH, element.countrySearch).send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element(By.XPATH, element.searchBtn).click()
        time.sleep(2)

        #delete location
        driver.find_element(By.XPATH, element.deleteBtn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, element.cancelDelete).click()
        time.sleep(5)

        #validasi
        response_url = driver.current_url
        self.assertEqual(url.addLocUrl, response_url)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()