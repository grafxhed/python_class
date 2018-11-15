import random as ran 
import time

while True:

    dice_num=("1","2","3","4","5","6")

    one=(""" ____________
    |            |
    |            |
    |            |
    |     ()     |
    |            |
    |            |
     ____________\n""")

    two=("""____________
    |            |
    |            |
    |       ()   |
    |            |
    |   ()       |
    |            |
     ____________\n""")

    three=("""____________
    |            |
    |       ()   |
    |            |
    |     ()     |
    |            |
    |  ()        |
     ____________\n""")

    four=("""____________
    |            |
    | ()     ()  |
    |            |
    |            |
    |            |
    | ()     ()  |
     ____________\n""")

    five=("""____________
    |            |
    | ()      () |
    |            |
    |     ()     |
    |            |
    | ()      () |
     ____________\n""")

    six=(""" ____________
    |            |
    |  ()    ()  |
    |            |
    |  ()    ()  |
    |            |
    |  ()    ()  |
     ____________\n""")

    p1_score= 0
    cpu_score=0

    p1= input ("press Enter to roll a die ")
    for p1 in range (3):
        time.sleep(1)
        print("\n\trolling die...\n")
        time.sleep(2)

        p1= ran.choice(dice_num)
        if p1 == "1":
            print ("you rolled,one\n",one)

        elif p1 == "2":
            print ("you rolled, two\n",two)

        elif p1 == "3":
            print ("you rolled, three\n",three)

        elif p1 == "4":
            print ("you rolled, four\n",four)

        elif p1 == "5":
            print ("you rolled, five\n", five)

        elif p1 == "6":
            print ("you rolled, six\n",six)

        time.sleep(2.5)
        print ("my turn\n")
        time.sleep(1)
        print ("\n\trolling die...\n")
        time.sleep(2)

        cpu= ran.choice(dice_num)
        if cpu == "1":
            print ("I rolled,one\n",one)

        elif cpu == "2":
            print ("I rolled, two\n",two)

        elif cpu == "3":
            print ("I rolled, three\n",three)

        elif cpu == "4":
            print ("I rolled, four\n",four)

        elif cpu == "5":
            print ("I rolled, five\n", five)

        elif cpu == "6":
            print ("I rolled, six\n",six)


        if p1 > cpu:
            p1_score = p1_score +3
            time.sleep(1.5)
            print ("\n\tGREAT LUCK! You won this, round")
        elif p1 ==cpu:
            p1_score = p1_score +1
            cpu_score = cpu_score +1
            time.sleep(1.5)
            print("\n\t OMG! it's a tie!")
        else:
            cpu_score = cpu_score +3
            time.sleep(1.5)
            print ("\n\tI won! Better luck next time")

        another_try= input ("\t\npress ENTER to have another go: ")

    time.sleep(2)
    print("your score is, ", p1_score)
    print ("my score is, ", cpu_score)
    if p1_score > cpu_score:
            time.sleep(1.5)
            print ("\n\tGREAT LUCK! YOU ARE THE WINNER!")
    elif p1_score ==cpu_score:
        time.sleep(1.5)
        print("\n\t OMG! it's a tie!")
    else:
        time.sleep(1.5)
        print ("\n\tI won! Better luck next time")

    quit_game = input ("\t\npress 'q' to end the game or \t\ntype 'y' to have another go: ")

    if quit_game == "y":
        pass
    elif quit_game == "q":
        break
