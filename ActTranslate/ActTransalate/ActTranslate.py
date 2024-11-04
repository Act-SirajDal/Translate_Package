import requests
import json
from googletrans import Translator,LANGUAGES


def get_lan_code(text):
    # Initialize the Translator
    translator = Translator()

    # Detect the language
    detection = translator.detect(text)
    language_code = detection.lang
    language_name = LANGUAGES.get(detection.lang, "Unknown")
    return language_code


def translate_text(text, input_lang=None, output_lang=None):
    if not input_lang:
        input_lang = 'auto'
    if not output_lang:
        output_lang = 'en'

    # Request URL...
    GOOGLE_TRANSLATE_URL = "https://translate.googleapis.com/translate_a/single"

    """Translates given text using the Google Translate API."""
    params = {
        'client': 'gtx',
        'sl': input_lang,
        'tl': output_lang,
        'dt': 't',
        'q': text,
    }
    response = requests.get(GOOGLE_TRANSLATE_URL, params=params)
    print('RESPONSE_STATUS', response.status_code)
    result = response.json()
    translated_text = ''.join([item[0] for item in result[0]])
    if input_lang == 'auto':
        input_lang = get_lan_code(text)
    return json.dumps({'RESPONSE_STATUS': response.status_code,'Source_Language':input_lang,'Target_Language':output_lang,'translated_text': translated_text})