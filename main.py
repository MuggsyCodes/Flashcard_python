from tkinter import *
from flashcard_functions import *

BACKGROUND_COLOR = "#B1DDC6"
LABEL_X_POS = 400
LABEL_Y_POS = 150


def card_flip(can_label_1, can_label_2, translation):
    '''Show other side of card and english translation'''
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(can_label_1, text='English', fill='white')
    canvas.itemconfig(can_label_2, text=translation, fill='white')

# How do I get the updated word list to the check mark function???


def green_check(choice, words_list):
    global english
    '''Need to pop the current spanish-english combo on the screen'''
   # open the current file of words to learn
    df = pd.read_csv(file_to_learn)
    # create list of dictionaries from data frame
    new_words_list = df.to_dict(orient='records')
    print(f'len new words list: {len(new_words_list)}')
    # print(f'first dict choice: {choice}')
    try:
        # this will only work the first time around using the global variables
        new_words_list = remove_pair(words_list, choice)
        write_new_file(new_words_list, file_to_learn)
        choice, spanish, english = random_number_generator(word_list=new_words_list)
        print(f'UPDATED dict choice: {choice}')
        show_spanish(spanish, english)
    except ValueError:
        # this should work each time after
        print('Green check - Value error except block')
        choice, spanish, english = random_number_generator(word_list=new_words_list)
        print(f'UPDATED dict choice: {choice}')
        new_words_list = remove_pair(new_words_list, choice)
        write_new_file(new_words_list, file_to_learn)
        show_spanish(english, spanish)
    finally:
        if len(new_words_list) == 0:
            print('finally, no more words left...')
            print('No more words left')
            canvas.itemconfig(can_label_1, text='List Completed!', fill='black')
            canvas.itemconfig(can_label_2, text='You mastered all words', fill='black')
            return len(new_words_list)
            # note: Unless I return something here, the try block is executed again


def x_button(new_words_list):
    print('X Button')
    choice, spanish, english = random_number_generator(word_list=new_words_list)
    print(f'UPDATED dict choice: {choice}')
    show_spanish(english, spanish)


def show_spanish(spanish, english):
    #choice, spanish, english = random_number_generator(word_list=new_word_list)
    canvas.itemconfig(canvas_image, image=front_img)
    # update the canvas text
    canvas.itemconfig(can_label_1, text='Spanish', fill='black')
    canvas.itemconfig(can_label_2, text=spanish, fill='black')
    window.after(1000, card_flip, can_label_1, can_label_2, english)


print('Very top of loooooP???')

# 1. Open CSV file of words to be learnt
# a list of dictionaries
a_list_words = open_file(file_to_learn)
print('A List of Words from CSV File')
print(a_list_words)
print(f'len of list: {len(a_list_words)}')

#2. Random number key value pair selection
# choice is a single dictionary
choice, spanish, english = random_number_generator(a_list_words)

window = Tk() # window widget
print('Widow creation loop')
window.title('Flash card I beat you.')
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)

# ---------------- CANVAS ------------------ #
canvas = Canvas(width = 800, height = 525, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file='./images/card_front.png')
back_img = PhotoImage(file='./images/card_back.png')
canvas_image = canvas.create_image(410 ,270, image=front_img)
canvas.grid(column = 0, row = 0, columnspan = 2)

#Buttons
check_mark = PhotoImage(file="./images/right.png")
check_mark_button = Button(image=check_mark, highlightthickness=0, command=lambda: green_check(choice, a_list_words))
check_mark_button.grid(column=1, row=1, columnspan=1)

x_mark = PhotoImage(file="./images/wrong.png")
x_mark_button = Button(image=x_mark, highlightthickness=0, command = lambda: x_button(a_list_words))
x_mark_button.grid(column=0, row=1, columnspan=1)

# CANVAS
can_label_1 = canvas.create_text(400, 150, text='ESPANOL!', font=('Arial', 40, 'italic'))
can_label_2 = canvas.create_text(400, 350, text= spanish, font=('Arial', 60, 'bold'))


# CARD FLIP
window.after(1000, card_flip, can_label_1, can_label_2, english)
print('Reached main loop')

window.mainloop()