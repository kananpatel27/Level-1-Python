# Number Guessing Game 

import random

# Generate random number between 1 and 100
secret_number = random.randint(1, 100) 

print("🎮 Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100")

attempts = 0

while True:
    # User input
    guess = int(input("Enter your guess: "))
    attempts += 1

    # Conditions
    if guess > secret_number:
        print("📈 Too High! Try again.")

    elif guess < secret_number:
        print("📉 Too Low! Try again.")

    else:
        print("Congratulations!")
        print("You guessed the correct number:", secret_number)
        print("Total attempts:", attempts)
        break