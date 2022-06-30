import random

logo = """
  _____                     _                                          _ 
 / ____|                   (_)                                        | |
| |  __ _   _  ___  ___ ___ _ _ __   __ _    __ _  __ _ _ __ ___   ___| |
| | |_ | | | |/ _ \/ __/ __| | '_ \ / _` |  / _` |/ _` | '_ ` _ \ / _ \ |
| |__| | |_| |  __/\__ \__ \ | | | | (_| | | (_| | (_| | | | | | |  __/_|
 \_____|\__,_|\___||___/___/_|_| |_|\__, |  \__, |\__,_|_| |_| |_|\___(_)
                                     __/ |   __/ |                       
                                    |___/   |___/                        
"""

user_quit = False

while not user_quit:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of number between 1 and 100.")
    difficulty = input("Chose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        lives = 10
        rounds = lives
    else:
        lives = 5
        rounds = lives

    computer_number = random.randint(1, 100)

    for guessed_number in range(lives):
        print(f"You have {rounds} attempts to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess > computer_number:
            print("Too high.\nGuess again.")
            rounds -= 1
        elif user_guess == computer_number:
            break
        else:
            print("Too low.\nGuess again.")
            rounds -= 1

    if rounds > 0:
        print(f"You win with {rounds} attempts remaining.")
    else:
        print(f"You lose.The number was {computer_number}.")
    restart_game = input("Do you wish to play again? Type 'y' to restart and 'n' to quit.")
    if restart_game == "n":
        user_quit = True
        print("Thank you for playing!")
