from bs4 import BeautifulSoup
import urllib3
import requests

http = urllib3.PoolManager()

url = 'http://www.thefamouspeople.com/singers.php'
response = http.request('GET', url)
# print (response.data)
# soup = BeautifulSoup(response.data)
soup = BeautifulSoup(response.data.decode('utf-8'))


#response = requests.get(url)

# soup = BeautifulSoup(response.content, "html.parser")
print(soup)