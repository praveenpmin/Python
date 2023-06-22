import requests
from bs4 import BeautifulSoup

urls = 'https://www.moneycontrol.com/india/stockpricequote/A'
grab = requests.get(urls)
soup = BeautifulSoup(grab.text, 'html.parser')

#display the results
#urls = []
#for link in soup.find_all('a'):
#    print(link.get('href'))

# opening a file in write mode
f = open('test2.txt', 'w')
# traverse paragraphs from soup
for link in soup.find_all('ab'):

    data = link.get('href')
    #print(data)
    #print(link.get('href'))
    f.write(str(data.encode()))
    f.write('\n'.encode())

f.close()

file1 = open('test2.txt', 'r')
print(file1.read())
file1.close()