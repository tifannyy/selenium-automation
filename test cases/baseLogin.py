from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locator import element
from locator import url
from inputData import data
import time

def positive_login(driver): #OHRM01
    driver.get(url.baseUrl)
    time.sleep(10)
    driver.maximize_window()
    driver.find_element(By.NAME, element.name).send_keys(data.username)
    time.sleep(1)
    driver.find_element(By.NAME, element.password).send_keys(data.password)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, element.loginBtn).click()
    time.sleep(3)

def negative_login_invalid_username(driver): #OHRM02
    driver.get(url.baseUrl)
    time.sleep(10)
    driver.maximize_window()
    driver.find_element(By.NAME, element.name).send_keys(data.invalidUsername)
    time.sleep(1)
    driver.find_element(By.NAME, element.password).send_keys(data.password)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, element.loginBtn).click()
    time.sleep(3)

def negative_login_invalid_password(driver): #OHRM03
    driver.get(url.baseUrl)
    time.sleep(10)
    driver.maximize_window()
    driver.find_element(By.NAME, element.name).send_keys(data.username)
    time.sleep(1)
    driver.find_element(By.NAME, element.password).send_keys(data.invalidPassword)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, element.loginBtn).click()
    time.sleep(3)

def negative_login_empty_username(driver): #OHRM04
    driver.get(url.baseUrl)
    time.sleep(10)
    driver.maximize_window()
    driver.find_element(By.NAME, element.name).send_keys("")
    time.sleep(1)
    driver.find_element(By.NAME, element.password).send_keys(data.password)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, element.loginBtn).click()
    time.sleep(3)

def negative_login_empty_password(driver): #OHRM05
    driver.get(url.baseUrl)
    time.sleep(10)
    driver.maximize_window()
    driver.find_element(By.NAME, element.name).send_keys(data.username)
    time.sleep(1)
    driver.find_element(By.NAME, element.password).send_keys("")
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, element.loginBtn).click()
    time.sleep(3)

def negative_login_blank_all(driver): #OHRM06
    driver.get(url.baseUrl)
    time.sleep(10)
    driver.maximize_window()
    driver.find_element(By.NAME, element.name).send_keys("")
    time.sleep(1)
    driver.find_element(By.NAME, element.password).send_keys("")
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, element.loginBtn).click()
    time.sleep(3)

def negative_login_upcase_username(driver): #OHRM07
    driver.get(url.baseUrl) 
    time.sleep(10)
    driver.maximize_window()
    driver.find_element(By.NAME, element.name).send_keys(data.upcaseUsername)
    time.sleep(1)
    driver.find_element(By.NAME, element.password).send_keys(data.password)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, element.loginBtn).click() 
    time.sleep(3)