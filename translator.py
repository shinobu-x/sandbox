import os
import sys
from wget import download
from googletrans import Translator
from tika import parser
def doit(file):
    url = 'https://arxiv.org/pdf'
    if not os.path.isfile(file):
        download(url + '/' + file)
    file_data = parser.from_file(file)
    text = file_data['content']
    print(text)
    target = ''
    for line in sys.stdin:
        text = line.rstrip()
        if text != 'done':
            print(text)
            target += text
        else:
            text.replace('\n',' ')
            translator = Translator()
            translater = Translator(service_urls=['translate.googleapis.com'])
            trans = translater.translate(text=target,src='en',dest='ja').text
            print(trans)
if __name__ == '__main__':
    file = '2108.00981.pdf'
    doit(file)
