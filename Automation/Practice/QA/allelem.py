from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/Users/praveenbabu/Documents/python/Python/Automation/chromedriver")
#browser = webdriver.Chrome("/Users/praveenbabu/Documents/python/Python/Automation/chromedriver") 
driver.get('http://www.google.com/')
ids = driver.find_elements(By.XPATH, '//*[@id]')
# to get names use '//*[@name]'

for ii in ids:
    print('Tag: ' + ii.tag_name)
    print('ID: ' + ii.get_attribute('id'))     # element id as string
    print('Name: ' + ii.get_attribute('name')) # element name as string
driver.quit