import json
import urllib.request
from urllib.parse import urlencode

def request(text, source_lang, target_lang):
    arguments = urlencode({'client': 'gtx', 'ie': 'UTF-8', 'oe': 'UTF-8', 
        'q': text, 'sl': source_lang, 'tl': target_lang})
    url = f'https://translate.googleapis.com/translate_a/single?\
{arguments}&dt=bd&dt=ex&dt=ld&dt=md&dt=rw&dt=rm&dt=ss&dt=t&dt=at'
    data = urllib.request.urlopen(url).read()
    return json.loads(data)

