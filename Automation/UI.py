
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# For using sleep function because selenium 
# works only when the all the elements of the 
# page is loaded. 
import time 
# webdriver path set 
browser = webdriver.Chrome("/Users/praveenbabu/Documents/python/Python/Automation/chromedriver") 
  
# To maximize the browser window 
browser.maximize_window() 
  
# zomato link set 
#browser.get('http://automationpractice.com') 
#time.sleep(30) 
#browser.find_element_by_xpath("//*[@id=\"header\"]/div[2]/div/div/nav/div[1]/a").click()
browser.get('http://automationpractice.com/index.php?controller=my-account')
time.sleep(30)
#inputElement = browser.find_element_by_id("create_account_error")
inputElement = browser.find_element(by=By.ID, value='email_create')
inputElement.send_keys('praveenpmin@gmail.com')
#webelement l =browser.find_element("//*[@id='create_account_error']")
#.value='praveenpmin@gmail.com'")
#browser.find_element("//*[@class='login']").click()
time.sleep(30)
browser.find_element(by=By.ID, value='SubmitCreate').click
time.sleep(50)
browser.find_element(by=By.ID, value='SubmitCreate').click
#browser.find_element(by.id, 'create_account_error')
time.sleep(50)
browser.quit()