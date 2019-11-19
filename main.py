import read_odt as R
import pymorphy2
import imgFind as I

norm_word_order = 0 #может сломаться, если индекс выйдет за диапазон
fileName = 'текст.odt'
triggered_words = ['проиллюстрировать'
                   ,'показать'
                   ,'пример'
                   ,'увидеть'
                   ,'рисунок'
                    ]
key_words_count = 4
right_key_words_first = True

def splitToString(word_arr):
    str = " "
    return str.join(word_arr)
def getTwoSubSplitsStr(paragr_split, indx):
    word_arrs = []
    right = splitToString(paragr_split[indx+1:indx+1+key_words_count])
    word_arrs.append(right)
    min_indx = indx-key_words_count
    min_indx = 0 if min_indx < 0 else min_indx
    left = splitToString(paragr_split[min_indx:indx])
    if right_key_words_first:
        word_arrs.append(left)
    else:
        word_arrs.insert(0,left)
    return word_arrs


paragraphs = R.getParagraphsFromODT(fileName)
morph = pymorphy2.MorphAnalyzer()
result_buf = []
for p_indx, paragr in enumerate(paragraphs):
    images = []
    paragr_split = paragr.split()
    for w_indx, word in enumerate(paragr.split()):
        norm_word = morph.parse(word)[norm_word_order].normal_form
        # print(norm_word)
        if norm_word in triggered_words:
            # print('found - ' + norm_word)
            _image = []
            key_words_arr = getTwoSubSplitsStr(paragr_split, w_indx)
            print(key_words_arr)
            img = None
            first = True
            if key_words_arr[0] != '':
              img, term = I.get_pict(key_words_arr[0])
            if img == None and key_words_arr[1] != '':
                img, term = I.get_pict(key_words_arr[1])
                first = False
            print(img, term)
            if img:
                to_insert = w_indx + 1 if not first else w_indx + key_words_count + 1
                _image.append(to_insert)
                _image.append(term)
                _image.append(img)
                images.append(_image)
    result_buf.append(images)
R.writeUpdatedODT(fileName, result_buf)