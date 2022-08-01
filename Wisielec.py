from csv import unregister_dialect
from operator import truediv
import sys

num_of_tries = 5 
word = "monkeyoo"

user_word = []
used_letters = []


def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes

def show_state_of_game():
    print()
    print(user_word)
    print("Number of tries:", num_of_tries)
    print("Used letters:", used_letters)


for _ in word:
    user_word.append("_")

while True:
    letter = input("provide a letter: ")
    used_letters.append(letter)

    found_indexes = find_indexes(word, letter)
    if len(found_indexes) == 0:
        print("Wrong letter")
        num_of_tries -= 1
        
        if num_of_tries == 0:
            print("The end of game")
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter
        

        if "".join(user_word) == word:
            print("You find the correct word!")
            sys.exit(0)
    show_state_of_game()

    