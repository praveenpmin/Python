import requests
from beautifulsoap4 import beautifulsoap4

url = 'http://www.alibaba.com/catalogs/products/CID100003006'
response = requests.get(url)
html = response.content
soup = BeautifulSoap(html)
print (html)
# print (soup.prettify())