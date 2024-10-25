import requests
from bs4 import BeautifulSoup

req=requests.get("https://www.trivago.in/")

soup=BeautifulSoup(req.content,"html.parser")

print(soup.prettify())

print("hello")
