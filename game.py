"""A number-guessing game."""
import random

# Put your code here
print('Hello new player!')
player_name = input("What is your name?")
secret_number = random.randint(1, 100)
# print(secret_number)
players_guess = 0
guesscount = 0

while players_guess != secret_number: 
    players_guess = int(input("What's your guess?"))
    guesscount += 1
    if players_guess < secret_number:
        print("Guess higher!")
    elif players_guess > secret_number:
        print("Guess lower!")
else: 
    print(f"You got it! It took you {guesscount} guesses!")

