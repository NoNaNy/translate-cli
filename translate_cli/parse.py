'''parse module'''

from textwrap import dedent

def parse(data):
    '''parse data from `request()` into a dict'''
    result = {
        'text': '', 'text_pron': '', 'text_lang': '',
        'text_syno': [], 'text_defi': [], 'text_exam': [],
        'trans': '', 'trans_pron': '',
        'trans_all': [], 'trans_verbose': [],
        }

    codes = (
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

        '''\
        if len(data) > 11:
            for i in data[11]:
                word_type = i[0]
                type_synonyms = []
                for _i in i[1]:
                    type_synonyms.append(_i[0])
                result['text_syno'].append((word_type, type_synonyms))''',

        '''\
        if len(data) > 12:
            for j in data[12]:
                word_type = j[0]
                type_definitions = []
                for _j in j[1]:
                    type_definitions.append(_j[0])
                result['text_defi'].append((word_type, type_definitions))''',
        '''\
        if len(data) > 13:
            for k in data[13][0]:
                result['text_exam'].append(k[0])'''
        )

    for code in codes:
        try:
            exec(dedent(code))
        except (IndexError, TypeError):
            ...

    return result