import random
import time
import sys

import chapter_three as three

import player as pl
import player_party as pp
import player_flags as pf
import game_status as g

def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./90)


def chtwo():
    pf.player_flag.hiding = False
    pf.player_flag.bridge = False
    pf.player_flag.meet_pig = False
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    slowprint("----------------------")
    slowprint("C H A P T E R   T W O ")
    slowprint("----------------------")

    time.sleep(2)

    flag = True

    if pl.player.ducky:
        weapon = "ducky"

    elif pl.player.sword:
        weapon = "sword"

    elif pl.player.wand:
        weapon = "wand"

    elif pl.player.duck:
        weapon = "duck"

    else:
        slowprint("You shouldn't have gotten this far ... but ok.")
        weapon = "nothing"

    print("You continue moving forward with your", weapon, "in hand.")
    slowprint("You come across a river in front of you and a mountain to your left ... Which way do you want to go?")
    path = input()
    if "riv" in path:
        river(weapon)
    elif "mou" in path or "left" in path:
        mountain(weapon)

    else:
        slowprint("Pick a good choice...")


def mountain(weapon):
    pighurt = False
    if pf.player_flag.meet_pig == False:
        pf.player_flag.meet_pig = True
        slowprint("You start moving toward the mountains.")
        slowprint("As you proceed you hear squealing in the distance in front of you.")
        print("Right now you have a", weapon, " in your hands ... ")
        time.sleep(1.2)
        slowprint("Do you wanna charge with all the wrath of thor, or hide in the bushes next to you?")
        cho = input()
        if "cha" in cho:
            slowprint("You charge forward and find a pig ... NEAT")
            if "swo" in weapon or "wan" in weapon or "ducky" in weapon:
                slowprint("unfortunately you pieced into it ... ya know cause of your")
                print(weapon)
                pighurt = True

            elif weapon == "duck":
                slowprint("Thankfully because you have a useless duck for a weapon")
                slowprint("It didn't hurt the pig!")

        elif "hid" in cho:
            pf.player_flag.hiding = True
            slowprint("You hide in the bushes next to you.")
            slowprint("A few moments later you see a pig walking past ... NEAT!")
            slowprint("Do you wanna inspect the pig or stay hiding?")
            cho = input()
            if "hid" in cho:
                slowprint("The pig goes on and disappears into thin air ... ")
                pp.party.pig = False
                slowprint(" ... I suppose it was nothing.")
                slowprint("You continue on the path but there's nowhere else to go.")
                slowprint("It's a dead end and so you decide to go back to the river.")
                if pf.player_flag.bridge == True:
                    slowprint("You go across the bridge and continue on your way.")
                    return None
                    flag = False


                elif pf.player_flag.bridge == False:
                    river(weapon)

            elif "ins" in cho:
                pf.player_flag.hiding = False
                slowprint("You come out of the bushes and meet the pig.")
                slowprint("'AH YOU STARTLED ME' the pig squealed.")
                slowprint("'Are you ... inspecting me? ... NEAT :D'")
                slowprint("'I was just on my way to see the wizard I belonged to before running away.'")
                slowprint("'He's just across the river'")
                slowprint("'Do you wanna come with me?'")

                cho = input()
                if "y" in cho:
                    slowprint("'ALRIGHT! LET'S GO!!!'")
                    slowprint("You gained a pig into your party! WOOT")
                    slowprint("You both head off to the wizrds house across the river!")
                    pp.party.pig = True
                    return None
                    flag = False


                if "n" in cho:
                    slowprint("'ok ... well I'll see you later! ... weirdo ...'")
                    slowprint("You continue on the path but there's nowhere else to go.")
                    slowprint("It's a dead end and so you decide to go back to the river.")
                    pp.party.pig = False
                    if pf.player_flag.bridge == True:
                        slowprint("You go across the bridge and continue on your way.")
                        return None
                        flag = False


                    elif pf.player_flag.bridge == False:
                        river(weapon)



        if pighurt == True:
            slowprint("The pig started crying and squeals, ")
            slowprint("'PLEASE ... I'M IN SO MUCH PAIN! PLEASE END ME!!!'")
            slowprint("Do you want to end him?")
            cho = input()
            if "y" in cho:
                if weapon == "ducky":
                    slowprint("You hold up the ducky and rays of light shine down from heaven.")
                    slowprint("The pig looks up at you and as he closes his eyes says '... thank you ...'")
                    slowprint("A few moments pass")
                    for i in range(3):
                        print("...")
                        time.sleep(1.2)
                    slowprint("The pig starts to heal ... HE'S OK!!!")
                    pf.player_flag.pig_heal = True
                    slowprint("'Thank you for saving me! I thought I was a goner!!!")
                    slowprint("I belonged to a wizard before I ran away. He's across the river!")
                    slowprint("Do you wanna go see him?'")
                    cho = input()
                    if "y" in cho:
                        slowprint("'ALRIGHT! LET'S GO!!!'")
                        slowprint("You gained a pig into your party! WOOT")
                        slowprint("You both head off to the wizrds house across the river!")
                        pp.party.pig = True
                        return None
                        flag = False


                    if "n" in cho:
                        slowprint("ok ... well I'll see you later!")
                        slowprint("You continue on the path but there's nowhere else to go.")
                        slowprint("It's a dead end and so you decide to go back to the river.")
                        pp.party.pig = False
                        if pf.player_flag.bridge == True:
                            slowprint("You go across the bridge and continue on your way.")
                            return None
                            flag = False


                        elif pf.player_flag.bridge == False:
                            river(weapon)


                elif "swo" in weapon:
                    slowprint("You cut into the pig and with one last squeal ... he dies.")
                    slowprint("On the bright side you obtained bacon and pork chops!! DOO DOO DOO DOOOOOOOO")
                    pl.inv.pork = 1
                    pp.party.pig = False
                    print("")
                    slowprint("You continue on the path but there's nowhere else to go.")
                    slowprint("It's a dead end and so you decide to go back to the river.")
                    if pf.player_flag.bridge == True:
                        slowprint("You go across the bridge and continue on your way.")
                        return None
                        flag = False

                    elif pf.player_flag.bridge == False:
                        river(weapon)


                elif "wan" in weapon:
                    slowprint("You don't quite know how this thing works ... so here goes nothing!")
                    magic = random.randint(1,3)
                    if magic == 3:
                        slowprint("You wave your wand and the pig was miraculously healed!!!")
                        pf.player_flag.pig_heal = True
                        slowprint("'Thank you for saving me! I thought I was a goner!!!")
                        slowprint("I belonged to a wizard before I ran away. He's across the river!")
                        slowprint("Do you wanna go see him?'")
                        cho = input()
                        if "y" in cho:
                            slowprint("'ALRIGHT! LET'S GO!!!'")
                            slowprint("You gained a pig into your party! WOOT")
                            slowprint("You both head off to the wizrds house across the river!")
                            pp.party.pig = True
                            return None
                            flag = False


                    elif magic ==2:
                        slowprint("You wave the wand and turn the pig into ... some kind of mush ... I guess you did the job?")
                        slowprint("You continue on the path but there's nowhere else to go.")
                        slowprint("It's a dead end and so you decide to go back to the river.")
                        pp.party.pig = False
                        if pf.player_flag.bridge == True:
                            slowprint("You go across the bridge and continue on your way.")
                            return None
                            flag = False


                        elif pf.player_flag.bridge == False:
                            river(weapon)

                    elif magic ==1:
                        pp.party.pig = False
                        slowprint("You wave the wand and the pig explodes! You take 1 damage from the recoil.")
                        pl.player.health -= 1
                        print("HEALTH: ", pl.player.health)
                        if pl.player.health < 1:
                            g.game_over()
                            sys.exit()
                        slowprint("You continue on the path but there's nowhere else to go.")
                        slowprint("It's a dead end and so you decide to go back to the river.")
                        if pf.player_flag.bridge == True:
                            slowprint("You go across the bridge and continue on your way.")
                            return None
                            flag = False


                        elif pf.player_flag.bridge == False:
                            river(weapon)

            elif "n" in cho:
                pp.party.pig = False
                slowprint("The pig starts to bleed out and looks at you with tears in his eyes")
                slowprint("You couldn've ended his misery but instead you just watched him suffer.")
                for i in range(3):
                    print("...")
                    time.sleep(1)
                slowprint("Oh well.")
                slowprint("You continue on the path but there's nowhere else to go.")
                slowprint("It's a dead end and so you decide to go back to the river.")
                if pf.player_flag.bridge == True:
                    slowprint("You go across the bridge and continue on your way.")
                    return None
                    flag = False


                elif pf.player_flag.bridge == False:
                    river(weapon)

        elif pighurt == False and pf.player_flag.hiding == False:
            slowprint("The pig turns to you and squeals")
            pp.party.pig = False
            slowprint("'I'm so glad that's a rubber duck ...")
            slowprint("You could've killed me!'")
            slowprint("The pig turns around kicks you in the spleen and waddles away toward the river then vanishes.")
            pl.player.health -= 1
            print("HEALTH : ", pl.player.health)
            if pl.player.health < 1:
                g.game_over()
                sys.exit()
            slowprint("You continue on the path but there's nowhere else to go.")
            slowprint("It's a dead end and so you decide to go back to the river.")
            if pf.player_flag.bridge == True:
                slowprint("You go across the bridge and continue on your way.")
                return None
                flag = False


            elif pf.player_flag.bridge == False:
                river(weapon)

    else:
        slowprint("You make your way back to the river.")
        river(weapon)




def river(weapon):
    slowprint("You move toward the river and you don't see a bridge? Do you wanna try crossing anyways or look for a bridge?")
    path = input()
    if "cro" in path:
        cro = random.randint(1,5)
        suc = random.randint(1,3)
        slowprint("You try crossing the river")
        for i in range(3):
            print("...")
            time.sleep(1.2)
        if suc >= cro:
            slowprint("You have succeeded in crossing the river!")
            slowprint("You look to your right and you see a bridge ... oh well.")
            if pf.player_flag.meet_pig == False:
                slowprint("You march forward on the path when you hear squealing of some sort to the mountains.")
                slowprint("Do you want to go back and investigate?")
                path = input()
                if "y" in path or "su" in path:
                    slowprint("Did you want to cross the river again or use the bridge?")
                    path = input()
                    if "cro" in path or "riv" in path:
                        cro = random.randint(1,5)
                        suc = random.randint(1,3)
                        slowprint("You try crossing the river")
                        for i in range(3):
                            print("...")
                            time.sleep(1.2)
                        if suc >= cro:
                            slowprint("You have succeeded in crossing the river!")
                            mountain(weapon)

                        elif suc < cro:
                            slowprint("You were swept away by the river you lose 1 health and wash up near the mountains.")
                            pl.player.health -= 1
                            print("Health: ", pl.player.health)
                            if pl.player.health < 1:
                                g.game_over()
                                sys.exit()
                            mountain(weapon)

                elif "n" in path:
                    slowprint("Eh ... it was probably nothing anyways.")
                    slowprint("You continue on your way.")
                    return None

            else:
                slowprint("You continue on your journey and await new adventure!")
                return None
                flag = False


        elif suc < cro:
            slowprint("You were swept away by the river you lose 1 health and wash up near the mountains.")
            pl.player.health -= 1
            print("Health: ", pl.player.health)
            if pl.player.health < 1:
                g.game_over()
                sys.exit()
            mountain(weapon)

        else:
            slowprint("ABORT")

    elif "brid" in path:
        blind = random.randint(1,5)
        good = random.randint(1,4)
        if good >= blind:
            slowprint("You look to your right and see a bridge! HOORAY!")
            pf.player_flag.bridge = True
            if pf.player_flag.meet_pig == False:
                slowprint("You cross the bridge and then you hear squealing coming from the mountains")
                slowprint("Do you want to investigate?")
                path = input()

                if "y" in path or "su" in path:
                    slowprint("You go back across the bridge and head toward the mountains")
                    mountain(weapon)

                elif "n" in path:
                    slowprint("Eh, it was probably nothing anyways.")
                    return None

                    flag = False
            else:
                slowprint("You continue on your journey and await new adventure!")
                return None
                flag = False



        elif good < blind:
            slowprint("You do not see a bridge... did you wanna cross the river?")
            path = input()
            if "y" or "su" in path:
                cro = random.randint(1,5)
                suc = random.randint(1,3)
                slowprint("You try crossing the river")
                for i in range(3):
                    print("...")
                    time.sleep(1.2)
                if suc >= cro:
                    slowprint("You have succeeded in crossing the river!")
                    slowprint("You look to your right and you see a bridge ... oh well.")
                    slowprint("You march forward on the path when you hear squealing of some sort to the mountains.")
                    slowprint("Do you want to go back and investigate?")
                    path = input()
                    if "y" in path or "su" in path:
                        slowprint("Did you want to cross the river again or use the bridge?")
                        path = input()
                        if "cro" in path or "riv" in path:
                            cro = random.randint(1,5)
                            suc = random.randint(1,3)
                            slowprint("You try crossing the river")
                            for i in range(3):
                                print("...")
                                time.sleep(1.2)
                            if suc >= cro:
                                slowprint("You have succeeded in crossing the river!")

                            elif suc < cro:
                                slowprint("You were swept away by the river you lose 1 health and wash up near the mountains.")
                                pl.player.health -= 1
                                print("Health: ", pl.player.health)
                                if pl.player.health < 1:
                                    g.game_over()
                                    sys.exit()
                                mountain(weapon)

                    elif "n" in path:
                        slowprint("Eh, it was probably nothing anyways.")
                        # three.chthree()
                        return None

                elif suc < cro:
                    slowprint("You were swept away by the river you lose 1 health and wash up near the mountains.")
                    pl.player.health -= 1
                    print("Health: ", pl.player.health)
                    if pl.player.health < 1:
                        g.game_over()
                        sys.exit()
                    mountain(weapon)
