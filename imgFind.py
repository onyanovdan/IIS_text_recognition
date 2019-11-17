from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode
import os


def get_soup(url,header):
  data = urlencode(header).encode("utf-8")
  req = Request(url)
  return BeautifulSoup(urlopen(req,data=data),features="lxml")

image_type = "img"
# you can change the query for the image  here  
query = "Terminator 3 Movie"
query= query.split()
query='+'.join(query)
url="https://yandex.ru/images/search?from=tabbar&text="+query

print(url)
header = {'User-Agent': 'Mozilla/5.0'} 
soup = get_soup(url,header)
print(soup)
images = [a['src'] for a in soup.find_all("img", class_="serp-item__thumb")]

for img in images:
  img='https:'+img
  print(img)
  raw_img = urlopen(img).read()
  #add the directory for your image here 
  dir = r'C:\Users\Vasiliy\python\images\\'
  cntr = len([i for i in os.listdir(dir) if image_type in i]) + 1
  print(cntr)
  f = open(dir + image_type + "_"+ str(cntr)+".jpg", 'wb')
  f.write(raw_img)
  f.close()