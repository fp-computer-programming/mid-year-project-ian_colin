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
print("You Have: {0} cards.".format(player_len)); sleep(1.5)
print("I Have: {0} cards.".format(cpu_len)); sleep(1.5)
print("The deck is shuffled. Let's Play!"); sleep(2)

try:
    while len(player) != 0 or len(cpu) != 0:
        if player[0] > cpu[0]:
            print("victory {0} > {1}".format(player[0], cpu[0]))
            player.append(player[0])
            player.append(cpu[0])
            del player[0]
            del cpu[0]
            print(("You have {0} cards.").format(len(player)))
            print(('I have {0} cards.').format(len(cpu))); sleep(2)
            print(player)
            print(cpu)
        
        if player[0] < cpu[0]:
            print("loss {0} < {1}".format(player[0], cpu[0]))
            cpu.append(cpu[0])
            cpu.append(player[0])
            del cpu[0]
            del player[0]
            print(("You have {0} cards.").format(len(player)))
            print(('I have {0} cards.').format(len(cpu))); sleep(2)
            print(player)
            print(cpu)

        if len(player) < 5 or len(cpu) < 5:
            print("DANGER: Less than 5 cards!"); sleep(2)
            if player[0] == cpu[0]: 
                print("WAR"); sleep(2)
                print("drawing additional cards"); sleep(2)
                if player[3] > cpu[3]:
                    print("victory {0} > {1}".format(player[3], cpu[3]))
                    player.extend(player[0:4])
                    player.extend(cpu[0:4])
                    del player[:4]
                    del cpu[:4]
                    print(("You have {0} cards.").format(len(player)))
                    print(('I have {0} cards.').format(len(cpu))); sleep(2)
                    print(player)
                    print(cpu)
                    continue
                elif player[3] < cpu[3]:
                    print("defeat {0} < {1}".format(player[3], cpu[3]))
                    cpu.extend(cpu[0:4])
                    cpu.extend(player[0:4])
                    del player[:4]
                    del cpu[:4]
                    print(("You have {0} cards.").format(len(player)))
                    print(('I have {0} cards.').format(len(cpu))); sleep(2)
                    print(player)
                    print(cpu)
                    continue
                elif player[2] > cpu[2]:
                    print("victory {0} > {1}".format(player[2], cpu[2]))
                    player.extend(player[0:3])
                    player.extend(cpu[0:3])
                    del player[:3]
                    del cpu[:3]
                    print(("You have {0} cards.").format(len(player)))
                    print(('I have {0} cards.').format(len(cpu))); sleep(2)
                    print(player)
                    print(cpu)
                    continue
                elif player[2] < cpu[2]:
                    print("defeat {0} < {1}".format(player[2], cpu[2]))
                    cpu.extend(cpu[0:3])
                    cpu.extend(player[0:3])
                    del player[:3]
                    del cpu[:3]
                    print(("You have {0} cards.").format(len(player)))
                    print(('I have {0} cards.').format(len(cpu))); sleep(2)
                    print(player)
                    print(cpu)
                    continue
                elif player[1] > cpu[1]:
                    print("victory {0} > {1}".format(player[1], cpu[1]))
                    player.extend(player[0:2])
                    player.extend(cpu[0:2])
                    del player[:2]
                    del cpu[:2]
                    print(("You have {0} cards.").format(len(player)))
                    print(('I have {0} cards.').format(len(cpu))); sleep(2)
                    print(player)
                    print(cpu)
                    continue
                elif player[1] < cpu[1]:
                    print("defeat {0} < {1}".format(player[1], cpu[1]))
                    cpu.extend(cpu[0:2])
                    cpu.extend(player[0:2])
                    del player[:2]
                    del cpu[:2]
                    print(("You have {0} cards.").format(len(player)))
                    print(('I have {0} cards.').format(len(cpu))); sleep(2)
                    print(player)
                    print(cpu)
                    continue
            elif player[0] > cpu[0]:
                print("victory {0} > {1}".format(player[0], cpu[0]))
                player.append(player[0])
                player.append(cpu[0])
                del player[0]
                del cpu[0]
                print(("You have {0} cards.").format(len(player)))
                print(('I have {0} cards.').format(len(cpu))); sleep(2)
                print(player)
                print(cpu)
                continue
            elif player[0] < cpu[0]:
                print("loss {0} < {1}".format(player[0], cpu[0]))
                cpu.append(cpu[0])
                cpu.append(player[0])
                del cpu[0]
                del player[0]
                print(("You have {0} cards.").format(len(player)))
                print(('I have {0} cards.').format(len(cpu))); sleep(2)
                print(player)
                print(cpu)
                continue

        if player[0] == cpu[0]:
            print("WAR"); sleep(2)
            print("drawing three additional cards"); sleep(2)
            if player[4] == cpu[4]:
                print("WAR"); sleep(2)
                print("drawing three more cards"); sleep(2)
                if player[8] == cpu[8]:
                    print("WAR"); sleep(2)
                    print("drawing even more cards"); sleep(2)
                    if player[12] == cpu[12]:
                        print("WAR"); sleep(2)
                        print("drawing even more cards"); sleep(2)
                        if player[16] == cpu[16]:
                            print("WAR"); sleep(2)
                            print("drawing even more cards"); sleep(2)
                            if player[20] == cpu[20]:
                                print("WAR"); sleep(2)
                                print("drawing even more cards"); sleep(2)
                                if player[24] == cpu[24]:
                                    print("WAR"); sleep(2)
                                    print("drawing even more cards"); sleep(2)
                                    if player[26] == cpu[26]:
                                        print("Whoops! we ran out of cards, let's just skip that then")
                                        continue
                                    if player[26] < cpu[26]:
                                        print("defeat {0} < {1}".format(player[26], cpu[26])); sleep(2)
                                        print("Cpu won:{0} and {1}".format(player[:26],cpu[:26]))
                                        cpu.extend(player[0:27])
                                        cpu.extend(cpu[0:27])
                                        del player[:26]
                                        del cpu[:26]
                                        continue
                                    if player[26] > cpu[26]:
                                        print("victory {0} > {1}".format(player[26], cpu[26])); sleep(2)
                                        print("You won:{0} and {1}".format(player[:26],cpu[:26]))
                                        player.extend(player[0:27])
                                        player.extend(cpu[0:27])
                                        del player[:26]
                                        del cpu[:26]
                                        continue
                                if player[24] < cpu[24]:
                                    print("defeat {0} < {1}".format(player[24], cpu[24])); sleep(2)
                                    print("Cpu won:{0} and {1}".format(player[:24],cpu[:24]))
                                    cpu.extend(player[0:25])
                                    cpu.extend(cpu[0:25])
                                    del player[:24]
                                    del cpu[:24]
                                    continue
                                if player [24] > cpu[24]:
                                    print("victory {0} > {1}".format(player[24], cpu[24])); sleep(2)
                                    print("You won:{0} and {1}".format(player[:24],cpu[:24]))
                                    player.extend(player[0:25])
                                    player.extend(cpu[0:25])
                                    del player[:24]
                                    del cpu[:24]
                                    continue
                            if player[20] < cpu[20]:
                                print("defeat {0} < {1}".format(player[20], cpu[20])); sleep(2)
                                print("Cpu won:{0} and {1}".format(player[:20],cpu[:20]))
                                cpu.extend(player[0:21])
                                cpu.extend(cpu[0:21])
                                del player[:20]
                                del cpu[:20]
                                continue
                            if player[20] > cpu[20]:
                                print("victory {0} > {1}".format(player[20], cpu[20])); sleep(2)
                                print("You won:{0} and {1}".format(player[:20],cpu[:20]))
                                player.extend(player[0:21])
                                player.extend(cpu[0:21])
                                del player[:20]
                                del cpu[:20]
                                continue
                        if player[16] < cpu[16]:
                            print("defeat {0} < {1}".format(player[16], cpu[16])); sleep(2)
                            print("Cpu won:{0} and {1}".format(player[:16],cpu[:16]))
                            cpu.extend(player[0:17])
                            cpu.extend(cpu[0:17])
                            del player[:16]
                            del cpu[:16]
                            continue
                        if player[16] > cpu[16]:
                            print("victory {0} > {1}".format(player[16], cpu[16])); sleep(2)
                            print("You won:{0} and {1}".format(player[:16],cpu[:16]))
                            player.extend(player[0:17])
                            player.extend(cpu[0:17])
                            del player[:16]
                            del cpu[:16]
                            continue
                    if player[12] < cpu[12]:
                        print("defeat {0} < {1}".format(player[12], cpu[12])); sleep(2)
                        print("Cpu won:{0} and {1}".format(player[:12],cpu[:12]))
                        cpu.extend(player[0:13])
                        cpu.extend(cpu[0:13])
                        del player[:12]
                        del cpu[:12]
                        continue
                    if player[12] > cpu[12]:
                        print("victory {0} > {1}".format(player[12], cpu[12])); sleep(2)
                        print("You won:{0} and {1}".format(player[:12],cpu[:12]))
                        player.extend(player[0:13])
                        player.extend(cpu[0:13])
                        del player[:12]
                        del cpu[:12]
                        continue
                if player[8] > cpu[8]:
                    print("victory {0} > {1}".format(player[8], cpu[8]))
                    player.extend(player[0:9])
                    player.extend(cpu[0:9])
                    del player[:9]
                    del cpu[:9]
                    print(("You have {0} cards.").format(len(player)))
                    print(('I have {0} cards.').format(len(cpu))); sleep(2)
                    print(player)
                    print(cpu)
                    continue
                if player[8] < cpu[8]:
                    print("defeat {0} < {1}".format(player[8], cpu[8]))
                    cpu.extend(player[0:9])
                    cpu.extend(cpu[0:9])
                    del player[:9]
                    del cpu[:9]
                    print(("You have {0} cards.").format(len(player)))
                    print(('I have {0} cards.').format(len(cpu))); sleep(2)
                    print(player)
                    print(cpu)
                    continue
            if player[4] > cpu[4]:
                print("victory {0} > {1}".format(player[4], cpu[4]))
                player.extend(player[0:5])
                player.extend(cpu[0:5])
                del player[:5]
                del cpu[:5]
                print(("You have {0} cards.").format(len(player)))
                print(('I have {0} cards.').format(len(cpu))); sleep(2)
                print(player)
                print(cpu)
                continue
            if player[4] < cpu[4]:
                print("defeat {0} < {1}".format(player[4], cpu[4]))
                cpu.extend(cpu[0:5])
                cpu.extend(player[0:5])
                del player[:5]
                del cpu[:5]
                print(("You have {0} cards.").format(len(player)))
                print(('I have {0} cards.').format(len(cpu))); sleep(2)
                print(player)
                print(cpu)
                continue
except IndexError:
    if len(player) == 0:
        print("I win! You lose, {0}!".format(name)); sleep(1.5)
    if len(cpu) == 0:
        print("You win, {0}! I lose!".format(name)); sleep(1.5)
