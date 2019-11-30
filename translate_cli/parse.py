'''parse module'''
import os
from textwrap import dedent

def buildStructure():
    return {
        'text': '', 'text_pron': '', 'text_lang': '',
        'text_syno': [], 'text_defi': [], 'text_exam': [],
        'trans': '', 'trans_pron': '',
        'trans_all': [], 'trans_verbose': [],
        }

def getCodesGoogleTranslate():   
    return (
        "result['trans'] = data[0][0][0]",
        "result['text'] = data[0][0][1]",
        "result['text_pron'] = data[0][1][3] if len(data[0])>1 else ''",
        "result['trans_pron'] = data[0][1][2] if len(data[0])>1 else ''",
        "result['text_lang'] = data[2]",

        '''
        if data[1]:
            for g in data[1]:
                word_type = g[0]
                type_synonyms = []        
                for _g in g[2]:
                    reverse_words = []
                    for __g in _g[1]:
                        reverse_words.append(__g)
                    type_synonyms.append((_g[0],reverse_words))
                result['trans_verbose'].append((word_type, type_synonyms))''',

        '''
        for h in data[5][0][2]:
            result['trans_all'].append(h[0])''',

        '''
        if len(data) > 11:
            for i in data[11]:
                word_type = i[0]
                type_synonyms = []
                for _i in i[1]:
                    type_synonyms.append(_i[0])
                result['text_syno'].append((word_type, type_synonyms))''',

        '''
        if len(data) > 12:
            for j in data[12]:
                word_type = j[0]
                type_definitions = []
                for _j in j[1]:
                    type_definitions.append(_j[0])
                result['text_defi'].append((word_type, type_definitions))''',
        '''
        if len(data) > 13:
            for k in data[13][0]:
                result['text_exam'].append(k[0])'''
        )

def getCodesDeepL(data):
    return [] if 'result' not in data else (
        "result['trans'] = data['result']['translations'][0]['beams'][0]['postprocessed_sentence']",
        "result['text'] = text",
        "result['text_pron'] = ''",
        "result['trans_pron'] = ''",
        "result['text_lang'] = data['result']['source_lang'].lower()",
        '''
        for h in data['result']['translations'][0]['beams']:
            result['trans_all'].append(h['postprocessed_sentence'])''')

def getCodesBing(data):    
    check = any([x for x in data if 'translations' in x])
    return [] if not check else (
        "result['trans'] = data[0]['translations'][0]['text']",
        "result['text'] = text",
        "result['text_pron'] = ''",
        "result['trans_pron'] = ''",
        "result['text_lang'] = data[0]['detectedLanguage']['language'].lower()",
        '''
        for h in data[1]['translations']:
            result['trans_all'].append(h['displayTarget'])''',
        '''
        for h in data[1]['translations']:
            word_type = h['posTag']
            type_synonyms = []        
            reverse_words = []
            for g in h['backTranslations']:
                reverse_words.append(g['displayText'])
            type_synonyms.append((h['displayTarget'],reverse_words))
            
            if result['trans_verbose']:
                for wtSynItems in result['trans_verbose']:
                    if wtSynItems[0] == word_type:
                        index = result['trans_verbose'].index(wtSynItems)
                        result['trans_verbose'][index][1].extend(type_synonyms)
            else:
                result['trans_verbose'].append((word_type, type_synonyms))''',
        '''
        for k in data[2]['examples']:
            result['text_exam'].append(f"{k['sourcePrefix']}<b>{k['sourceTerm']}</b>{k['sourceSuffix']}{os.linesep}\t{k['targetPrefix']}<b>{k['targetTerm']}</b>{k['targetSuffix']}")''')

def parseResponse(data, text, engine):
    result = buildStructure()
    if engine == 'g':
        codes = getCodesGoogleTranslate()
        #Use Google
    if engine == 'b':
        #Use Bing
        codes = getCodesBing(data)

    if engine == 'd':
        #Use DeepL
        codes = getCodesDeepL(data)

    # Execute all commands for parse 
    for code in codes:
        try:
            exec(dedent(code))
        except (IndexError, TypeError):
            ...

    return result        
