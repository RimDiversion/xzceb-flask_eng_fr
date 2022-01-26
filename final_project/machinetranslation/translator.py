"""
translator is to convert French text to English or vice-versa
"""

import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

auth = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(version='2022-01-26', authenticator=auth)
translator.set_service_url(url)

def english_to_french(english_text):
    """
    Takes english text and returns it in French
    """
    if not english_text:
        return None
    french_text = translator.translate(
        text=english_text,
        model_id='en-fr').get_result()['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    Takes French text and returns it in English
    """
    if not french_text:
        return None
    english_text = translator.translate(
        text=french_text,
        model_id='fr-en').get_result()['translations'][0]['translation']
    return english_text
