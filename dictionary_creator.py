#!/usr/bin/python3

from googletrans import Translator

origin_languages = ["es"]
destination_languages = ["pt","fr","en"]
translator = Translator()
translated_file = open("translation.txt","w")

text = input("Please enter the name of the file with the extension:\n")
print(f'You entered {text}')

file = open(text, "r") 
temp = file.read().splitlines()
for line in temp:
    for origin in origin_languages:
        translated_file.writelines(line + "/" )
        for destination in destination_languages:
            translation = translator.translate(
                line, src=origin, dest=destination).text
            translated_file.writelines(translation + "/")
        translated_file.writelines("\n")

file.close()
translated_file.close() 

