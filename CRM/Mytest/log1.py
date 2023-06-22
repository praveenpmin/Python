from selenium import webdriver 
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium import WebElement 
# For using sleep function because selenium 
# works only when the all the elements of the 
# page is loaded. 
import time 
#import org.openqa.selenium.JavascriptExecutor;
# webdriver path set 
browser = webdriver.Chrome("/Users/praveenbabu/Documents/python/Python/Automation/chromedriver") 
  
# To maximize the browser window 
browser.maximize_window()
#browser.execute_script(("arguments[0].click();", loginBtn))
browser.get('https://www.freecrm.com') 
#inputElement = browser.find_element(by=By.href, value='Login')
#inputElement = browser.find_element(by=By.xpath, value='//a[@href="https://ui.freecrm.com/"]')
#inputElement = browser.find_element_by_xpath('//a[@href="freecrm.com"]')
inputElement = browser.find_element("xpath", '/html/body/div[2]/div/div[2]/ul/li[1]/a')
time.sleep(5)
inputElement.click()
time.sleep(5)
signUp = browser.find_element("xpath", '//*[@id="ui"]/div/div/div[3]/a')
time.sleep(5)
signUp.click()
time.sleep(5)
signUp_email = browser.find_element("xpath", '//*[@id="email"]')
signUp_email.send_keys('praveenpmin@gmail.com')
signUp_phone = browser.find_element("xpath", '//*[@id="phone_number"]')
signUp_phone.send_keys('9980930299')
time.sleep(15)
signUp_accept = browser.find_element("xpath", '//*[@id="terms"]')
signUp_accept.click()
#signUp_captcha = browser.find_element("xpath", '//*[@id="recaptcha-anchor"]')  
#signUp_captcha = browser.find_element("xpath", '/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]') 
#signUp_captcha.click()
signUp_button = browser.find_element("xpath", '/html/body/div[1]/div/div[2]/div[2]/form/div[5]/button')
signUp_button.click()
time.sleep(5)
#signUp_already_reg = browser.find_element("xpath", '/html/body/div[1]/div/div[2]/div[2]/ul/li')
signUp_already_reg = browser.find_element(By.CLASS_NAME, "list").text
print(signUp_already_reg)
#print(signUp_already_reg.getText())
if signUp_already_reg == "[[Email is already registered]]":
    print("Existing user validation Passed")
else:
    print("Existing user validation Failed")
#inputElement.send_keys('praveenpmin@gmail.com')
#browser.findElement(By.linkText("Login"));
#time.sleep(30) 
#browser.execute_script(("arguments[0].click();", loginBtn))
#JavascriptExecutor js = (JavascriptExecutor)driver;
#js.executeScript("arguments[0].click();", loginBtn);#
browser.quit()

#<a href="https://ui.freecrm.com/">Login</a>