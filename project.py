# Author: CMOB 2/10/2022

from time import sleep
player = [2,13,14,5,4]
cpu = [2,2,9,10,2]

if player[0] == cpu[0]:
    print("WAR")
    print("drawing three additional cards")

    if player[4] > cpu[4]:
        print("victory {0} > {1}".format(player[4], cpu[4])); sleep(2)
        print("You won:{0} and {1}".format(player[:4],cpu[:4]))
        for i, v in enumerate(player):
            if i < 4:
                player.append(player[v])
        for i, v in enumerate(cpu):
            if i < 4:
                    player.append(cpu[v])
        del player[:4]
        del cpu[:4]

    if player[4] < cpu[4]:
        print("defeat {0} < {1}".format(player[4], cpu[4])); sleep(2)
        print("Cpu won:{0} and {1}".format(player[:4],cpu[:4]))
        for i, v in enumerate(player):
                if i < 4:
                    cpu.append(player[v])
        for i, v in enumerate(cpu):
            if i < 4:
                cpu.append(cpu[v])
        del player[:4]
        del cpu[:4]

    if player[4] == cpu[4]:
        print("WAR"); sleep(2)
        print("drawing three more cards")

        if player[8] > cpu[8]:
            print("victory {0} > {1}".format(player[8], cpu[8])); sleep(2)
            print("You won:{0} and {1}".format(player[:8],cpu[:8]))
            for i, v in enumerate(player):
                if i < 8:
                    player.append(player[v])
            for i, v in enumerate(cpu):
                if i < 8:
                    player.append(cpu[v])
            del player[:8]
            del cpu[:8]
            
        if player[8] < cpu[8]:
            print("defeat {0} < {1}".format(player[8], cpu[8])); sleep(2)
            print("Cpu won:{0} and {1}".format(player[:8],cpu[:8]))
            for i, v in enumerate(player):
                if i < 8:
                    cpu.append(player[v])
            for i, v in enumerate(cpu):
                if i < 8:
                    cpu.append(cpu[v])
            del player[:8]
            del cpu[:8]

        if player[8] == cpu[8]:
            print("WAR"); sleep(2)
            print("drawing three more cards")


            if player[12] < cpu[12]:
                print("defeat {0} < {1}".format(player[12], cpu[12])); sleep(2)
                print("Cpu won:{0} and {1}".format(player[:12],cpu[:12]))
                for i, v in enumerate(player):
                    if i < 12:
                        cpu.append(player[v])
                    for i, v in enumerate(cpu):
                        if i < 12:
                            cpu.append(cpu[v])
                        del player[:12]
                        del cpu[:12]

            if player[12] > cpu[12]:
                print("victory {0} > {1}".format(player[12], cpu[12])); sleep(2)
                print("You won:{0} and {1}".format(player[:12],cpu[:12]))
                for i, v in enumerate(player):
                    if i < 12:
                        player.append(player[v])
                for i, v in enumerate(cpu):
                    if i < 12:
                        player.append(cpu[v])
                del player[:12]
                del cpu[:12]
                
            if player[12] == cpu[12]:
                print("WAR"); sleep(2)
                print("drawing three additional cards")

                if player[16] < cpu[16]:
                    print("defeat {0} < {1}".format(player[16], cpu[16])); sleep(2)
                    print("Cpu won:{0} and {1}".format(player[:16],cpu[:16]))
                    for i, v in enumerate(player):
                        if i < 16:
                            cpu.append(player[v])
                    for i, v in enumerate(cpu):
                        if i < 16:
                            cpu.append(cpu[v])
                    del player[:16]
                    del cpu[:16]

                if player[16] > cpu[16]:
                    print("victory {0} > {1}".format(player[16], cpu[16])); sleep(2)
                    print("You won:{0} and {1}".format(player[:16],cpu[:16]))
                    for i, v in enumerate(player):
                        if i < 16:
                            player.append(player[v])
                    for i, v in enumerate(cpu):
                        if i < 16:
                            player.append(cpu[v])
                    del player[:16]
                    del cpu[:16]
               
                if player[16] == cpu[16]:
                    print("WAR"); sleep(2)
                    print("drawing three additional cards")
                    
                    if player[20] < cpu[20]:
                        print("defeat {0} < {1}".format(player[20], cpu[20])); sleep(2)
                        print("Cpu won:{0} and {1}".format(player[:20],cpu[:20]))
                        for i, v in enumerate(player):
                            if i < 20:
                                cpu.append(player[v])
                        for i, v in enumerate(cpu):
                            if i < 20:
                                cpu.append(cpu[v])
                        del player[:20]
                        del cpu[:20]

                    if player[20] > cpu[20]:
                        print("victory {0} > {1}".format(player[20], cpu[20])); sleep(2)
                        print("You won:{0} and {1}".format(player[:20],cpu[:20]))
                        for i, v in enumerate(player):
                            if i < 20:
                                player.append(player[v])
                        for i, v in enumerate(cpu):
                            if i < 20:
                                player.append(cpu[v])
                        del player[:20]
                        del cpu[:20]
              
                    if player[20] == cpu[20]:
                        print("WAR"); sleep(2)
                        print("drawing three additional cards")

                        if player[24] < cpu[24]:
                            print("defeat {0} < {1}".format(player[24], cpu[24])); sleep(2)
                            print("Cpu won:{0} and {1}".format(player[:24],cpu[:24]))
                            for i, v in enumerate(player):
                                if i < 24:
                                    cpu.append(player[v])
                            for i, v in enumerate(cpu):
                                if i < 24:
                                    cpu.append(cpu[v])
                            del player[:24]
                            del cpu[:24]

                        if player [24] > cpu[24]:
                            print("victory {0} > {1}".format(player[24], cpu[24])); sleep(2)
                            print("You won:{0} and {1}".format(player[:24],cpu[:24]))
                            for i, v in enumerate(player):
                                if i < 24:
                                    player.append(player[v])
                            for i, v in enumerate(cpu):
                                if i < 24:
                                    player.append(cpu[v])
                            del player[:24]
                            del cpu[:24]
                
                        if player[24] == cpu[24]:
                            print("WAR"); sleep(2)
                            print("drawing three additional cards")

                            if player[26] < cpu[26]:
                                print("defeat {0} < {1}".format(player[26], cpu[26])); sleep(2)
                                print("Cpu won:{0} and {1}".format(player[:26],cpu[:26]))
                                for i, v in enumerate(player):
                                    if i < 26:
                                        cpu.append(player[v])
                                for i, v in enumerate(cpu):
                                    if i < 26:
                                        cpu.append(cpu[v])
                                del player[:26]
                                del cpu[:26]

                            if player[26] > cpu[26]:
                                print("victory {0} > {1}".format(player[26], cpu[26])); sleep(2)
                                print("You won:{0} and {1}".format(player[:26],cpu[:26]))
                                for i, v in enumerate(player):
                                    if i < 26:
                                        player.append(player[v])
                                for i, v in enumerate(cpu):
                                    if i < 26:
                                        player.append(cpu[v])
                                del player[:26]
                                del cpu[:26]
                
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

