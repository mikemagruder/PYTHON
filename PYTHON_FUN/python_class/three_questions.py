import random

answers = []

def bridge_keeper():
    questions = [ "What is your favorite color?", "What is the airspeed of an unladen swallow?", "What is the capital of Assyria?" ]

    correct_answer = "African or European?"


    print("STOP!!!\n Those who approach the Bridge of Death must answer me these questions three. Ere the other side they see.\n")

    name = input("What is your name?\n")
    quest = input("What is your quest?\n")

    random_question = random.randint(0,len(questions)-1)
    third = input(f"{questions[random_question]}\n")

    if random_question == 0:
        if third in answers:
            print("You have been casted into the gorge!!!\n")
            return False
        else:
            answers.append(third)
            print("Right. Off you go!\n")
            return False
    elif random_question == 1:
        if third == correct_answer:
            print("Wait!... I don't know! AHHHHHHH!!\n The gate keeper was casted into the gorge.")
            return False
        else:
            print("You have been casted into the gorge!!!\n")
            return False
    elif random_question == 2:
        if third == "Ninevah":
            print("Right!!! Of you go!\n")
            return False
        else:
            print("You have been casted into the gorge!!\n")
            return False

isGuessing = True

while isGuessing == True:
    isGuessing = bridge_keeper()

