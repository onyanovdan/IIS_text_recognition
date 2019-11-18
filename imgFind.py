from bs4 import BeautifulSoup
import requests
import os
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode
import os


def get_soup(url, header):
	data = urlencode(header).encode("utf-8")
	r = requests.get(url,data=data)
	return BeautifulSoup(r.content, from_encoding='utf-8',features=u'lxml')

def getPict(descript):
	image_type = "img"
	descript=descript.split()
	#descript='+'.join(descript)
	#url="https://yandex.ru/images/search?from=tabbar&text="+descript
	descript='-'.join(descript)
	url="https://ru.depositphotos.com/stock-photos/"+descript+".html"
	header = {'User-Agent': 'Mozilla/5.0'}
	print(url)
	soup = get_soup(url,header)
	#print(soup)
	#image = soup.a.find_next("img", class_="serp-item__thumb")['src'] яндекс
	image = soup.a.find_next("img", class_="file-container__image")['src']
	#image='https:'+image яндекс
	print(image)
	raw_img = urlopen(image).read()
	dir = r'.\images\\'
	if not os.path.exists(dir): 
		os.mkdir(dir)
	cntr = len([i for i in os.listdir(dir) if image_type in i]) + 1
	f = open(dir + image_type + "_"+ str(cntr)+".jpg", 'wb')
	f.write(raw_img)
	f.close()