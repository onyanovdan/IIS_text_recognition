from bs4 import BeautifulSoup
#from odf import text, teletype

import sys, zipfile, io

fileName = 'текст.odt'
content = ''
myFile  = zipfile.ZipFile(fileName)
listOfFiles = myFile.infolist()
for s in listOfFiles:
    # print(s.orig_filename)
    # content = myFile.read(s.orig_filename)
    # print(content)
    if s.orig_filename == 'content.xml':
        content = myFile.read(s.orig_filename).decode("utf-8")
        # text = io.TextIOWrapper(io.BytesIO(content.read()))
        doc = BeautifulSoup(content, features="html.parser")
        text = doc.findAll('text:p')
        print(text)