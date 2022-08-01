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


for _ in word:
    user_word.append("_")

while True:
    letter = input("provide a letter: ")
    used_letters.append(letter)

    found_indexes = find_indexes(word, letter)
    if len(found_indexes) == 0:
        print("Wrong letter")
        num_of_tries -= 1
        print("Left number of tries:", num_of_tries)
        if num_of_tries == 0:
            print("The end of game")
            sys.exit(0)

    print("used letters:", used_letters)