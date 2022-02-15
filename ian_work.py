# Author: IBN (AMDG) 2/10/2022

import random
from time import sleep
deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14]
name = input("What is your name? ")

print("Hello {0}, Let's play War!".format(name)); sleep(1.5)
print("I will shuffle the deck."); sleep(1.5)
random.shuffle(deck)
print("Shuffling..."); sleep(3)

player = deck[0:int(len(deck)/2)]
cpu = deck[int(len(deck)/2):len(deck)]
player_len = len(player)
cpu_len = len(cpu)
print(player)
print(cpu)
print("You Have: {0} cards.".format(player_len)); sleep
print("I Have: {0} cards.".format(cpu_len)); sleep(1.5)
print("The deck is shuffled. Let's Play!"); sleep(2)

while player != [] or cpu != []:
    if player[0] == cpu[0]:
        print("WAR"); sleep(2)
        print("drawing three additional cards"); sleep(2)
        if player[4] == cpu[4]:
            print("WAR"); sleep(2)
            print("drawing three more cards"); sleep(2)
            if player[8] == cpu[8]:
                print("WAR"); sleep(2)
                print("drawing even more cards"); sleep(2)
            if player[8] > cpu[8]:
                print("victory {0} > {1}".format(player[8], cpu[8])); sleep(2)
                player.extend(player[0:9])
                player.extend(cpu[0:9])
                del player[:8]
                del cpu[:8]
                print(player)
                print(cpu)
            if player[8] < cpu[8]:
                print("defeat {0} < {1}".format(player[8], cpu[8])); sleep(2)
                cpu.extend(player[0:9])
                cpu.extend(cpu[0:9])
                del player[:9]
                del cpu[:9]
                print(player)
                print(cpu)
        if player[4] > cpu[4]:
            print("victory {0} > {1}".format(player[4], cpu[4])); sleep(2)
            player.extend(player[0:5])
            player.extend(cpu[0:5])
            del player[:5]
            del cpu[:5]
            print(player)
            print(cpu)
        if player[4] < cpu[4]:
            print("defeat {0} < {1}".format(player[4], cpu[4])); sleep(2)
            cpu.extend(cpu[0:5])
            cpu.extend(player[0:5])
            del player[:5]
            del cpu[:5]
            print(player)
            print(cpu)


    if player[0] > cpu[0]:
        print("victory {0} > {1}".format(player[0], cpu[0])); sleep(2)
        player.append(player[0])
        player.append(cpu[0])
        del player[0]
        del cpu[0]
        print(player)
        print(cpu)
            
    if player[0] < cpu[0]:
        print("loss {0} < {1}".format(player[0], cpu[0])); sleep(2)
        cpu.append(cpu[0])
        cpu.append(player[0])
        del cpu[0]
        del player[0]
        print(player)
        print(cpu)

if player == []:
    print("I win! You lose!"); sleep(1.5)
if cpu == []:
    print("You win! I lose!"); sleep(1.5)

retry = input("Would you like to play again? (Y/N)")
print(retry)
retry.isupper