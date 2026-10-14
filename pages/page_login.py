


import time


from utitlities.config_file_reader import BASE_URL, BROWSER

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver



# Here will define all locators that is used for login page
My_ac = "//span[normalize-space()='My Account']"
login = "//a[normalize-space()='Login']"
user_input = "//input[@id='input-email']"
pwd_input = "//input[@id='input-password']"




#This is test for login
def open_login(driver:WebDriver):
  driver.get(BASE_URL)
  time.sleep(5)
  driver.find_element(By.XPATH,My_ac).click()
  time.sleep(10)
  driver.find_element(By.XPATH,login).click()
  time.sleep(5)
  driver.find_element(By.XPATH,user_input).send_keys("AMIT KUMAR")
  time.sleep(5)  
  driver.find_element(By.XPATH,pwd_input).send_keys(12345)
  
  
  


