#!/usr/bin/python3

from googletrans import Translator

origin_languages = ["es"]
destination_languages = ["pt","fr","en"]
translator = Translator()

file = open("hello.txt", "r") 
for line in file.readlines():

# for word in  word_list:
    for origin in origin_languages:
        for destination in destination_languages:
            translation = translator.translate(
               line, src=origin, dest=destination).text
            print(line + "  ----->   "   +  translation)

file.close() 