import os

from bs4 import BeautifulSoup
import re
#from odf import text, teletype

import sys, zipfile, io

re_word_split = "\\s"#"[^\\w\\d-]"
re_sentence_split = "(?<!www)[.?!](?!com)"

def readFile(fileName):
    file = open(fileName, 'r') #, encoding='ascii'
    xmls = file.read()
    return xmls

def getParagraphsFromODT(filename):
    # myFile  = zipfile.ZipFile(filename)
    # listOfFiles = myFile.infolist()
    texts = []
    # for s in listOfFiles:
    #     if s.orig_filename == 'content.xml':
    #         content = myFile.read(s.orig_filename).decode("utf-8")
    #         doc = BeautifulSoup(content, features=u"lxml")
    #         xmls = doc.findAll('text:p')
    xmls = readFile(filename)
    for xml in xmls.split('\n'):
        texts.append(xml)
    # print(xmls)
    return texts

def insertIntoSentence(sentence, word_place, value):
    word_split = re.split(re_word_split, sentence)
    word_split.insert(word_place, value)
    return " ".join(word_split)
def insertImage(text, sentence_numb, word_place, value):
    sentence_split = re.split(re_sentence_split, text)
    sentence = sentence_split[sentence_numb]
    sentence_split[sentence_numb] = insertIntoSentence(sentence, word_place, value)
    return ". ".join(sentence_split)
def writeUpdatedODT(fileName, images_buf):
    # os.system('copy ' + fileName + ' updated_' + fileName)
    file = os.path.basename(fileName)
    path = os.path.dirname(fileName)
    up_fileName = os.path.join(path, 'updated_' + file + '.html')
    try:
        os.remove(up_fileName)
    except:
        None

    html_file = open(up_fileName, 'w')
    # myFile = zipfile.ZipFile(fileName)
    # listOfFiles = myFile.infolist()
    texts = []
    # with zipfile.ZipFile(up_fileName, mode='a', compression=zipfile.ZIP_DEFLATED) as zf:
    # for s in listOfFiles:
    #     # zf.comment = myFile.comment
    #     if s.orig_filename == 'content.xml':
    #         content = myFile.read(s.orig_filename).decode("utf-8")
    #         doc = BeautifulSoup(content, features=u"xml")
    #         xmls = doc.findAll('text:p')
    #         print(doc.get('text:p'))
    #     else:
    #         content = myFile.read(s.filename)
    #         # zf.writestr(s, content)

    xmls = readFile(fileName)
    count_images = 0
    for x_indx, xml in enumerate(xmls.split('\n')):
        _str = xml
        print(x_indx)
        try:
            for i_indx, image in reversed(list(enumerate(images_buf[x_indx]))):
                print(_str)
                _str = insertImage(_str, image[0], image[1], 'Рис. ' + str(count_images + i_indx + 1) + ' ' + image[2] + ' <img src="' + image[3] + '">')
                print(_str)
            count_images += len(images_buf[x_indx])
        except IndexError as e:
            print(e, x_indx, file = sys.stderr)
            print(_str)
            print(image)
            print(images_buf)
        html_file.write(_str + '\n\r')
        # xml.string = _str

    html_file.close()
    # print(doc.find('text:p'))
    # with zipfile.ZipFile(up_fileName, mode='a', compression=zipfile.ZIP_DEFLATED) as zf:
    #     zf.writestr('content.xml', doc.encode('utf-8'))

# fileName = 'текст.odt'
# buf = [[[2,'test','test.img']],[],[],[],[]]
# writeUpdatedODT(fileName, buf)