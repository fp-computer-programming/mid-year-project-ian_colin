# Author: CMOB 2/10/2022

player = [2,13,14,5,4]
cpu = [2,2,9,10,2]

if player[0] == cpu[0]:
    print("WAR")
    print("drawing three additional cards")

    if player[4] > cpu[4]:
        print("victory {0} > {1}".format(player[4], cpu[4]))
        print("You won:{0} and {1}".format(player[:4],cpu[:4]))

    if player[4] < cpu[4]:
        print("defeat {0} < {1}".format(player[4], cpu[4]))
        print("Cpu won:{0} and {1}".format(player[:4],cpu[:4]))

    if player[4] == cpu[4]:
        print("WAR")
        print("drawing three more cards")

        if player[8] > cpu[8]:
            print("victory {0} > {1}".format(player[4], cpu[4]))
            print("You won:{0} and {1}".format(player[:4],cpu[:4]))

        if player[8] < cpu[8]:
            print("defeat {0} < {1}".format(player[4], cpu[4]))
            print("Cpu won:{0} and {1}".format(player[:4],cpu[:4]))

        if player[8] == cpu[8]:
            print

            if player[12] < cpu[12]:
                print("defeat {0} < {1}".format(player[4], cpu[4]))
                print("Cpu won:{0} and {1}".format(player[:4],cpu[:4]))

            if player[12] > cpu[12]:
                print("victory {0} > {1}".format(player[4], cpu[4]))
                print("You won:{0} and {1}".format(player[:4],cpu[:4]))
                
            if player[12] == cpu[12]:
                print("WAR")
                print("drawing three additional cards")

                if player[16] < cpu[16]:
                    print("defeat {0} < {1}".format(player[4], cpu[4]))
                    print("Cpu won:{0} and {1}".format(player[:4],cpu[:4]))

                if player[16] > cpu[16]:
                    print("victory {0} > {1}".format(player[4], cpu[4]))
                    print("You won:{0} and {1}".format(player[:4],cpu[:4]))

                if player[16] == cpu[16]:
                    print("WAR")
                    print("drawing three additional cards")
                    
                    if player[20] < cpu[20]:
                        print("defeat {0} < {1}".format(player[4], cpu[4]))
                        print("Cpu won:{0} and {1}".format(player[:4],cpu[:4]))

                    if player[20] > cpu[20]:
                        print("victory {0} > {1}".format(player[4], cpu[4]))
                        print("You won:{0} and {1}".format(player[:4],cpu[:4]))

                    if player[20] == cpu[20]:
                        print("WAR")
                        print("drawing three additional cards")

                        if player[24] < cpu[24]:
                            print("defeat {0} < {1}".format(player[4], cpu[4]))
                            print("Cpu won:{0} and {1}".format(player[:4],cpu[:4]))

                        if player [24] > cpu[24]:
                            print("victory {0} > {1}".format(player[4], cpu[4]))
                            print("You won:{0} and {1}".format(player[:4],cpu[:4]))

                        if player[24] == cpu[24]:
                            print("WAR")
                            print("drawing three additional cards")

                            if player[26] < cpu[26]:
                                print("defeat {0} < {1}".format(player[4], cpu[4]))
                                print("Cpu won:{0} and {1}".format(player[:4],cpu[:4]))

                            if player[26] > cpu[26]:
                                print("victory {0} > {1}".format(player[4], cpu[4]))
                                print("You won:{0} and {1}".format(player[:4],cpu[:4]))

elif player[0] > cpu[0]:
    print("victory {0} > {1}".format(player[0], cpu[0]))
    player.append(player[0])
    player.append(cpu[0])
    del player[0]
    del cpu[0]
    
elif player[0] < cpu[0]:
    print("loss {0} < {1}".format(player[0], cpu[0]))
    cpu.append(cpu[0])
    cpu.append(player[0])
    del cpu[0]
    del player[0]

