# from s_a_main_code import listAlphabet, num_letters_in_alphabet, list_indexes_of_letters_in_alphabet, files, column_titles, fill_csv_with
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# import pygame
# from pygame import mixer
from load_imgs_sounds import *
import pandas as pd
# pygame.init()
# mixer.init()
# pygame.mixer.init()
import csv
from time import sleep

def show_image(image):
    plt.imshow(image)
    plt.show(block=False)

def play_sound(sound):
    sound.play()
    pygame.time.wait(int(sound.get_length() *1000))

def show_letter_image(rand_index):
    image = listAlphabet[rand_index].image
    show_image(image)

def show_word_image(rand_index):
    image = listAlphabet[rand_index].word_image
    show_image(image)

def show_word_typed(rand_index):
    image = listAlphabet[rand_index].word_spelled_image
    show_image(image)

def play_letter_name(rand_index):
    sound = listAlphabet[rand_index].name
    play_sound(sound)

def play_letter_sound(rand_index):
    sound = listAlphabet[rand_index].sound
    play_sound(sound)

def play_word_sound(rand_index):
    sound = listAlphabet[rand_index].word_sound
    play_sound(sound)

def warm_up():
    for i in range(num_letters_in_alphabet):
        print('Letter number:', i+1)
        play_letter_sound(i)

def id_letter_sound_by_letter_image(rand_index):
    show_letter_image(rand_index)
    input('Say the sound the letter makes then press enter: ')
    play_letter_sound(rand_index)

def id_letter_image_by_letter_name_sound(rand_index):
    play_letter_name(rand_index)
    input('Draw the letter then press enter: ')
    show_letter_image(rand_index)

# activity == '1'
# A2.csv
def id_letter_image_by_letter_sound(rand_index):
    play_letter_sound(rand_index)
    input("Draw the letter then press enter: ")
    show_letter_image(rand_index)

def id_letter_sound_by_letter_image(rand_index):
    show_letter_image(rand_index)
    input("Say the letter name's sound then press enter: ")
    play_letter_sound(rand_index)


def id_letter_name_by_letter_image(rand_index):
    show_letter_image(rand_index)
    input("Say the letter's name then press enter: ")
    play_letter_name(rand_index)


# A5.csv
def id_letter_name_by_word_typed(rand_index):
    show_word_typed(rand_index)
    input("Say the letter's name then press enter: ")
    play_letter_name(rand_index)

# activity == '3'
def id_letter_image_by_word_image(rand_index):
    show_word_image(rand_index)
    input("Draw the letter's image then press enter: ")
    show_word_image(rand_index)

# A7.csv
# activity == '2'
def id_letter_name_by_word_sound(rand_index):
    play_word_sound(rand_index)
    input("Say the letter's name then press enter: ")
    play_letter_name(rand_index)

def id_word_sound_by_word_image(rand_index):
    show_word_image(rand_index)
    input("Say the word's sound then press enter: ")
    play_word_sound(rand_index)

# A9.csv
def id_word_typed_image_by_word_sound(rand_index):
    play_word_sound(rand_index)
    input("Picture the image of the work then press enter:")
    show_word_image(rand_index)

def id_word_typed_image_by_letter_sound(rand_index):
    play_letter_sound(rand_index)
    input("Now write the word then press enter: ")
    show_word_typed(rand_index)

# A11.csv
# activity == '4'
def id_letter_name_sound_by_letter_sound(rand_index):
    play_letter_sound(rand_index)
    input("Now say the letter's name then press enter: ")
    play_letter_name(rand_index)

def repeat_after_me_letter_name_and_letter_sound(rand_index):
    show_letter_image(rand_index)
    input('Press enter then listen:')
    play_letter_name(rand_index)
    sleep(.4)
    play_letter_sound(rand_index)
    input('Now you say it. Then press enter again:')

def id_letter_sound_by_letter_name(rand_index):
    show_letter_image(rand_index)
    play_letter_name(rand_index)
    input("Now say the letter's sound then press enter: ")
    play_letter_sound(rand_index)

def read_csv_values_for_average(filename):
    sum_values = 0
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader):
            for value in row:
                try:
                    float_value = float(value)
                    sum_values+= float_value
                    # if float_value < percentage_below_include_in_activity:
                    #     indexes.append(index-offset_for_entries_in_csv_files)
                except ValueError:
                    pass  # Ignore non-float values
            average = sum_values/num_letters_in_alphabet
    return average

def read_csv_values(filename, purpose):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        purpose()

def average(reader, float_value):
    sum_values = 0
    for index, row in enumerate(reader):
        for value in row:
            try:
                float_value = float(value)
                sum_values+= float_value
            except ValueError:
                pass  # Ignore non-float values
        average = sum_values/num_letters_in_alphabet
        return average

def create_list_of_indexes_based_on_accuracy_score(reader):
    indexes = []
    for index, row in enumerate(reader):
        for value in row:
            try:
                float_value = float(value)
                if float_value < percentage_below_include_in_activity:
                    indexes.append(index)
            except ValueError:
                pass  # Ignore non-float values
    return indexes

def read_csv_values_2(reader,purpose):
    for index, row in enumerate(reader):
        for value in row:
            try:
                float_value = float(value)
                result_of_reading_csv = purpose()
            except ValueError:
                pass  # Ignore non-float values
    return result_of_reading_csv

def proedure_create_list_of_indexes_based_on_accuracy_score(index, float_value, indexes):
    if float_value < percentage_below_include_in_activity:
        return indexes.append(index)

def procedure_average(reader, float_value):
    sum_values += float_value
    average = sum_values/num_letters_in_alphabet
    return average

def index_of_title(activity_num):
    return int(activity_num)-1

def create_csv_file_for_usage(activity_num):
    index_title = index_of_title(activity_num)    
    title = column_titles[index_title]
    df = pd.DataFrame(index = range(num_letters_in_alphabet), columns = [title], dtype=float)
    for x in list_indexes_of_letters_in_alphabet:
        df.loc[x,title] = fill_csv_with
    df.to_csv(files[index_title], index=False)
    return df
    # return df
    # df_list[index_of_title] = pd.read_csv(files[index_of_title])

def update_score(df, x, new_score,files,activity_num):
    df.loc[x] = [new_score]
    df.to_csv(files[index_of_title(activity_num)], index=False)
