import pandas as pd
import random
# from main import *


# this is the file we will want to update
file_to_learn = 'cool_words.csv'

def random_number_generator(word_list):
    # random value from 0 to 24
    x = random.randint(0, len(word_list)-1)
    print(f'random value: {x}')
    # a single dictionary from the list
    choice = word_list[x]
    print(f'random choice: {choice}')
    spanish = choice['Spanish']
    print(f'Spanish word: {spanish}')
    english = choice['English']
    print(f'English word: {english}')
    return choice, spanish, english


def remove_pair(word_list, dict):
    '''choice is a key-value pair dictionary from the list'''
    word_list.remove(dict)
    print(f'new list len: {len(word_list)}')
    print(f'new word list: {word_list}')
    return word_list


def write_new_file(word_list, file_name):
    words_data_frame = pd.DataFrame(word_list, columns=['Spanish', 'English'])
    print(words_data_frame)
    words_data_frame.to_csv(file_name, index=False)


def open_file(file_to_learn):
    try:
        # create list of dicts from master list
        df = pd.read_csv(file_to_learn)
        # create list of dictionaries from data frame
        words_list = df.to_dict(orient='records')
        print(f'original len: {len(words_list)}')
        print(words_list)
        return words_list
    except FileNotFoundError:
        print('File doe''s not exist')
        print('Open new blank file from test words master')
        # create list of dicts from master list
        df = pd.read_csv('test_words.csv')
        # df = pd.read_csv('../../../../../PycharmProjects/day-31-flashcard/test_words.csv')
        # create list of dictionaries from data frame
        cool_words_list = df.to_dict(orient='records')
        write_new_file(cool_words_list, file_to_learn)
        return cool_words_list


# def green_check(word_list):
#     choice, spanish, english = random_number_generator(word_list=word_list)
#     show_front(spanish)
#
#
# def show_front(span_def):
#     canvas.itemconfig(canvas_image, image=front_img)
#     # update the canvas text
#     canvas.itemconfig(can_label_1, text='Spanish', fill='black')
#     canvas.itemconfig(can_label_2, text=span_def, fill='black')


