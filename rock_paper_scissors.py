import random

user_wins=0
com_wins=0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit. ").lower()
    if user_input == 'q':
        break
    if user_input not in options:
        print("Enter Valid Input! ")
        continue

    random_num = random.randint(0,2)
    # 0 for rock
    # 1 for paper
    # 2 for Scissors
    com_pick =options[random_num]
    print("Computer Picked ", com_pick+".")

    if user_input == "rock" and com_pick == "scissors":
        print("You won!")
        user_wins +=1

    elif user_input == "paper" and com_pick == "rock":
        print("You won!")
        user_wins +=1

    elif user_input == "scissors" and com_pick == "paper":
        print("You won!")
        user_wins +=1

    elif user_input == com_pick:
        print("Both pick same thing! Tied! ")
        continue

    else:
        print("You lost! Computer Wins")
        com_wins +=1


print("You have won", user_wins,"times.")
print("Computer wins", com_wins,"times.")
print("Goodbye!")
