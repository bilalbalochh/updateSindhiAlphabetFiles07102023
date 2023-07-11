import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# import time, sys
import pygame
from pygame import mixer
import os
# import numpy as np
pygame.init()
mixer.init()
pygame.mixer.init()
# import csv
import random
# import pandas as pd
# from time import sleep


num_letters_in_alphabet = 52
list_indexes_of_letters_in_alphabet = list(range(num_letters_in_alphabet))
offset_for_activities = 1
offset_for_entries_in_csv_files = 1
percentage_below_include_in_activity = 0.75
indexes_of_incorrect_guesses = []
fill_csv_with = None
column_titles = ['symbol', 'number', 'id_letter_by_image', 'id_letter_image_by_letter_sound', 'id_image_by_letter_sound', 'id_letter_sound_by_image','id_letter_name_by_word_spelled_image','id_letter_image_by_word_image', 'id_letter_name_by_word_sound', 'id_word_sound_by_word_image' ,'id_image_by_word','id_word_by_letter_sound', 'id_letter_name_by_letter_sound', 'id_letter_name_by_letter_image', 'repeat_after_me_letter_name_and_letter_sound', 'id_letter_sound_by_letter_name']
files = ['Symbol.csv', 'Number.csv', 'A1.csv', 'A2.csv', 'A3.csv', 'A4.csv', 'A5.csv', 'A6.csv', 'A7.csv', 'A8.csv', 'A9.csv', 'A10.csv', 'A11.csv', 'A12.csv', 'A13.csv', 'A14.csv']

def split_list(list):
    return list[3:4] + list[8:9] + list[10:11] + list[12:16]

column_titles = split_list(column_titles)
files = split_list(files)

class alphabet:
    def __init__(letter,image,name,sound,typed, word_image, word_sound, word_spelled_image, attempts):
        letter.image = image
        letter.name = name
        letter.sound = sound
        letter.typed = typed
        letter.word_image = word_image
        letter.word_sound = word_sound
        letter.word_spelled_image = word_spelled_image
        letter.attempts = attempts

listAlphabet = []
images = []
names = []
sounds = []
word_images = []
word_sounds = []
word_name_image = []

image_dir = "/home/bbaloch/myproject/sindhiAlphabet/alphabetImages"
name_dir = "/home/bbaloch/myproject/sindhiAlphabet/alphabetLetterNameSound"
sound_dir = "/home/bbaloch/myproject/sindhiAlphabet/alphabetLetterSound"
word_image_dir = "/home/bbaloch/myproject/sindhiAlphabet/alphabetWordImage"
word_sound_dir = "/home/bbaloch/myproject/sindhiAlphabet/alphabetWordSound"
word_spelled_image_dir = "/home/bbaloch/myproject/sindhiAlphabet/alphabetWordSpelledImage"
typed_list = ['ا', 'ب' ,'ٻ', 'ڀ', 'ت','ٿ', 'ٽ','ٺ', 'ث','پ', 'ج', 'ڄ','جهہ' ,'ڃ','چ', 'ڇ', 'ح', 'خ' ,'د','ڌ','ڏ', 'ڊ','ڍ', 'ذ', 'ر', 'ڙ', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف','ڦ', 'ق', 'ڪ', 'ک', 'گ','ڳ','گهہ','ڱ', 'ل', 'م','ن', 'ڻ', 'و','ھ', 'ء', 'ي']
typed_list = typed_list[:num_letters_in_alphabet]
order_list = range(0,num_letters_in_alphabet)

all_images_dir = [image_dir, word_image_dir, word_spelled_image_dir]
all_sounds_dir = [name_dir, sound_dir, word_sound_dir]
all_images = [images,word_images,word_name_image]
all_sounds = [names, sounds, word_sounds]


for indexer_of_dir in range(len(all_images_dir)):
    for filename in sorted(os.listdir(all_images_dir[indexer_of_dir]), key = lambda x: int(x.split(".")[0])): 
        image_file = plt.imread(os.path.join(all_images_dir[indexer_of_dir], filename))
        image = plt.imread(os.path.join(all_images_dir[indexer_of_dir], filename))
        (all_images[indexer_of_dir]).append(image)

for indexer_of_dir in range(len(all_sounds_dir)):
    for filename in sorted(os.listdir(all_sounds_dir[indexer_of_dir]), key = lambda x: int(x.split(".")[0])):
        name_file = os.path.join(all_sounds_dir[indexer_of_dir], filename)
        name = pygame.mixer.Sound(name_file)
        (all_sounds[indexer_of_dir]).append(name)

for i in range(num_letters_in_alphabet):
    listAlphabet.append(alphabet(images[i],names[i],sounds[i],typed_list[i], word_images[i], word_sounds[i], word_name_image[i],0))       

