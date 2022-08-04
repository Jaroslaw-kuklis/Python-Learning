from glob import glob
from msilib.schema import RadioButton
import sys
import random
import string
password = []
characters_left = -1
password_lenght = int(input("How long should be password?"))

def upadate_characters_left(number_of_characters):
        global characters_left
        if number_of_characters < 0 or number_of_characters > characters_left:
            print("the number of characters is not within the range", characters_left)
            sys.exit(0)
        else:
            characters_left -= number_of_characters
            print("Left characters:", characters_left)


if password_lenght < 5:
    print("Password needs have minimum 5 signs")
    sys.exit(0)
else:
    characters_left = password_lenght

lowercase_latters = int(input("How many lowercase password should have? "))
upadate_characters_left(lowercase_latters)

uppercase_letters = int(input("How many upercase password should have?"))
upadate_characters_left(uppercase_letters)

special_character = int(input("How many special charackter password should have ?"))
upadate_characters_left(special_character)

digits = int(input("How many digits password should have?"))
upadate_characters_left(digits)

if characters_left > 0:
    print("Didn't use all characters, password will filled randomly lowercase characters")
    print()
    
    lowercase_latters += characters_left

for _ in range(password_lenght):
    if lowercase_latters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_latters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_character > 0:
        password.append(random.choice(string.punctuation))
        special_character -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)

print("".join(password))
print()