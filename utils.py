import easyocr

def ocr_text(img_path):
    '''Extracts text and counts words.'''
    reader = easyocr.Reader(['en'])
    result = reader.readtext(img_path)
    op = ""
    count = 0
    for (bbox, text, prob) in result:
        if prob:
            count += len(text.split(" "))
            op += "\n" + text
    return op, count
