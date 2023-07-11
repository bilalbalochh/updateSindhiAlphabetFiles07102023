from load_imgs_sounds import *
from funcs_for_sindhi import *

activity_num = input('Hello. What activity would you like to play? Please type 1 for identifying letter image by letter sound, 2 for identifying letter name by word sound, 3 for identifying the image by the word sound, 4 for identifying letter names by letter sounds, 5 for identifying letter names by the letter\'s image, 6 for repeat_after_me_letter_name_and_letter_sound or 7 for identifying letter sounds by letter names: ')
while((activity_num != '1') and (activity_num != '2') and (activity_num != '3') and (activity_num != '4') and (activity_num != '5') and (activity_num != '6') and (activity_num != '7')):
    activity_num = input('Please enter either 1, 2, 3, 4, 5, 6 or 7 and try again: ')
df = create_csv_file_for_usage(activity_num)
indexes_of_incorrect_guesses = []

ordered_or_randomized = input('Would you like to do this activity in letter order, or randomized? Type \'1\' for yes or \'2\' for no: ')
while((ordered_or_randomized != '1') and (ordered_or_randomized != '2')):
    ordered_or_randomized = input('Please try again and enter either 1 or 2 then press enter: ')

while len(list_indexes_of_letters_in_alphabet) != 0:
    if (ordered_or_randomized == '1'):
        x = list_indexes_of_letters_in_alphabet[0]
    elif (ordered_or_randomized == '2'):
        x = random.choice(list_indexes_of_letters_in_alphabet)
    print('Letter number:', x+1)
    if (activity_num == '1'):
        id_letter_image_by_letter_sound(x)
    elif (activity_num == '2'):
        id_letter_name_by_word_sound(x)
    elif (activity_num == '3'):
        id_letter_image_by_word_image(x)
    elif (activity_num == '4'):
        id_letter_name_sound_by_letter_sound(x)
    elif (activity_num == '5'):
        id_letter_name_by_letter_image(x)
    elif (activity_num == '6'):
        repeat_after_me_letter_name_and_letter_sound(x)
    elif (activity_num == '7'):
        id_letter_sound_by_letter_name(x)
    result = input('Enter 1 for correct, 2 for incorrect: ')
    while (result != '1' and result != '2'):
        result = input('Please enter either "1" or "2" and try again: ')
    listAlphabet[x].attempts += 1
    if (result == '2'):
        indexes_of_incorrect_guesses.append(x)
        new_score = 0
    if (result == '1'):
        new_score = round(float(1/listAlphabet[x].attempts),2)
    update_score(df, x, new_score,files,activity_num)
    list_indexes_of_letters_in_alphabet.remove(x)

    if (len(list_indexes_of_letters_in_alphabet) == 0):
        print('You are now done with all 52 letters, now the program will proceed with only letters of the incorrect answers.')
        print('You have', len(indexes_of_incorrect_guesses), 'incorrect answers to work on.')
        print('Your average score for this activity is: ', round(read_csv_values(files[index_of_title(activity_num)], average),2) * 100, '%')
        if (len(indexes_of_incorrect_guesses) == 0):
            break
        for y in indexes_of_incorrect_guesses:
            list_indexes_of_letters_in_alphabet.append(y)
        indexes_of_incorrect_guesses = []