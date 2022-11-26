import json
from ibm_watson import LanguageTranslatorV3     # import language transator from watson
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator      # import authenticator

URL_LT = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/a48a4b7c-4ae0-46ab-888c-ce6876f58d4b'
APIKEY_LT = 'DcIUU2-MHTcUMfHzrTgj4d86TFjgi3-7z9V71gjY2mQX'
VERSION_LT = '2018-05-01'
authenticator = IAMAuthenticator(APIKEY_LT) # Authentication

# push the info in a translator variable
language_translator = LanguageTranslatorV3(version=VERSION_LT,authenticator=authenticator)
language_translator.set_service_url(URL_LT)
def hey_watson(translate, source, target):
  
    translated = language_translator.translate(text=translate, source=source, target=target).get_result()
    return translated['translations'][0]['translation'] 

lang_dict = { "ko":"한국어", "ja":"일본어", "zh":"중국어", "vi":"베트남어", "de":"독일어", "fr":"프랑스어", "it":"이탈리아어", "es":"스페인어" }

for key  in lang_dict:
  print(lang_dict[key], ':\t', hey_watson("Where is the Itaewon station?", 'en', key))