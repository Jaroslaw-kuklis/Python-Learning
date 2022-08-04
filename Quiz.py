import json

points = 0

def show_question(question_json):
    global points

    print()
    print(question_json["Question"])
    print("a:",question_json["a"])
    print("b:",question_json["b"])
    print("c:",question_json["c"])
    print("d:",question_json["d"])
    print()

    answer = input("Which answer you choice ?")
    print()

    if answer == question_json["Correct question is"]:
        print("Bravo! It is correct answer")
        points += 1
    else:
        print("It isn't correct answer!")

with open("Question.json") as json_file:
    questions = json.load(json_file)

    for i in range(0,len(questions)):
        show_question(questions[i])
    
    print()
    print(f"You have gathered {points} points")

