# importing the modules
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
  
# using webdriver for chrome browser
driver = webdriver.Chrome(ChromeDriverManager().install())
  
# using target url
driver.get(
    "https://www.geeksforgeeks.org/competitive-programming-a-complete-guide/")
  
# printing the content of entire page
#print(driver.find_element_by_xpath("/html/body").text)

# Get all the div elements
div_elements = driver.find_elements(By.TAG_NAME, "div")

# Iterate over the div elements
for index, div in enumerate(div_elements):
    print(f'Div Element {index+1}\n{div.text}\n') 
# closing the driver
driver.close()