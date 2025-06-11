import pandas as pd
import numpy as np
import random

number = random.randint(1, 100)
print(number)  
attempts = 0
max_attempts = 10
 
while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1
 
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations .You guessed it in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a valid number.")
 
if attempts == max_attempts and guess != number:
    print(f"Sorry, you've reached the maximum number of attempts. The correct number was {number}.")