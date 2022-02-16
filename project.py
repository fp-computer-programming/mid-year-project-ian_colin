# Author: CMOB 2/10/2022

from time import sleep
player = [2,13,14,5,4]
cpu = [2,2,9,10,2]

if player[0] > cpu[0]:
    print("victory {0} > {1}".format(player[0], cpu[0]))

    player.append(player[0])
    player.append(cpu[0])

    del player[0]
    del cpu[0]
    
    
if player[0] < cpu[0]:
    print("loss {0} < {1}".format(player[0], cpu[0]))

    cpu.append(cpu[0])
    cpu.append(player[0])
    
    del cpu[0]
    del player[0]


if player[0] == cpu[0]:
    print("WAR"); sleep(2)
    print("drawing three additional cards")

    if player[4] > cpu[4]:
        print("victory {0} > {1}".format(player[4], cpu[4])); sleep(2)
        print("You won:{0} and {1}".format(player[:4],cpu[:4]))

        player.extend(player[0:5])
        player.extend(cpu[0:5])

        del player[:4]
        del cpu[:4]

        continue

    if player[4] < cpu[4]:
        print("defeat {0} < {1}".format(player[4], cpu[4])); sleep(2)
        print("Cpu won:{0} and {1}".format(player[:4],cpu[:4]))

        cpu.extend(player[0:5])
        cpu.extend(cpu[0:5])

        del player[:4]
        del cpu[:4]

        continue

    if player[4] == cpu[4]:
        print("WAR"); sleep(2)
        print("drawing three more cards")

        if player[8] > cpu[8]:
            print("victory {0} > {1}".format(player[8], cpu[8])); sleep(2)
            print("You won:{0} and {1}".format(player[:8],cpu[:8]))

            player.extend(player[0:9])
            player.extend(cpu[0:9])

            del player[:8]
            del cpu[:8]

            continue
            
        if player[8] < cpu[8]:
            print("defeat {0} < {1}".format(player[8], cpu[8])); sleep(2)
            print("Cpu won:{0} and {1}".format(player[:8],cpu[:8]))

            cpu.extend(player[0:9])
            cpu.extend(cpu[0:9])

            del player[:8]
            del cpu[:8]

            continue

        if player[8] == cpu[8]:
            print("WAR"); sleep(2)
            print("drawing three more cards")


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
                
            if player[12] == cpu[12]:
                print("WAR"); sleep(2)
                print("drawing three additional cards")

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
               
                if player[16] == cpu[16]:
                    print("WAR"); sleep(2)
                    print("drawing three additional cards")
                    
                    if player[20] < cpu[20]:
                        print("defeat {0} < {1}".format(player[20], cpu[20])); sleep(2)
                        print("Cpu won:{0} and {1}".format(player[:20],cpu[:20]))

                        cpu.extend(player[0:21])
                        cpu.extend(cpu[0:21])

                        del player[:20]
                        del cpu[:20]

                    if player[20] > cpu[20]:
                        print("victory {0} > {1}".format(player[20], cpu[20])); sleep(2)
                        print("You won:{0} and {1}".format(player[:20],cpu[:20]))

                        player.extend(player[0:21])
                        player.extend(cpu[0:21])

                        del player[:20]
                        del cpu[:20]
              
                    if player[20] == cpu[20]:
                        print("WAR"); sleep(2)
                        print("drawing three additional cards")

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
                
                        if player[24] == cpu[24]:
                            print("WAR"); sleep(2)
                            print("drawing three additional cards")

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

                            if player[26] == cpu[26]:
                                print("woops! we ran out of cards, let's just skip that then")
                                continue
                
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

