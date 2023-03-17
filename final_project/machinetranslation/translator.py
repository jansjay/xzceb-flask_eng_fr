"""
Translates Strings from French to English and
English to French
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2023-03-15'
authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Returns french translation of the passed english text
    """
    if not english_text:
        return english_text
    french_text = language_translator.translate(
                    text=english_text,
                    model_id='en-fr').get_result()
    if not french_text.get("translations"):
        return None
    return french_text.get("translations")[0].get("translation")

def french_to_english(french_text):
    """
    Returns english translation of the passed french text
    """
    if not french_text:
        return french_text
    english_text = language_translator.translate(
                    text=french_text,
                    model_id='fr-en').get_result()
    if not english_text.get("translations"):
        return None
    return english_text.get("translations")[0].get("translation")
