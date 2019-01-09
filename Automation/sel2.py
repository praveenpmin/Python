from selenium import webdriver 
# For using sleep function because selenium 
# works only when the all the elements of the 
# page is loaded. 
import time 
# webdriver path set 
browser = webdriver.Chrome("C:/Users/ITPeople/code/Python/Automation/chromedriver") 
  
# To maximize the browser window 
browser.maximize_window() 
  
# zomato link set 
browser.get('https://www.zomato.com/ncr') 
time.sleep(30) 
browser.find_element_by_xpath("//*[@id='signin-link']").click()
time.sleep(30)
# browser.find_element_by_xpath("//*[@id='signup-email']/span").click()
# time.sleep(30) 
# Enter your user name and password here. 
username = "test"
password = "test"
  
  
# signin element clicked 
# browser.find_element_by_xpath("//a[@id ='signin-link']").click() 
time.sleep(20) 
  
# Login clicked 
# browser.find_element_by_xpath("//a[@id ='login-email']").click() 
  
# username send 

browser.find_element_by_xpath("//*[@id='login-email']").click()
time.sleep(20)
a = browser.find_element_by_xpath("//input[@id ='ld-email']") 
a.send_keys(username) 
  
# password send 
b = browser.find_element_by_xpath("//input[@id ='ld-password']") 
b.send_keys(password) 
  
# submit button clicked 
browser.find_element_by_xpath("//input[@id ='ld-submit-global']").click() 
  
print('Login Successful') 
browser.close()