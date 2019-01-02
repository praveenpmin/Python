import urllib3

# page = urlopen('http://www.example.com').read()
webp=urllib3.connection_from_url("google.com").urlopen
# webp=urllib3.urlopen("google.com").read()
webp.__get__("Gmail")
# webp.find("Gmail")