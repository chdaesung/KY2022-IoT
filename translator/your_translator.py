import json
from ibm_watson import LanguageTranslatorV3     # import language transator from watson
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator      # import authenticator

URL_LT = '여러분의 왓슨 language translator 엔드포인트 url'
APIKEY_LT = '여러분의 api key'
VERSION_LT = '2018-05-01'
authenticator = IAMAuthenticator(APIKEY_LT) # Authentication

# push the info in a translator variable
language_translator = LanguageTranslatorV3(version=VERSION_LT,authenticator=authenticator)
language_translator.set_service_url(URL_LT)
def hey_watson(translate, source, target):
  
    translated = language_translator.translate(text=translate, source=source, target=target).get_result()
    return translated['translations'][0]['translation'] 

lang_dict = { "ko":"한국어", "de":"독일어", "it":"이태리어" }

for key  in lang_dict:
  print(lang_dict[key], ':\t', hey_watson("Where is the Itaewon station?", 'en', key))