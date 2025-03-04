

import random
first_time = True

while True:
    if first_time:
        dor = int(input('''Welcome to Rock-Paper-Scissors!
         The rules are simple:
         Rock crushes Scissors,
         Scissors cuts Paper,
         Paper covers Rock
         How many rounds do you want to play? '''))
        first_time = False
    else:
        dor = int(input('How many rounds this time?'))


    com_score=0
    my_score=0


    def print_score():
        print(f'Computer Score: {com_score}, Your Score: {my_score}')

    def print_com_choice():
        print(f'Computer chose: {com_choice}')
    while com_score+my_score<dor:


        my_choice=(input('Rock, Paper, or Scissors? ').lower().split())
        rock=['rock','r']
        paper=['paper','p']
        scissors=['scissors','s']
        if any(i in my_choice for i in rock) :
            my_choice= 'rock'

        elif any(i in my_choice for i in paper) :
            my_choice= 'paper'
        elif any(i in my_choice for i in scissors) :
            my_choice= 'scissors'
        else:
            print('Invalid choice, try again!')
            continue

        r_p_s = ["rock", "paper", "scissors"]
        com_choice = random.choice(r_p_s)

        # if my_choice == com_choice:
        #     print_com_choice()
        #     print("It's a tie!")
        #     print_score()
        #
        # elif my_choice == "rock":
        #     if com_choice == "scissors":
        #         print_com_choice()
        #         print("Rock crushes Scissors, you win this round!")
        #         my_score+=1
        #         print_score()
        #
        #     else:
        #         print_com_choice()
        #         print("Paper covers Rock, computer wins this round!")
        #         com_score+=1
        #         print_score()
        #
        # elif my_choice == "paper":
        #     if com_choice == "rock":
        #         print_com_choice()
        #         print("Paper covers Rock, you win this round!")
        #         my_score+=1
        #         print_score()
        #
        #     else:
        #         print_com_choice()
        #         print("Scissors cuts Paper, computer wins this round!")
        #         com_score+=1
        #         print_score()
        #
        #
        # elif my_choice == "scissors":
        #     if com_choice == "paper":
        #         print_com_choice()
        #         print("Scissors cuts Paper, you win this round!")
        #         my_score+=1
        #         print_score()
        #
        #     else:
        #         print_com_choice()
        #         print("Rock crushes Scissors, computer wins this round!")
        #         com_score+=1
        #         print_score()

        if my_choice == com_choice:
            print("It's a tie!")
        elif (my_choice == "rock" and com_choice == "scissors") or \
             (my_choice == "scissors" and com_choice == "paper") or \
             (my_choice == "paper" and com_choice == "rock"):
            print(f"{my_choice.capitalize()} beats {com_choice}, you win!")
            my_score += 1
        else:
            print(f"{com_choice.capitalize()} beats {my_choice}, computer wins!")
            com_score += 1

        print(f"Score - You: {my_score}, Computer: {com_score}")



    else:
        if com_score>my_score:
            print('Computer wins the game!')
        elif com_score<my_score:
            print('You win the game! Congratulations!')
        else:
            print('It\'s a tie game!')

        replay = (input('Do you want to play again? (Y/N):')).lower()
        if replay == 'y':
            continue
        elif replay == 'n':
            break
        else:
            print('Invalid input, try again!')
            continue



import random
first_time = True

while True:
    if first_time:
        dor = int(input('''slm in ye bazie sang kaghaz gheychie!
         ghavanin be in soorat hastan:
         sang gheychi ro mishkane,
         gheychi kaghazo mibore,
         kaghaz sango migire
         hala baraye shoro aval bgo bazi be chand :'''))
        first_time = False
    else:
        dor = int(input('bazi be chand?'))


    com_score=0
    my_score=0


    def print_score():
        print(f'com_score: {com_score}, my_score: {my_score}')

    def print_com_choice():
        print(f'my choice: {com_choice}')
    while com_score+my_score<dor:


        my_choice=(input('hala sang ya kaghaz ya gheychi ro entekhab kon:').lower().split())
        gheychi=['gheychi','g']
        sang=['sang','s']
        kaghaz=['kaghaz','k']
        if any(i in my_choice for i in gheychi) :
            my_choice= 'gheychi'

        elif any(i in my_choice for i in sang) :
            my_choice= 'sang'
        elif any(i in my_choice for i in kaghaz) :
            my_choice= 'kaghaz'
        else:
            print('entekhab eshtebah')
            continue

        s_k_g = ["sang", "kaghaz", "gheychi"]
        com_choice = random.choice(s_k_g)

        if my_choice == com_choice:
            print_com_choice()
            print("mosavi")
            print_score()

        elif my_choice == "sang":
            if com_choice == "kaghaz":
                print_com_choice()
                print("shoma in dor ra bakhtid")
                com_score+=1
                print_score()

            else:
                print_com_choice()
                print("shoma in dor ra bordid")
                my_score+=1
                print_score()

        elif my_choice == "kaghaz":
            if com_choice == "gheychi":
                print_com_choice()
                print("shoma in dor ra bakhtid")
                com_score+=1
                print_score()

            else:
                print_com_choice()
                print("shoma in dor ra bordid")
                my_score+=1
                print_score()


        elif my_choice == "gheychi":
            if com_choice == "sang":
                print_com_choice()
                print("shoma in dor ra bakhtid")
                com_score+=1
                print_score()

            else:
                print_com_choice()
                print("shoma in dor ra bordid")
                my_score+=1
                print_score()





    else:
        if com_score>my_score:
            print('com bord')
        elif com_score<my_score:
            print('shoma bordid')
        else:
            print('mosavi')

        replay = (input('dobare bazi mikoni? (Y/N):')).lower()
        if replay == 'y':
            continue
        elif replay == 'n':
            break
        else:
            print('entekhab eshtebah')
            continue

