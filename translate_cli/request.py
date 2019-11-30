'''request module'''

import requests
import time
import json
from translate_cli.lang_codes import LANG_MAP
from urllib.request import urlopen
from urllib.parse import urlencode

def transformLanguage(lang, engine):
    return LANG_MAP[lang][engine] if engine in LANG_MAP[lang] else lang

def requestGoogleTranslate(text, src_lang, dst_lang):
    '''make a request to google public translate api'''
    arguments = urlencode({
        'client': 'gtx', 'ie': 'UTF-8', 'oe': 'UTF-8',
        'q': text, 'sl': src_lang, 'tl': dst_lang, 'hl': src_lang})
    url = f'https://translate.googleapis.com/translate_a/single?{arguments}&dt=bd&dt=ex&dt=ld&dt=md&dt=rw&dt=rm&dt=ss&dt=t&dt=at'
    data = urlopen(url).read()
    return json.loads(data)

def requestDeepL(text, src_lang, dst_lang):
    bodyRequestJson = f'''{{
    "jsonrpc": "2.0","method": "LMT_handle_jobs",
    "params": {{"jobs": [{{
                "kind": "default",
                "raw_en_sentence": "{text}",
                "raw_en_context_before": [],
                "raw_en_context_after": [],
                "quality": "normal"}}],
        "lang": {{
            "source_lang": "{src_lang}",
            "target_lang": "{dst_lang}"
        }},
        "priority": -1,
        "timestamp": {str(int(time.time()))}000
    }},
    "id": 10330004}}'''
    url = "https://www2.deepl.com/jsonrpc"
    headers = {'Content-Type': 'application/json'}
    data = requests.post(url, data=bodyRequestJson, headers=headers)
    return json.loads(data.text)

def requestBing(text, src_lang, dst_lang):    
    arguments = urlencode({'fromLang':src_lang, 'to':dst_lang, 'text':text})
    url = f'https://www.bing.com/ttranslatev3?{arguments}'
    data = requests.post(url)
    translation = json.loads(data.text)

    transText=translation[0]['translations'][0]['text'].lower()

    if len(transText.split()) > 1:
        return translation

    fromLang= translation[0]['detectedLanguage']['language']
    toLang= translation[0]['translations'][0]['to']

    arguments = urlencode({'from':fromLang, 'to':toLang, 'text':text})
    url = f'https://www.bing.com/tlookupv3?{arguments}'
    data = requests.post(url)
    other = json.loads(data.text)

    arguments = urlencode({'from':fromLang, 'to':toLang, 'text':text, 'translation':transText})
    url = f'https://www.bing.com/texamplev3?{arguments}'
    data = requests.post(url)
    examples = json.loads(data.text)

    return translation + other + examples

def requestEngine(text, src_lang, dst_lang, engine):
    if engine == 'g':
        #Use Google
        src_lang = transformLanguage(src_lang, 'google')
        dst_lang = transformLanguage(dst_lang, 'google')
        return requestGoogleTranslate(text, src_lang, dst_lang)
        
    if engine == 'b':
        #Use Bing
        src_lang = transformLanguage(src_lang, 'bing')
        dst_lang = transformLanguage(dst_lang, 'bing')
        return requestBing(text, src_lang, dst_lang)
    if engine == 'd':
        #Use DeepL
        # NOTE: Don't need transform anything 
        return requestDeepL(text, src_lang, dst_lang)