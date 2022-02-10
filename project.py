# Author: CMOB 2/10/2022

player_cards = []
cpu_cards = []

if player_cards[0] == cpu_cards[0]:
    print("WAR")
    print("drawing three additional cards")
    if player_cards[4] == cpu_cards[4]:
        print("WAR")
        print("drawing three more cards")
    if player_cards[4] > cpu_cards[4]:
        print("victory {0} > {1}".format(player_cards[4], cpu_cards[4]))
    if player_cards[4] < cpu_cards[4]:
        print("defeat {0} < {1}".format(player_cards[4], cpu_cards[4]))


if player_cards[0] > cpu_cards[0]:
    print("victory {0} > {1}".format(player_cards[0], cpu_cards[0]))
    player_cards.append(player_cards[0])
    player_cards.append(cpu_cards[0])
    del player_cards[0]
    del cpu_cards[0]
        
if player_cards[0] < cpu_cards[0]:
    print("loss {0} < {1}".format(player_cards[0], cpu_cards[0]))
    cpu_cards.append(cpu_cards[0])
    cpu_cards.append(player_cards[0])
    del cpu_cards[0]
    del player_cards[0]
