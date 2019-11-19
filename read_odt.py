from bs4 import BeautifulSoup
#from odf import text, teletype

import sys, zipfile, io

def getParagraphsFromODT(filename):
    myFile  = zipfile.ZipFile(filename)
    listOfFiles = myFile.infolist()
    texts = []
    for s in listOfFiles:
        if s.orig_filename == 'content.xml':
            content = myFile.read(s.orig_filename).decode("utf-8")
            doc = BeautifulSoup(content, features=u"lxml")
            xmls = doc.findAll('text:p')
    for xml in xmls:
        texts.append(xml.text)
    return texts