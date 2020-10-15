#!/usr/bin/python3

from googletrans import Translator

origin_languages = ["es"]
destination_languages = ["pt", "fr"]

word_list = input("Introduce your word list, separated with ,\n\n").split(",")
translator = Translator()

for word in word_list:
    for origin in origin_languages:
        for destination in destination_languages:
            translation = translator.translate(
                word, src=origin, dest=destination).text
            print(word + "  ----->   " + translation)
