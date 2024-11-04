# Text Translator

A simple Python package for detecting languages and translating text using the Google Translate API. This package utilizes the `googletrans` library for language detection and text translation.

## Features

- Detect the language of a given text.
- Translate text from one language to another.
- Automatically detect the source language or specify it.

## Installation

To use this package, you'll need to install the required dependencies. You can install them using pip:

```bash
pip install requests googletrans==4.0.0-rc1
```

## Usage
You can use the package by importing the functions provided in the main.py file.

## Detecting Language
To detect the language of a text, use the get_lan_code function:
```bash
from ActTranslate import get_lan_code

text = "Bonjour le monde"
language_code = get_lan_code(text)
print(f"Detected language code: {language_code}")
```

## Translating Text
To translate text, use the translate_text function:
```bash
from main import translate_text

text_to_translate = "Hello world"
translated = translate_text(text_to_translate, input_lang='en', output_lang='fr')
print(translated)
```

## Parameters

- text (str): The text to be translated.
- input_lang (str, optional): The language code of the input text (e.g., 'en' for English). Defaults to 'auto'.
- output_lang (str, optional): The language code of the output text (e.g., 'fr' for French). Defaults to 'en'.

## Response Format
The translate_text function returns a JSON string containing:

- RESPONSE_STATUS: HTTP status code of the request.
- Source_Language: Detected source language code.
- Target_Language: Target language code.
- translated_text: The translated text.


## Example: 1
Here’s a complete example of how to use both functions:
```bash
from main import get_lan_code, translate_text

text = "Hola, ¿cómo estás?"
detected_lang = get_lan_code(text)
print(f"Detected Language: {detected_lang}")

translated = translate_text(text, input_lang=detected_lang, output_lang='en')
print(translated)
```

## Example: 2
Here’s a complete example of how to use both functions:
```bash
from main import get_lan_code, translate_text

text = "Hola, ¿cómo estás?"
translated = translate_text(text)
print(translated)
```

## Contributing
If you'd like to contribute to this project, feel free to open an issue or submit a pull request.