from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
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
inputElement = browser.find_element(by=By.xpath, value='//a[@href="https://ui.freecrm.com/"]')
#inputElement.click()
#inputElement.send_keys('praveenpmin@gmail.com')
#browser.findElement(By.linkText("Login"));
#time.sleep(30) 
#browser.execute_script(("arguments[0].click();", loginBtn))
#JavascriptExecutor js = (JavascriptExecutor)driver;
#js.executeScript("arguments[0].click();", loginBtn);#
browser.quit()

#<a href="https://ui.freecrm.com/">Login</a>