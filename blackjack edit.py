import time
import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
game_options = ['hit', 'stand']
play_options = ['y', 'yes']

print(f'{"*"*58} \n Welcome to Black Jack! \n{"*"*58}')
time.sleep(1)

player_name = input('Please enter your name: ')

# A loop that allows the user to play again once the game ends.
while True:
    user_input = input("Would you like to play? 'y' for yes, 'q' to quit. ")
    if user_input == 'y':
        play = True

    if user_input not in play_options:
        break

    random.shuffle(deck)
    d_cards = []
    p_cards = []
    time.sleep(2)

    while len(d_cards) != 2:
        random.shuffle(deck)
        d_cards.append(deck.pop())
        
        if len(d_cards) == 2:
            print("The dealer has:", d_cards[1], 'of 21.')
    
    while len(p_cards) != 2:
        random.shuffle(deck)
        p_cards.append(deck.pop())
        
        if len(p_cards) == 2:
            print(player_name, 'has', sum(p_cards), 'of 21. ')
            print("The cards you have are", p_cards)
    
    if sum(p_cards) > 21:
        print(f"You BUSTED!\n  {'*'*14} The dealer wins! {'*'*14}\n")
        exit()

    if sum(d_cards) > 21:
        print(f"Dealer is BUSTED!\n   {'*'*14} You win! {'*'*18}\n")
        exit()

    if sum(d_cards) == 21:
        print(f"{'*'*24} The dealer won! {'*'*14}")
        exit()

    if sum(d_cards) == 21 and sum(p_cards) == 21:
        print(f"{'*'*17} You tied! {'*'*25}")
        exit()

    def dealer_choice():
        if sum(d_cards) < 17:
            while sum(d_cards) < 17:
                random.shuffle(deck)
                d_cards.append(deck.pop())

        print("The dealer totaled " + str(sum(d_cards)) + " with the cards", d_cards, ".")
        print("You totaled " + str(sum(p_cards)) + " with the cards", p_cards, ".")

        if sum(p_cards) == sum(d_cards):
            print(f"{'*'*15} You tied! {'*'*15}")
            exit()

        if sum(d_cards) == 21:
            if sum(p_cards) < 21:
                print(f"{'*'*23} The dealer wins! {'*'*18}")
            
            elif sum(p_cards) == 21:
                print(f"{'*'*20} You tied! {'*'*26}")
            
            else:
                print(f"{'*'*23} The dealer wins! {'*'*18}")

        elif sum(d_cards) < 21:
            
            if sum(p_cards) < 21 and sum(p_cards) < sum(d_cards):
                print(f"{'*'*23} The dealer wins! {'*'*18}")
            
            if sum(p_cards) == 21:
                print(f"{'*'*22} You win! {'*'*22}")
            
            if 21 > sum(p_cards) > sum(d_cards):
                print(f"{'*'*22} You win! {'*'*22}")

        else:
            
            if sum(p_cards) < 21:
                print(f"{'*'*22} You win! {'*'*22}")

            elif sum(p_cards) == 21:
                print(f"{'*'*22} You win! {'*'*22}")

            else:
                print(f"{'*'*23} The dealer wins! {'*'*18}")

    while sum(p_cards) < 21:

    # to continue the game again and again !!
        k = input('Do you want to hit or stand?\nType 1 to hit, type 0 to stand. ')
        if k == 1:
            random.shuffle(deck)
            p_cards.append(deck.pop())
            print('You have a total of ' + str(sum(p_cards))
                + ' with the cards ', p_cards)
            
            if sum(p_cards) > 21:
                print(f'{"*"*13}You BUSTED!{"*"*13}\nThe dealer wins!')
            
            if sum(p_cards) == 21:
                print(f'{"*"*19}You win!{"*"*29}')

        else:
            dealer_choice()
            break
