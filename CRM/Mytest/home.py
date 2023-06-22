from selenium import webdriver 
import time
from selenium.webdriver.common.by import By 

browser = webdriver.Chrome("/Users/praveenbabu/Documents/python/Python/Automation/chromedriver") 
  
# To maximize the browser window 
browser.maximize_window()
#browser.execute_script(("arguments[0].click();", loginBtn))
browser.get('https://www.freecrm.com') 
inputElement = browser.find_element("xpath", '/html/body/div[2]/div/div[2]/ul/li[1]/a')
time.sleep(5)
inputElement.click()
time.sleep(5)
userName = browser.find_element("xpath", '/html/body/div[1]/div/div/form/div/div[1]/div/input')
userName.send_keys('praveenpmin@gmail.com')
passWord = browser.find_element("xpath", '/html/body/div[1]/div/div/form/div/div[2]/div/input')
passWord.send_keys('test1234')
submit_Button = browser.find_element("xpath", '/html/body/div[1]/div/div/form/div/div[3]')
submit_Button.click()
time.sleep(10)
#menu_Contacts = browser.find_element(By.CLASS_NAME, "item-text") /html/body/div[1]/div/div[1]/div[3]/a
menu_Contacts = browser.find_element("xpath", '/html/body/div[1]/div/div[1]/div[3]/a')
menu_Contacts.click()
create_Btn = browser.find_element("xpath", '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/a/button')
create_Btn.click()
time.sleep(5)
firstName = browser.find_element("xpath", '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/form/div[1]/div[1]/div/div/input')
firstName.send_keys('first')
lastName = browser.find_element("xpath", '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/form/div[1]/div[2]/div/div/input')
lastName.send_keys('last')
save_Btn = browser.find_element("xpath", '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/button[2]')
save_Btn.click()
contact_Validate = browser.find_element("xpath", '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]')
#contact_Validate = browser.find_element(By.CLASS_NAME, 'large user red icon').text   /html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]
#contact_Validate = browser.find_element("xpath", '//*[@id="dashboard-toolbar"]/div[1]/text()') /html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/i 
print(contact_Validate.text)
if contact_Validate == "first last":
    print("Existing user validation Passed")
else:
    print("Existing user validation Failed")
#browser.quit()