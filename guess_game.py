# Number guessing game

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
running = True

print("NUMBER GUESSING GAME")
print(f"YOU HAVE TO GUESS A NUMBER BETWEEN {lowest_num} AND {highest_num}")
print()

#--------------------------
while running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)

        if guess > highest_num or guess < lowest_num:
            print("OUT OF RANGE!")
            print(f"Please guess a number between {lowest_num} and {highest_num}")
        else:
            if guess > answer:
                print("Too high! Try again")
            elif guess < answer:
                print("Too low! Try again")
            elif guess == answer:
                print("CORRECT!")
                print(f"The answer was {answer}")
                running = False

    else:
        print("INVALID GUESS!")
        print(f"Please guess a number between {lowest_num} and {highest_num}")