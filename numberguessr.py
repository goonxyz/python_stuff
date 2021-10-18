# This is a guess the number game.
import random


# Ask the player to guess 6 times.
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
    else:
        print('Nope. The number I was thinking of was ' + str(secret_number) + '.')


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
    else:
        print('Nope. The number I was thinking of was ' + str(secret_number) + '.')


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
    else:
        print('Nope. The number I was thinking of was ' + str(secret_number) + '.')


def gamestarting():
    while True:
        select_gamemode = input('Type 1, 2, or 3 to choose your gamemode. ')
        if select_gamemode == '1':
            gamemode_one()
        elif select_gamemode == '2':
            gamemode_two()
        elif select_gamemode == '3':
            gamemode_three()
        else:
            print('Enter a valid gamemode.')
            continue


gamestarting()
