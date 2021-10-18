# A guess the number game with three different gamemodes. 
import random

# This initializes the start of the game and asks for a gamemode. It will initialize whichever gamemode function is selected.
def gamestarting():
    while True:
        select_gamemode = input('Type 1, 2, or 3 to choose your gamemode, or Q to quit. ')
        if select_gamemode == '1':
            gamemode_one()
        elif select_gamemode == '2':
            gamemode_two()
        elif select_gamemode == '3':
            gamemode_three()
        elif select_gamemode.lower() == 'q':
            quit()
        else:
            print('Enter a valid gamemode.')
            continue

# This is the function for leaving the game. After each correct or incorrect guess, they can press Q to quit.
def leave_game():
    quit_game = input('Type Q to quit, or anything else to continue. ')
    if quit_game.lower() == 'q':
        quit()
    else:
        gamestarting()

# Function for gamemode 1.
def gamemode_one():
    print('I am thinking of a number between 1 and 10.')
    secret_number = random.randint(1, 10)
    for guesses_taken in range(1, 7):
        guess = int(input('Take a guess. '))

        if guess < secret_number:
            print('Your guess is too low.')
        elif guess > secret_number:
            print('Your guess is too high.')
        else:
            break
    if guess == secret_number:
        print('Congrats! You guessed my number in ' + str(guesses_taken) + ' guesses.')
        leave_game()
    else:
        print('Nope. The number I was thinking of was ' + str(secret_number) + '.')
        leave_game()

# Function for gamemode 2. The only change is that the max number the computer can guess is now 30.
def gamemode_two():
    print('I am thinking of a number between 1 and 30.')
    secret_number = random.randint(1, 30)
    for guesses_taken in range(1, 7):
        guess = int(input('Take a guess. '))

        if guess < secret_number:
            print('Your guess is too low.')
        elif guess > secret_number:
            print('Your guess is too high.')
        else:
            break
    if guess == secret_number:
        print('Congrats! You guessed my number in ' + str(guesses_taken) + ' guesses.')
        leave_game()
    else:
        print('Nope. The number I was thinking of was ' + str(secret_number) + '.')
        leave_game()
        
# Function for gamemode 3. The only change is that the max number the computer can guess is now 50.
def gamemode_three():
    print('I am thinking of a number between 1 and 50.')
    secret_number = random.randint(1, 50)
    for guesses_taken in range(1, 7):
        guess = int(input('Take a guess. '))

        if guess < secret_number:
            print('Your guess is too low.')
        elif guess > secret_number:
            print('Your guess is too high.')
        else:
            break
    if guess == secret_number:
        print('Congrats! You guessed my number in ' + str(guesses_taken) + ' guesses.')
        leave_game()
    else:
        print('Nope. The number I was thinking of was ' + str(secret_number) + '.')
        leave_game()

gamestarting()
