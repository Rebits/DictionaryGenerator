#!/usr/bin/python3

from googletrans import Translator
from google_speech import Speech
import sys,os

dir_path = os.path.dirname(os.path.realpath(__file__))

if len(sys.argv) < 5:
    print("Input file, Output file, Audio folder, origin language and destination languages musto be set")
    exit(-1)

input_file = sys.argv[1]
output_file = sys.argv[2]
dest_audio = sys.argv[3]
origin_languages = sys.argv[4]
destination_languages = sys.argv[5]

if os.path.isfile(f"{output_file}"):
    print("Selected output file already exits")
    exit(-1)

if not os.path.isfile(f"{input_file}"):
    print("Selected input file is not redeable or does not exit")
    exit(-1)

if os.path.isdir(f"{dest_audio}"):
    print("Selected folder already exists")
    exit(-1)
else:
    os.mkdir(f"./{dest_audio}")

translator = Translator()

translated_file = open(f"{output_file}","w")

file = open(input_file, "r") 
temp = file.read().splitlines()
for line in temp:
    os.mkdir(f"./{dest_audio}/{line}")
    for origin in origin_languages:
        translated_file.writelines(line + "/" )
        for destination in destination_languages:
            translation = translator.translate(
                line, src=origin, dest=destination).text
            speech = Speech(f"{translation}",destination)  
            array_word = [f"{line}"]
            array_word.append(f"{translation}[sound:{dir_path}/{dest_audio}/{line}/{destination}.mp3]")
            speech.save(f"{dest_audio}/{line}/{destination}.mp3")
            translated_file.writelines(translation + "/")
        translated_file.writelines("\n")

file.close()
translated_file.close() 

            



