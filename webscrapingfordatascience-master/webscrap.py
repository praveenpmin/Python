#!usr/bin/env python


import requests
from bs4 import BeautifulSoup

# url of the search page
url = "http://www.amazon.in/s/ref=nb_sb_ss_i_4_8?url=search-alias%3Daps&field-keywords=protein+bars&sprefix=protein+%2Caps%2C718&crid=1SW4WFJE8O22T&rh=i%3Aaps%2Ck%3Aprotein+bars"


r = requests.get(url)			# get the search url using requests
soup = BeautifulSoup(r.content, 'lxml')	# create a BeautifulSoup object 'soup' of the content

# Item Name
i_name = soup.find_all("h2",{"class": "a-size-medium s-inline  s-access-title  a-text-normal"})

#'find_all' method is used to find the  matching criteria as mentioned in parenthesis

# Item Price
i_price = soup.find_all("span",{"class": "a-size-base a-color-price a-text-bold"})


# Now print Item name and price
# 'zip' is used to traverse parallely to both name and price
for name,price  in zip(i_name,i_price):
	print "Item Name: " +name.string
	print "Item Price:" +price.text
	print '-'*70