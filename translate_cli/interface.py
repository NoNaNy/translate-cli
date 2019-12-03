#!/usr/bin/env python3

import sys
import argparse
import os.path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))
from translate_cli import translate
from translate_cli.format import BOLD, ITALIC, UNDERLINE, GRAY
from translate_cli.lang_codes import LANG_MAP
from translate_cli import __version__

def list_codes():
    for index, i in enumerate(LANG_MAP.items()):
        name = i[1]["name"]+" "#+"[ "
        name += "\u25B2 " if i[1]["engine"] >= 4 else ""
        name += "\u25A0 " if i[1]["engine"] in [6,7,2,3] else ""
        name += "\u25CF " if i[1]["engine"] in [1,3,5,7] else ""
        # name += "]"

        #TODO: Insert additional languages from bing [yue, fil, mww, tlh, yua, otq]
        code = UNDERLINE.format(BOLD.format(i[0]))
        if index % 2 == 0:
            print(f'{name:25}-->  {code:21}', end=f'{"":2}\u2502{"":2}')
        else:
            print(f'{name:25}-->  {code:21}')
    print("\n")
    print(f'\u25B2: Google translate | \u25A0: DeepL translate | \u25CF: Bing translate')

def validLanguageCode(langCode, engine):
    if not langCode:
        return False
    engineValue = langCode.get("engine")
    if engineValue == 7:
        return True

    if engine == 'g' and engineValue >= 5:
        return True
    if engine == 'd' and engineValue in [6,7,2,3]:
        return True
    if engine == 'b' and engineValue in [5,3,1]:
        return True
    
    return False

def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        prog='trans',
        description='A simple cli tool to translate',
        usage='trans [OPTIONS] [SOURCES]:[TARGETS] [TEXT]...',
        epilog="""examples:
    trans awesome :fr
        translate 'awesome' to French
    trans python -d
        lookup 'python' using dictionary mode""",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        '-e', '--engine',
        action='store',
        default='g',
        choices=['g','b','d'],
        help="""engine used for translate
    g: use google translator (default)
    b: use bing translator
    d: use deepl translator"""
    )
    parser.add_argument(
        '-l', '--list',
        action='store_true',
        help='list supported language codes'
    )
    parser.add_argument('-v', '--version', action='version', version='%(prog)s '+f'{__version__}')
    parser.add_argument(
        '-x', '--examples',
        action='store_true',
        default=False,
        help='show examples about the translation'
    )
    parser.add_argument(
        '-a', '--all',
        action='store_true',
        default=False,
        help='show all about the translation'
    )
    parser.add_argument(
        '-d', '--definition',
        action='store_true',
        default=False,
        help='show definition (if exist)'
    )
    parser.add_argument(
        '-r', '--reverse',
        action='store_true',
        default=False,
        help='revese translations from dictionary (if exist)'
    )
    parser.set_defaults(
        src_lang='auto',
        dst_lang='es'
    )
    args, texts = parser.parse_known_args(argv)

    # NOTE: DELETE this line, is only for debug
    del texts[0]

    if args.list:
        list_codes()
        sys.exit(0)
    args.src_lang = parser._defaults["src_lang"]
    args.dst_lang = parser._defaults["dst_lang"]
    for text in texts[:]:
        if ':' in text:
            languages = text.split(':')
            args.src_lang = languages[0] if languages[0] else args.src_lang
            args.dst_lang = languages[1] if languages[1] else args.dst_lang
            texts.remove(text)
    if not texts or (len(texts)==1 and not texts[0].strip()):
        print(f'{__package__} {__version__}')
        print()
        parser.print_help()        
        sys.exit(0)
    args.text = ' '.join(texts)
    src_val=LANG_MAP.get(args.src_lang)

    if not validLanguageCode(LANG_MAP.get(args.src_lang), args.engine) or not validLanguageCode(LANG_MAP.get(args.dst_lang), args.engine):
        raise ValueError('Invalid language code.')
    return args

def definition_print(translation):
    print()
    text = translation['text']

    if not translation['text_defi']:
        print(f'=> {UNDERLINE.format(text)} don''t have definition <=')
        return

    print(f'=> Definitions of {UNDERLINE.format(text)}')

    for i in translation['text_defi']:
        print(i[0])
        for _i in i[1]:
            print(f'{" ":4}{_i}\n')

    if translation['text_syno']:
        print(f'=> Synonyms of {UNDERLINE.format(text)}')
    for j in translation['text_syno']:
        print(f'{" ":4}{j[0]}')
        for _j in j[1]:
            print(f'{" ":8}- {BOLD.format(", ".join(_j))}')

def examples_print(translation):
    print()
    text = translation['text']
    if translation['text_exam']:
        print(f'=> Examples of {UNDERLINE.format(text)}')
    for k in translation['text_exam']:
        k = k.replace('<b>', '\033[1m\033[4m')
        k = k.replace('</b>', '\033[0m')
        print(f'{" ":4}- {k}\n')
    print()

def trans_print(translation, engine):
    print()
    text = translation['text']

    text_lang = LANG_MAP[translation['text_lang'][:2]]['name'] \
        if LANG_MAP.get(translation['text_lang'][:2]) \
        else translation['text_lang']

    text_pron = translation['text_pron']\
        if translation['text_pron'] and \
        isinstance(translation['text_pron'], str) else None

    trans = translation['trans']

    trans_pron = translation['trans_pron']\
        if translation['trans_pron'] and \
        isinstance(translation['trans_pron'], str) else None

    if engine == 'g':
        print(f'{UNDERLINE.format(GRAY.format("Google Translate"))}')
    if engine == 'd':
        print(f'{UNDERLINE.format(GRAY.format("DeepL Translator"))}')
    if engine == 'b':
        print(f'{UNDERLINE.format(GRAY.format("Bing Translator"))}')

    print(text)
    if text_pron:
        print(f'/{ITALIC.format(text_pron)}/')
    print()
    print(f'{BOLD.format(trans)}')
    if trans_pron:
        print(f'/{ITALIC.format(trans_pron)}/')
    print()

def trans_alternate(translation):
    print()
    text = translation['text']

    text_lang = LANG_MAP[translation['text_lang'][:2]]['name'] \
        if LANG_MAP.get(translation['text_lang'][:2]) \
        else translation['text_lang']

    trans_lang = LANG_MAP[translation['trans_lang']]['name']
    trans_all = ', '.join(translation['trans_all']) if len(
        text) <= 20 else f'\n{"":3}'.join(translation['trans_all'])

    print(f'=> Other alternatives of {UNDERLINE.format(text)}')
    print(f'[ {UNDERLINE.format(text_lang)} -> {BOLD.format(trans_lang)} ]')
    print()
    print(f'{UNDERLINE.format(text)}')
    print(f'   {trans_all}')
    print()

def trans_reverse(translation):
    if not translation['trans_verbose']:
        return
    print()    
    text = translation['text']
    print(f'=> Other translations of {UNDERLINE.format(text)}')
    print()
    for i in translation['trans_verbose']:
        print(i[0])
        for _i in i[1]:
            print(f'{"":4}{BOLD.format(_i[0])}\n{"":7}{", ".join(_i[1])}\n')

# def main(argv=None):
def main(argv=sys.argv):
    args = parse_args(argv)
    translation = translate(args.text, args.src_lang, args.dst_lang, args.engine)
    translation['trans_lang'] = args.dst_lang
    trans_print(translation, args.engine)
    trans_alternate(translation)
    if args.reverse or args.all:
        trans_reverse(translation)
    if args.definition or args.all:
        definition_print(translation)
    if args.examples or args.definition or args.all:
        examples_print(translation)
    return 0

if __name__ == '__main__':
    sys.exit(main())
