


'''This file use to write code for browser setup & close and also return driver object to use  for test'''

from selenium import webdriver
import pytest



'''Using fixture here to automate setup & teardown code for all test'''
@pytest.fixture(autouse=True)
def driver():
  '''Opening chrome browser'''
  driver  = webdriver.Chrome()
  driver.maximize_window()
    
  '''Here returning browser object to test code'''
  yield driver
    
  '''Here closing browser'''
  driver.quit()