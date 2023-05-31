"""
1) Ask user for input
2) Generate random move
3) Calculate winner using logic
4) Print result for the user and ask to play again
"""
from random import randint

while True:
    #Ask user for input and check for invalid responses
    print("Welcome to Rock, Paper, Scissors!\n")
    flag = True
    while flag:
        user_choice = input("Choose Rock, Paper, or Scissors: ")
        user_choice = user_choice.lower()
        if user_choice == "rock":
            break
        elif user_choice == "paper":
            break
        elif user_choice == "scissors":
            break
        else:
            print("Invalid response!")
            continue

#Generate computer_choice
    print("Thinking...\n")
    random_number = randint(0, 301)
    computer_choice = ""
    if random_number <= 100:
        computer_choice += "rock"
    elif random_number <= 200 and random_number >= 101:
        computer_choice+= "paper"
    elif random_number <= 300 and random_number >= 201:
        computer_choice += "scissors"

#Calculate winner using logic and print result
#if Rock
    if user_choice == "rock" and computer_choice == "rock":
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "paper":
        print("Computer wins! (Rock vs Paper)")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win! (Rock vs Scissors)")
#if Paper
    elif user_choice == "paper" and computer_choice == "paper":
        print("It's a tie!")
    elif user_choice == "paper" and computer_choice == "scissors":
        print("Computer wins! (Paper vs Scissors)")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win! (Paper vs Rock)")
#if Scissors
    elif user_choice == "scissors" and computer_choice == "scissors":
        print("It's a tie!")
    elif user_choice == "scissors" and computer_choice == "rock":
        print("Computer wins! (Rock vs Scissors)")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win! (Scissors vs Paper)")
