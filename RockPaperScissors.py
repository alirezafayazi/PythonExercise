import random

while True:
    try :
        # اعداد را از کاربر دریافت میکنیم
        print('(please enter a number) ')
        repeat=int(input('How many times do we play?\n'))
        break
    except:
        #اگر داده های ورودی به عدد صحیح تبدیل نشدند اخطار میدهیم تا کاربر عدد وارد کند
        print('\n ** please enter a number (Just enter number !) \n')


possible_actions = ["rock", "paper", "scissors"]
user_score= 0
computer_score= 0

for i in range(repeat):
    while True:
        try :
             # انتخاب کاربر سنگ یا کاغذ یا قیجی میباشد
            user_choice = int(input("Enter a choice (0,1 or 2) \n\n0.rock, \n1.paper, \n2.scissors \n: "))
            while not(0<=user_choice<3):
                print('\nYour choice was not available in the items')
                user_choice = int(input("Enter a choice (0,1 or 2) \n\n0.rock, \n1.paper, \n2.scissors \n: "))
            break
        except:
            #اگر داده های ورودی صحبح نباشد کاربر خطا دریافت میکند
            print('\n ** Please select one of the items \n')

    random_choice=random.randint(0,2)
    if user_choice == random_choice:
        print(f"\tBoth players selected {possible_actions[user_choice]}. It's a tie!")
    elif user_choice == 0:
        if random_choice == 2:
            user_score+=1
            print("\tRock smashes scissors! , You got 1 score!")
        else:
            computer_score+=1
            print("\tPaper covers rock! , computer got 1 score!")
    elif user_choice == 1:
        if random_choice == 0:
            user_score+=1
            print("\tPaper covers rock! , You got 1 score!")
        else:
            computer_score+=1
            print("\tScissors cuts paper! , computer got 1 score!")
    elif user_choice == 2:
        if random_choice == 1:
            user_score+=1
            print("\tScissors cuts paper! , You got 1 score!!")
        else:
            computer_score+=1
            print("\tRock smashes scissors! computer got 1 score!")

    print(f"""\nYou choose {possible_actions[user_choice]}, computer choose {possible_actions[random_choice]}.
\n--your score : {user_score}\n--computer score: {computer_score}""")
    if (user_score > repeat) or (computer_score > repeat) :
        break
if user_score > computer_score:
    print(f'*** You Win ***\n\t Your score : {user_score}')
elif user_score < computer_score:
    print(f':( You Lose ): \ncomputer score : {computer_score}')
else:
    print(f'You are tied ! \ncomputer score : {computer_score}')
    