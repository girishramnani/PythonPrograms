import requests
import urllib
import sys
import json

def translate(text,lang1,lang2):
    base_url='http://ajax.googleapis.com/ajax/services/language/translate?'    
    langpair='%s|%s'%(lang1,lang2)
    params=urllib.parse.urlencode( (('v',1.0),
                       ('q',text.encode('utf-8')),
                       ('langpair',langpair),) )
    url=base_url+params
    content=requests.get(url).json()
    return content['responseData']['translatedText']

languages='de da nl zh-tw ko es pt el'.split()
text=(' '.join(sys.argv[1:]))

for lang in languages:
    result=translate(text,'en',lang)
    result=translate(result,lang,'en')
    print(result)
    print()