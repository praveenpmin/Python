# Importing important library
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
  
# using chrome browser
driver = webdriver.Chrome(ChromeDriverManager().install())
  
# Target url
driver.get(
    "https://www.geeksforgeeks.org/competitive-programming-a-complete-guide/")
  
# Storing the page source in page variable
page = driver.page_source.encode('utf-8')
# print(page)
  
# open result.html
file_ = open('result.html', 'wb')
  
# Write the entire page content in result.html
file_.write(page)
  
# Closing the file
file_.close()
  
# Closing the driver
driver.close()