import googletrans
from googletrans import Translator
# translator = Translator()
translator = Translator(service_urls=['translate.googleapis.com'])

def translate_lyrics(lyrics):
    translation = translator.translate(lyrics, dest='uk').text
    print(translation)
    #tr = translation.decode('utf-8')
    #print(tr)
    return translation
# def translate_lyris(lyrics):
