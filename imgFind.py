from bs4 import BeautifulSoup
import requests
import os
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode
from rutermextract import TermExtractor
import os

def get_soup(url, header):
	data = urlencode(header).encode("utf-8")
	r = requests.get(url,data=data)
	return BeautifulSoup(r.content, from_encoding='utf-8',features=u'lxml')

def find_pict(descript):
	image_type = "img"
	descript=descript.split()
	#descript='+'.join(descript) яндекс
	#url="https://yandex.ru/images/search?from=tabbar&text="+descript яндекс
	descript='-'.join(descript)
	url="https://ru.depositphotos.com/stock-photos/"+descript+".html"
	header = {'User-Agent': 'Mozilla/5.0'}
	print(url)
	soup = get_soup(url,header)
	#print(soup)
	#image = soup.a.find_next("img", class_="serp-item__thumb")['src'] яндекс
	try:
		image = soup.a.find_next("img", class_="file-container__image")['src']
	except:
		image = ''
	#image='https:'+image яндекс
	#print(image)
	#raw_img = urlopen(image).read()
	#dir = r'.\images\\'
	#if not os.path.exists(dir): 
	#	os.mkdir(dir)
	#cntr = len([i for i in os.listdir(dir) if image_type in i]) + 1	сохранение картинки в виде файла
	#f = open(dir + image_type + "_"+ str(cntr)+".jpg", 'wb')
	#f.write(raw_img)
	#f.close()
	return image
	
# возвращает или ссылку на картинку, или ничего	
def get_pict(text):	
	term_extractor = TermExtractor()
	for term in term_extractor(text, nested=True):
		norm_term = term.normalized
		print(norm_term)
		result = find_pict(norm_term)
		if result:
			return result, norm_term
	return
		
#get_pict('Съешь ещё этих мягких французских булок да выпей же чаю.')