'''a language code-to-name map'''
'''
Engine value 
google,deepl,bing
1,1,1 = 7
1,1,0 = 6
1,0,1 = 5
1,0,0 = 4
0,1,1 = 3
0,1,0 = 2
0,0,1 = 1
'''

from json import loads

DATA = \
'''
{
	"ab": {
		"engine": 4,
		"name": "Abkhaz",
		"nativeName": "аҧсуа"
	},
	"af": {
		"engine": 5,
		"name": "Afrikaans",
		"nativeName": "Afrikaans"
	},
	"am": {
		"engine": 4,
		"name": "Amharic",
		"nativeName": "አማርኛ"
	},
	"ar": {
		"engine": 5,
		"name": "Arabic",
		"nativeName": "العربية"
	},
	"az": {
		"engine": 4,
		"name": "Azerbaijani",
		"nativeName": "azərbaycan dili"
	},
	"be": {
		"engine": 4,
		"name": "Belarusian",
		"nativeName": "Беларуская"
	},
	"bg": {
		"engine": 5,
		"name": "Bulgarian",
		"nativeName": "български език"
	},
	"bn": {
		"bing": "bn-BD",
		"engine": 5,
		"name": "Bengali",
		"nativeName": "বাংলা"
	},
	"bs": {
		"bing": "bs-Latn",
		"engine": 1,
		"name": "Bosnian",
		"nativeName": "bosanski"
	},
	"ca": {
		"engine": 5,
		"name": "Catalan",
		"nativeName": "Català"
	},
	"co": {
		"engine": 4,
		"name": "Corsican",
		"nativeName": "corsu"
	},
	"cs": {
		"engine": 5,
		"name": "Czech",
		"nativeName": "česky"
	},
	"cy": {
		"engine": 5,
		"name": "Welsh",
		"nativeName": "Cymraeg"
	},
	"da": {
		"engine": 5,
		"name": "Danish",
		"nativeName": "dansk"
	},
	"de": {
		"engine": 7,
		"name": "German",
		"nativeName": "Deutsch"
	},
	"el": {
		"engine": 5,
		"name": "Greek (modern)",
		"nativeName": "Ελληνικά"
	},
	"en": {
		"engine": 7,
		"name": "English",
		"nativeName": "English"
	},
	"eo": {
		"engine": 4,
		"name": "Esperanto",
		"nativeName": "Esperanto"
	},
	"es": {
		"engine": 7,
		"name": "Spanish",
		"nativeName": "español"
	},
	"et": {
		"engine": 5,
		"name": "Estonian",
		"nativeName": "eesti"
	},
	"eu": {
		"engine": 4,
		"name": "Basque",
		"nativeName": "euskara"
	},
	"fa": {
		"engine": 5,
		"name": "Persian",
		"nativeName": "فارسی"
	},
	"fi": {
		"engine": 5,
		"name": "Finnish",
		"nativeName": "suomi"
	},
	"fj": {
		"engine": 1,
		"name": "Fiji",
		"nativeName": "vaka-Viti"
	},
	"fr": {
		"engine": 7,
		"name": "French",
		"nativeName": "franç"
	},
	"fy": {
		"engine": 4,
		"name": "Western Frisian",
		"nativeName": "Frysk"
	},
	"ga": {
		"engine": 4,
		"name": "Irish",
		"nativeName": "Gaeilge"
	},
	"gd": {
		"engine": 4,
		"name": "Scottish Gaelic",
		"nativeName": "Gàidhlig"
	},
	"gl": {
		"engine": 4,
		"name": "Galician",
		"nativeName": "Galego"
	},
	"gu": {
		"engine": 4,
		"name": "Gujarati",
		"nativeName": "ગુજરાતી"
	},
	"ha": {
		"engine": 4,
		"name": "Hausa",
		"nativeName": "Hausa, هَوُسَ"
	},
	"he": {
		"engine": 5,
		"name": "Hebrew (modern)",
		"nativeName": "עברית"
	},
	"hi": {
		"engine": 5,
		"name": "Hindi",
		"nativeName": "हिन्दी, हिंदी"
	},
	"hr": {
		"engine": 5,
		"name": "Croatian",
		"nativeName": "hrvatski"
	},
	"ht": {
		"engine": 5,
		"name": "Haitian Creole",
		"nativeName": "Kreyòl ayisyen"
	},
	"hu": {
		"engine": 5,
		"name": "Hungarian",
		"nativeName": "Magyar"
	},
	"hy": {
		"engine": 4,
		"name": "Armenian",
		"nativeName": "Հայերեն"
	},
	"id": {
		"engine": 5,
		"name": "Indonesian",
		"nativeName": "Bahasa Indonesia"
	},
	"ig": {
		"engine": 4,
		"name": "Igbo",
		"nativeName": "Asụsụ Igbo"
	},
	"is": {
		"engine": 5,
		"name": "Icelandic",
		"nativeName": "Íslenska"
	},
	"it": {
		"engine": 7,
		"name": "Italian",
		"nativeName": "Italiano"
	},
	"ja": {
		"engine": 5,
		"name": "Japanese",
		"nativeName": "日本語"
	},
	"jv": {
		"engine": 4,
		"name": "Javanese",
		"nativeName": "basa Jawa"
	},
	"ka": {
		"engine": 4,
		"name": "Georgian",
		"nativeName": "ქართული"
	},
	"kk": {
		"engine": 4,
		"name": "Kazakh",
		"nativeName": "Қазақ тілі"
	},
	"km": {
		"engine": 4,
		"name": "Khmer",
		"nativeName": "ភាសាខ្មែរ"
	},
	"kn": {
		"engine": 4,
		"name": "Kannada",
		"nativeName": "ಕನ್ನಡ"
	},
	"ko": {
		"engine": 5,
		"name": "Korean",
		"nativeName": "韓國語 (朝鮮語)"
	},
	"ku": {
		"engine": 4,
		"name": "Kurdish",
		"nativeName": "Kurdî, كوردی‎"
	},
	"ky": {
		"engine": 4,
		"name": "Kyrgyz",
		"nativeName": "кыргыз тили"
	},
	"la": {
		"engine": 4,
		"name": "Latin",
		"nativeName": "latine"
	},
	"lb": {
		"engine": 4,
		"name": "Letzeburgesch",
		"nativeName": "Lëtzebuergesch"
	},
	"lo": {
		"engine": 4,
		"name": "Lao",
		"nativeName": "ພາສາລາວ"
	},
	"lt": {
		"engine": 5,
		"name": "Lithuanian",
		"nativeName": "lietuvių kalba"
	},
	"lv": {
		"engine": 5,
		"name": "Latvian",
		"nativeName": "latviešu valoda"
	},
	"mg": {
		"engine": 5,
		"name": "Malagasy",
		"nativeName": "Malagasy fiteny"
	},
	"mi": {
		"engine": 4,
		"name": "Māori",
		"nativeName": "te reo Māori"
	},
	"mk": {
		"engine": 4,
		"name": "Macedonian",
		"nativeName": "македонски јазик"
	},
	"ml": {
		"engine": 4,
		"name": "Malayalam",
		"nativeName": "മലയാളം"
	},
	"mn": {
		"engine": 4,
		"name": "Mongolian",
		"nativeName": "монгол"
	},
	"mr": {
		"engine": 4,
		"name": "Marathi (Marāṭhī)",
		"nativeName": "मराठी"
	},
	"ms": {
		"engine": 5,
		"name": "Malay",
		"nativeName": "bahasa Melayu"
	},
	"mt": {
		"engine": 5,
		"name": "Maltese",
		"nativeName": "Malti"
	},
	"my": {
		"engine": 4,
		"name": "Burmese",
		"nativeName": "ဗမာစာ"
	},
	"nb": {
		"engine": 5,
		"name": "Norwegian Bokmål",
		"nativeName": "Norsk bokmål"
	},
	"ne": {
		"engine": 4,
		"name": "Nepali",
		"nativeName": "नेपाली"
	},
	"nl": {
		"engine": 7,
		"name": "Dutch",
		"nativeName": "Nederlands"
	},
	"nn": {
		"engine": 4,
		"name": "Norwegian Nynorsk",
		"nativeName": "Norsk nynorsk"
	},
	"no": {
		"engine": 4,
		"name": "Norwegian",
		"nativeName": "Norsk"
	},
	"ny": {
		"engine": 4,
		"name": "Nyanja",
		"nativeName": "chiCheŵa"
	},
	"pa": {
		"engine": 4,
		"name": "Panjabi",
		"nativeName": "ਪੰਜਾਬੀ"
	},
	"pl": {
		"engine": 7,
		"name": "Polish",
		"nativeName": "polski"
	},
	"ps": {
		"engine": 4,
		"name": "Pashto",
		"nativeName": "پښتو"
	},
	"pt": {
		"engine": 7,
		"name": "Portuguese",
		"nativeName": "Português"
	},
	"ro": {
		"engine": 5,
		"name": "Romanian",
		"nativeName": "română"
	},
	"ru": {
		"engine": 7,
		"name": "Russian",
		"nativeName": "русский язык"
	},
	"sd": {
		"engine": 4,
		"name": "Sindhi",
		"nativeName": "सिन्धी"
	},
	"si": {
		"engine": 4,
		"name": "Sinhala",
		"nativeName": "සිංහල"
	},
	"sk": {
		"engine": 5,
		"name": "Slovak",
		"nativeName": "slovenčina"
	},
	"sl": {
		"engine": 5,
		"name": "Slovene",
		"nativeName": "slovenščina"
	},
	"sm": {
		"engine": 5,
		"name": "Samoan",
		"nativeName": "gagana faa Samoa"
	},
	"sn": {
		"engine": 4,
		"name": "Shona",
		"nativeName": "chiShona"
	},
	"so": {
		"engine": 4,
		"name": "Somali",
		"nativeName": "Soomaaliga"
	},
	"sq": {
		"engine": 4,
		"name": "Albanian",
		"nativeName": "Shqip"
	},
	"sr": {
		"bing": "sr-Cyrl",
		"engine": 5,
		"name": "Serbian Cyrillic",
		"nativeName": "српски језик (ћирилица)"
	},
	"sr-La": {
		"bing": "sr-Latn",
		"engine": 1,
		"name": "Serbian Latin",
		"nativeName": "Srpski jezik (latinica)"
	},
	"st": {
		"engine": 4,
		"name": "Southern Sotho",
		"nativeName": "Sesotho"
	},
	"su": {
		"engine": 4,
		"name": "Sundanese",
		"nativeName": "Basa Sunda"
	},
	"sv": {
		"engine": 5,
		"name": "Swedish",
		"nativeName": "svenska"
	},
	"sw": {
		"engine": 5,
		"name": "Swahili",
		"nativeName": "Kiswahili"
	},
	"ta": {
		"engine": 5,
		"name": "Tamil",
		"nativeName": "தமிழ்"
	},
	"te": {
		"engine": 5,
		"name": "Telugu",
		"nativeName": "తెలుగు"
	},
	"tg": {
		"engine": 4,
		"name": "Tajik",
		"nativeName": "тоҷикӣ"
	},
	"th": {
		"engine": 5,
		"name": "Thai",
		"nativeName": "ไทย"
	},
	"tl": {
		"engine": 4,
		"name": "Tagalog",
		"nativeName": "Wikang Tagalog"
	},
	"to": {
		"engine": 1,
		"name": "Tongan",
		"nativeName": "Tonga"
	},
	"tr": {
		"engine": 5,
		"name": "Turkish",
		"nativeName": "Türkçe"
	},
	"ty": {
		"engine": 1,
		"name": "Tucked",
		"nativeName": "Tahiti"
	},
	"uk": {
		"engine": 5,
		"name": "Ukrainian",
		"nativeName": "українська"
	},
	"ur": {
		"engine": 5,
		"name": "Urdu",
		"nativeName": "اردو"
	},
	"uz": {
		"engine": 4,
		"name": "Uzbek",
		"nativeName": "zbek"
	},
	"vi": {
		"engine": 5,
		"name": "Vietnamese",
		"nativeName": "Tiếng Việt"
	},
	"xh": {
		"engine": 4,
		"name": "Xhosa",
		"nativeName": "isiXhosa"
	},
	"yi": {
		"engine": 4,
		"name": "Yiddish",
		"nativeName": "ייִדיש"
	},
	"yo": {
		"engine": 4,
		"name": "Yoruba",
		"nativeName": "Yorùbá"
	},
	"zh": {
		"bing": "zh-Hant",
		"engine": 5,
		"google": "zh-TW",
		"name": "Chinese Trad",
		"nativeName": "中文"
	},
	"zh-CN": {
		"bing": "zh-Hans",
		"engine": 5,
		"name": "Chinese Simp",
		"nativeName": "中文"
	},
	"auto": {
		"bing": "auto-detect",
		"engine": 7,
		"name": "Detect automatically"
	}
}
'''

LANG_MAP = loads(DATA)
