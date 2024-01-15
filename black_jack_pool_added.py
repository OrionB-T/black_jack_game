#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import time

suits = ['♥', '♦', '♣', '♠']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def create_deck():
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    value = 0
    num_aces = 0

    for card in hand:
        if card[0] in ['J', 'Q', 'K']:
            value += 10
        elif card[0] == 'A':
            num_aces += 1
        else:
            value += int(card[0])

    for _ in range(num_aces):
        if value + 11 <= 21:
            value += 11
        else:
            value += 1

    return value

def display_card(card):
    rank, suit = card
    card_ascii = f"""
┌─────────┐
│ {rank:<2}      │
│         │
│    {suit}    │
│         │
│      {rank:>2} │
└─────────┘
"""
    print(card_ascii)

def display_hand_slow(hand, hide_first_card=False):
    for i, card in enumerate(hand):
        if i == 0 and hide_first_card:
            print("┌─────────┐")
            print("│░░░░░░░░░│")
            print("│░░░░░░░░░│")
            print("│░░░░░░░░░│")
            print("│░░░░░░░░░│")
            print("│░░░░░░░░░│")
            print("└─────────┘")
        else:
            display_card(card)
            time.sleep(1) 

def player_turn(deck, player_hand, display_starting_hand=True):
    if display_starting_hand:
        print("Your Starting Hand:")
        display_hand_slow(player_hand)

    while True:
        choice = input("Do you want to hit or stand? ").lower()

        if choice == 'hit':
            new_card = random.choice(deck)
            deck.remove(new_card)
            player_hand.append(new_card)
            display_hand_slow([new_card])
            if calculate_hand_value(player_hand) > 21:
                print("Bust! You went over 21.")
                return 'bust'
        elif choice == 'stand':
            return 'stand'
        else:
            print("Invalid choice. Please enter 'hit' or 'stand.'")

def play_game():
    pool = 0
    
    while True:
        wager = int(input('How much money would you like to wager?'))
        pool += wager

        deck = create_deck()
        player_hand = []
        dealer_hand = []

        for _ in range(2):
            player_card = random.choice(deck)
            deck.remove(player_card)
            player_hand.append(player_card)

        for _ in range(2):
            dealer_card = random.choice(deck)
            deck.remove(dealer_card)
            dealer_hand.append(dealer_card)

        print("Dealer's Starting Hand:")
        display_hand_slow(dealer_hand, hide_first_card=True)

        player_result = player_turn(deck, player_hand)

        while player_result != 'stand':
            if player_result == 'bust':
                break  
            player_result = player_turn(deck, player_hand, display_starting_hand=False)

        if player_result == 'bust':
            print("You busted! Dealer wins.")
            pool -= wager
            print(f'Your new total ${pool}')
        else:
            print("\nDealer's Hand:")
            display_hand_slow(dealer_hand)

            while calculate_hand_value(dealer_hand) < 17:
                dealer_card = random.choice(deck)
                deck.remove(dealer_card)
                dealer_hand.append(dealer_card)
                display_hand_slow([dealer_card])

            if calculate_hand_value(dealer_hand) > 21:
                print("Dealer busted! You win.")
                pool += wager
                print(f'Your new total ${pool}')
            elif calculate_hand_value(dealer_hand) >= calculate_hand_value(player_hand):
                print("Dealer wins.")
                pool -= wager
                print(f'Your new total ${pool}')
            else:
                print("You win!")
                pool += wager
                print(f'Your new total ${pool}')

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    play_game()


# In[ ]:




