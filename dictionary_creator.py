#!/usr/bin/python3

from googletrans import Translator



word_list = input("Introduce your word list, separated with ,\n\n").split(",")
translator = Translator()


for word in  word_list:
    translation = translator.translate(
    word, src="es", dest="pt").text

print(translation)
