# Author: IBN (AMDG) 2/10/2022

player_cards = []
cpu_cards = []
import random
from time import sleep
from re import A
deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14]
name = input("What is your name? ")
print("Hello {0}, Let's play War!".format(name)); sleep(1.5)
print("I will shuffle the deck."); sleep(1.5)
random.shuffle(deck)
print("Shuffling..."); sleep(3)

for i, v in enumerate(deck):
    if i < 26:
        player_cards.append(deck[v])
    elif i >= 26:
        cpu_cards.append(deck[v])

print("The deck is shuffled. Let's Play!")