import sys
password = []

password_lenght = int(input("How long should be password?"))

if password_lenght < 5:
    print("Password needs have minimum 5 signs")
    sys.exit(0)
    