#!/usr/bin/env python
# coding: utf-8

# In[1]:
import random

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
        if card in ['J', 'Q', 'K']:
            value += 10
        if card == 'A':
            num_aces += 1
        else:
            value += int(card)
    for _ in range(num_aces):
        if value + 11 <= 21:
            value += 11
        else:
            value += 1

    return value
# In[ ]:




