"""
This module uses IBM Watson services to translate text between English and French
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ["apikey"]
url = os.environ["url"]

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3("2018-05-01", authenticator)
language_translator.set_service_url(url)


def english_to_french(english_text: str) -> str:
    """
    This function is used to translate english text to french
    """

    french_translation = language_translator.translate(text=english_text,
                                                       model_id="en-fr"
                                                      ).get_result()

    return french_translation["translations"][0]["translation"]


def french_to_english(french_text: str) -> str:
    """
    This function is used to translate french text to english
    """

    english_translation = language_translator.translate(text=french_text,
                                                        model_id="fr-en"
                                                       ).get_result()

    return english_translation["translations"][0]["translation"]
