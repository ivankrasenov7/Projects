import random

choice = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter a choice between 'rock', 'paper' and 'scissors' ").strip().lower()
    computer_choice = random.choice(choice).lower()

    if user_choice == "q" or user_choice == "quit" :
        break


    if user_choice not in choice:
        print("Invalid function")
        continue

    print(f"You chose {user_choice} and the computer selected {computer_choice}")

    computer_choice = random.choice(choice).lower()

    if user_choice == computer_choice:
        print("it's a tie")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        print("you won")
        quit()
    else:
        print("you lost")



