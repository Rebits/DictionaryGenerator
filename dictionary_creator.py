#!/usr/bin/python3

from googletrans import Translator
from google_speech import Speech
import sys,os


origin_languages = ["es"]
destination_languages = ["pt", "fr"]

dest_audio = sys.argv[1]


if os.path.isdir(f"{dest_audio}"):
    print("Selectd folder already exists")
    exit(-1)
else:
    os.mkdir(f"./{dest_audio}")


dir_path = os.path.dirname(os.path.realpath(__file__))

word_list = input("Introduce your word list, separated with ,\n\n").split(",")
translator = Translator()

for word in word_list:
    os.mkdir(f"./{dest_audio}/{word}")
    for origin in origin_languages:
        for destination in destination_languages:
            translation = translator.translate(word, src=origin, dest=destination).text
            speech = Speech(f"{translation}",destination)  
            array_word = [f"{word}"]
            array_word.append(f"{translation}[sound:{dir_path}/{dest_audio}/{word}/{destination}.mp3]")
            speech.save(f"{dest_audio}/{word}/{destination}.mp3")
            print(word + "  ----->   " + translation)
            



