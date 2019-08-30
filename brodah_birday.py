import random
import time
import sys

def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./90)

def player_flag():
    global bridge
    global hiding
    global meet_pig

def party():
    global pig
    global mempha

def player():
    global ducky
    global sword
    global wand
    global duck
    global health
    global name
    global level
    global gold


def stats():
    print("Name ", name)
    print("Weapon")

def intro():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    slowprint("----------------------")
    slowprint("C H A P T E R   O N E ")
    slowprint("----------------------")

    name = input("\nWhat is your name:\n")
    if "jon" in name.lower() or "oo" in name.lower() or "ok" in name.lower() or "oy" in name.lower() or "bro" in name.lower():
        slowprint("BRODAH!!! I HAVE PLANS FOR YOU!!!")
        brodah = True

    # else:
    #     slowprint("Alrighty! ")
    #     print(name)

    else:
        slowprint("Sorry, either you didn't take this seriously enough or you're not brodah")
        slowprint("Soooooo yeah, see ya ...")
        time.sleep(2)
        game_over()
        slowprint("You weren't cool enough to play yo")
        time.sleep(2)
        sys.exit()

    adv = input("Are you ready for an adventure? : ")
    if "y" in adv.lower():
        return name

    elif "n" in adv.lower():
        slowprint("Oh ... ok")
        game_over()
        slowprint("Guess you were too cool to play :(")
        time.sleep(2)
        sys.exit()

    else:
        slowprint("I don't think you answered right ... but you meant yes right!? :D")
        time.sleep(2)
        return name

def chapter_two():
    player_flag.hiding = False
    player_flag.bridge = False
    player_flag.meet_pig = False
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    slowprint("----------------------")
    slowprint("C H A P T E R   T W O ")
    slowprint("----------------------")

    time.sleep(2)

    flag = True

    if player.ducky:
        weapon = "ducky"

    elif player.sword:
        weapon = "sword"

    elif player.wand:
        weapon = "wand"

    elif player.duck:
        weapon = "duck"

    else:
        slowprint("You shouldn't have gotten this far ... but ok.")
        weapon = "nothing"

    while flag == True:
        print("You continue moving forward with your", weapon, "in hand.")
        slowprint("You come across a river in front of you and a mountain to your left ... Which way do you want to go?")
        path = input()
        if "riv" in path:
            river(weapon)
        elif "mou" in path or "left" in path:
            mountain(weapon)

        else:
            slowprint("Pick a good choice...")


def chapter_three():
    slowprint("")
    print("\n\n\n________________________________________________________________________________")
    print("                           C O M I N G    S O O N")
    print("________________________________________________________________________________\n\n\n")

    time.sleep(3)

def mountain(weapon):
    pighurt = False
    if player_flag.meet_pig == False:
        player_flag.meet_pig = True
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
            player_flag.hiding = True
            slowprint("You hide in the bushes next to you.")
            slowprint("A few moments later you see a pig walking past ... NEAT!")
            slowprint("Do you wanna inspect the pig or stay hiding?")
            cho = input()
            if "hid" in cho:
                slowprint("The pig goes on and disappears into thin air ... ")
                slowprint(" ... I suppose it was nothing.")
                slowprint("You continue on the path but there's nowhere else to go.")
                slowprint("It's a dead end and so you decide to go back to the river.")
                if player_flag.bridge == True:
                    slowprint("You go across the bridge and continue on your way.")
                    chapter_three()
                    flag = False
                    sys.exit()

                elif player_flag.bridge == False:
                    river(weapon)

            elif "ins" in cho:
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
                    chapter_three()
                    flag = False
                    sys.exit()

                if "n" in cho:
                    slowprint("'ok ... well I'll see you later! ... weirdo ...'")
                    slowprint("You continue on the path but there's nowhere else to go.")
                    slowprint("It's a dead end and so you decide to go back to the river.")
                    if player_flag.bridge == True:
                        slowprint("You go across the bridge and continue on your way.")
                        chapter_three()
                        flag = False
                        sys.exit()

                    elif player_flag.bridge == False:
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
                    slowprint("'Thank you for saving me! I thought I was a goner!!!")
                    slowprint("I belonged to a wizard before I ran away. He's across the river!")
                    slowprint("Do you wanna go see him?'")
                    cho = input()
                    if "y" in cho:
                        slowprint("'ALRIGHT! LET'S GO!!!'")
                        slowprint("You gained a pig into your party! WOOT")
                        slowprint("You both head off to the wizrds house across the river!")
                        chapter_three()
                        flag = False
                        sys.exit()

                    if "n" in cho:
                        slowprint("ok ... well I'll see you later!")
                        slowprint("You continue on the path but there's nowhere else to go.")
                        slowprint("It's a dead end and so you decide to go back to the river.")
                        if player_flag.bridge == True:
                            slowprint("You go across the bridge and continue on your way.")
                            chapter_three()
                            flag = False
                            sys.exit()

                        elif player_flag.bridge == False:
                            river(weapon)


                elif "swo" in weapon:
                    slowprint("You cut into the pig and with one last squeal ... he dies.")
                    slowprint("On the bright side you obtained bacon and pork chops!! DOO DOO DOO DOOOOOOOO")
                    print("")
                    slowprint("You continue on the path but there's nowhere else to go.")
                    slowprint("It's a dead end and so you decide to go back to the river.")
                    if player_flag.bridge == True:
                        slowprint("You go across the bridge and continue on your way.")
                        chapter_three()
                        flag = False
                        sys.exit()
                    elif player_flag.bridge == False:
                        river(weapon)


                elif "wan" in weapon:
                    slowprint("You don't quite know how this thing works ... so here goes nothing!")
                    magic = random.randint(1,3)
                    if magic == 3:
                        slowprint("You wave your wand and the pig was miraculously healed!!!")
                        slowprint("'Thank you for saving me! I thought I was a goner!!!")
                        slowprint("I belonged to a wizard before I ran away. He's across the river!")
                        slowprint("Do you wanna go see him?'")
                        cho = input()
                        if "y" in cho:
                            slowprint("'ALRIGHT! LET'S GO!!!'")
                            slowprint("You gained a pig into your party! WOOT")
                            slowprint("You both head off to the wizrds house across the river!")
                            chapter_three()
                            flag = False
                            sys.exit()

                    elif magic ==2:
                        slowprint("You wave the wand and turn the pig into ... some kind of mush ... I guess you did the job?")
                        slowprint("You continue on the path but there's nowhere else to go.")
                        slowprint("It's a dead end and so you decide to go back to the river.")
                        if player_flag.bridge == True:
                            slowprint("You go across the bridge and continue on your way.")
                            chapter_three()
                            flag = False
                            sys.exit()

                        elif player_flag.bridge == False:
                            river(weapon)

                    elif magic ==1:
                        slowprint("You wave the wand and the pig explodes! You take 1 damage from the recoil.")
                        player.health -= 1
                        print("HEALTH: ", player.health)
                        if player.health < 1:
                            game_over()
                            sys.exit()
                        slowprint("You continue on the path but there's nowhere else to go.")
                        slowprint("It's a dead end and so you decide to go back to the river.")
                        if player_flag.bridge == True:
                            slowprint("You go across the bridge and continue on your way.")
                            chapter_three()
                            flag = False
                            sys.exit()

                        elif player_flag.bridge == False:
                            river(weapon)

            elif "n" in cho:
                slowprint("The pig starts to bleed out and looks at you with tears in his eyes")
                slowprint("You couldn've ended his misery but instead you just watched him suffer.")
                for i in range(3):
                    print("...")
                    time.sleep(1)
                slowprint("Oh well.")
                slowprint("You continue on the path but there's nowhere else to go.")
                slowprint("It's a dead end and so you decide to go back to the river.")
                if player_flag.bridge == True:
                    slowprint("You go across the bridge and continue on your way.")
                    chapter_three()
                    flag = False
                    sys.exit()

                elif player_flag.bridge == False:
                    river(weapon)

        elif pighurt == False and player_flag.hiding == False:
            slowprint("The pig turns to you and squeals")
            slowprint("'I'm so glad that's a rubber duck ...")
            slowprint("You could've killed me!'")
            slowprint("The pig turns around kicks you in the spleen and waddles away toward the river then vanishes.")
            player.health -= 1
            if player.health < 1:
                game_over()
                sys.exit()
            slowprint("You continue on the path but there's nowhere else to go.")
            slowprint("It's a dead end and so you decide to go back to the river.")
            if player_flag.bridge == True:
                slowprint("You go across the bridge and continue on your way.")
                chapter_three()
                flag = False
                sys.exit()

            elif player_flag.bridge == False:
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
            if player_flag.meet_pig == False:
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
                            player.health -= 1
                            print("Health: ", player.health)
                            if player.health < 1:
                                game_over()
                                sys.exit()
                            mountain(weapon)

                elif "n" in path:
                    slowprint("Eh ... it was probably nothing anyways.")
                    slowprint("You continue on your way.")
            else:
                slowprint("You continue on your journey and await new adventure!")
                chapter_three()
                flag = False
                sys.exit()

        elif suc < cro:
            slowprint("You were swept away by the river you lose 1 health and wash up near the mountains.")
            player.health -= 1
            print("Health: ", player.health)
            if player.health < 1:
                game_over()
                sys.exit()
            mountain(weapon)

        else:
            slowprint("ABORT")

    elif "brid" in path:
        blind = random.randint(1,5)
        good = random.randint(1,4)
        if good >= blind:
            slowprint("You look to your right and see a bridge! HOORAY!")
            player_flag.bridge = True
            if player_flag.meet_pig == False:
                slowprint("You cross the bridge and then you hear squealing coming from the mountains")
                slowprint("Do you want to investigate?")
                path = input()

                if "y" in path or "su" in path:
                    slowprint("You go back across the bridge and head toward the mountains")
                    mountain(weapon)

                elif "n" in path:
                    slowprint("Eh, it was probably nothing anyways.")
                    chapter_three()
                    flag = False
                    sys.exit()
            else:
                slowprint("You continue on your journey and await new adventure!")
                chapter_three()
                flag = False
                sys.exit()


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
                                player.health -= 1
                                print("Health: ", player.health)
                                if player.health < 1:
                                    game_over()
                                    sys.exit()
                                mountain(weapon)
                elif suc < cro:
                    slowprint("You were swept away by the river you lose 1 health and wash up near the mountains.")
                    player.health -= 1
                    print("Health: ", player.health)
                    if player.health < 1:
                        game_over()
                        sys.exit()
                    mountain(weapon)

def story_wake_up(name):
    flag = True
    player.sword = False
    player.wand = False
    player.duck = False
    player.ducky = False
    player.health = 3
    tree_life = 0
    sword_try = False
    wand_try = False
    duck_try = False
    ducky_try = False

    slowprint("\nYou wake up in the middle of a forest. Before you, you see a sword \
lodged into a stump, a wand growing as part of a tree, and a rubber ducky with sunglasses.")
    sword_stubborn = random.randint(1,7)

    while(flag):
        if player.health <=0:
            game_over()
            sys.exit()

        elif sword_try == True and wand_try == True and ducky_try == True and duck_try == True:
            slowprint("Wow ... how unlucky, you actually missed all of them.")
            slowprint("That is one of the most statistically amazing thing I have ever seen")
            slowprint("There is nothing left for you to do ... You actually have nothing.")
            slowprint("Well ... I guess that's a game over ... (Give it a second)")
            flag = False
            time.sleep(2)
            game_over()
            sys.exit()

        weapon = input("\nWhich do you want to grab? (Sword/Wand/Duck (ducky))\n")


        if weapon.lower() == "ducky" and ducky_try == True:
            slowprint("YOU WERE ALREADY DEEMED UNWORTHY LEAVE HIM BE!!!")

        elif "sw" in weapon.lower() and player.health < 3:
            sw_choice = input("Are you sure? It feels like it was sucking the life out of you.\n")
            if "y" in sw_choice:
                swordWorth = random.randint(1,6)
                sword_stubborn -= 1
                if swordWorth > sword_stubborn:
                    slowprint("\nYou pull the sword out and you wield it triumphantly feeling as epic as a \
polar bear on fire riding a unicorn into the sunset!")
                    player.sword = True
                    time.sleep(1.2)
                    flag = False
                else:
                    slowprint("You feel the sword drawing life out of you, you lose 1 health and let go.")
                    player.health -= 1
                    sword = False
                    print("HEALTH: ", player.health)
                    flag = True
            elif "n" in sw_choice:
                slowprint("Yeah ... I thought so WIMP!")
                flag = True
            else:
                slowprint("... I'm gonna take that as a no.")
                flag = True

        elif "wa" in weapon.lower() and tree_life == 1:
            slowprint("'I WARNED YOU! NOW YOU'LL PAY!'")
            time.sleep(2)
            game_over()
            sys.exit()

        elif weapon.lower() == "sword" or "sw" in weapon.lower():
            sword_try = True
            swordWorth = random.randint(1,6)
            if swordWorth > sword_stubborn:
                slowprint("You pull the sword out and you wield it triumphantly feeling as epic as a \
polar bear on fire riding a unicorn into the sunset!")
                player.sword = True
                print(player.sword)
                flag = False
            else:
                slowprint("You feel the sword drawing life out of you, you lose 1 health and let go.")
                player.health -= 1
                sword = False
                print("HEALTH: ", player.health)
                flag = True

        elif weapon.lower() == "wand" or "wa" in weapon.lower():
            wand_choice = input("You approach the tree and it looks like you can break the wand off. Do you wanna try?\n")
            if "y" in wand_choice:
                wand_try = True
                tree_life = random.randint(1,2)
                if tree_life == 1:
                    slowprint("You try to break the wand off the tree and you hear a yelp.")
                    slowprint("The tree comes to life and starts talking to you.")
                    slowprint("\n" r"'Hey! Leave that alone! If you pull that out I will die!'")
                    slowprint(r"'Come in front of me and we can talk.'")
                    tree_choice = input("Do you want to face the talking tree?\n")
                    if "y" in tree_choice:
                        slowprint("\n" r"'Well thank you kindly. Sorry for yelling but that wand is the source of my life.")
                        slowprint(r"'Why were you trying to grab it?'")
                        slowprint("\n[1] : 'I don't actually know. It was in front of me and I wanted it.'")
                        slowprint("[2] : 'Forget you old hag, this wand is mine! *Proceed to rip the wand from the tree's branch*")
                        print("[3] : 'I'm sorry, my name is", name, " and I'm just a little lost")

                        choice = input("What do you want to say?\n")

                        if choice == '1':
                            choice = input("\n'Oh ... I see, so you just wanted to KILL ME!?'\n")
                            if "ye" in choice:
                                slowprint("\nOh ... ok, take my life, it's not like I need it or anything\n")
                                slowprint("You reach up and grab the wand and the tree is not letting go.")
                                slowprint("'YOU'LL GET THIS WAND FROM MY COLD DEAD BRANCHES!!!'")
                                choice = input("\n1 : 'Cold?'\n2 : 'Well ExCuUuUuSsEe mE pRiNcEsS!!!'\n 3 : 'Alright, I'm sorry, I thought you said I could have it!'\n")

                                if choice == '1':
                                    slowprint("\nYou set the tree on fire and listen to the screams of a burning tree.")
                                    slowprint("When the fire settles you pick up the wand and reflect about how proud you are of your clever pun.")
                                    player.wand = True
                                    flag = False
                                    time.sleep(2)
                                    break

                                elif choice == '2':
                                    slowprint("'... I don't understand what you're saying. Get away from me! If I see you again, I'll blast you with my wand!'")
                                    slowprint("You decided not to question that logic and turned around and walked away. Probably best not to go back.")
                                    player.wand = False


                                elif choice == '3':
                                    slowprint("'I WAS BEING SARCASTIC! Get away you little devil! If I see you again, I'll turn you into a sheep!'")
                                    slowprint("You decided not to question that logic and turned around and walked away. Probably best not to go back.")
                                    player.wand = False

                            elif "n" in choice:
                                tree_logic = random.randint(1,3)
                                if tree_logic == 3:
                                    slowprint("Hmmm, well I'm sure it was an accident so that's fine. Just please don't do it again.")
                                else:
                                    slowprint("'Well skiddadle before I turn you into an insect you bug!'")
                                    slowprint("You decided not to question that logic and turned around and walked away. Probably best not to go back.")
                                    player.wand = False

                            else:
                                slowprint(" ... I didn't understand what you just said ... BUT BEGONE DEMON!")
                                game_over()
                                slowprint("You probably should speak more clearly ...")
                                time.sleep(2)
                                sys.exit()

                        elif choice == '2':
                            slowprint("You proceed to rip the wand out of the tree and with a loud wail the tree dies.")
                            slowprint("*YOU RECEIVED A MAGIC WAND*")
                            player.wand = True
                            slowprint("You can feel the weight of your actions to acheive this item")
                            guilt = input("Do you feel guilty?")
                            if "y" in guilt:
                                slowprint("Yeah, that was a jerky move ... not like beef jerky though")
                                slowprint("Like ... Jerk jerky...")
                                time.sleep(1.4)
                                slowprint("Yeah, you're a jerk!")
                                break
                            elif "n" in guilt:
                                slowprint("Really? That was the only thing keeping the tree alive and you basically")
                                slowprint("literally and metaphorically ripped out its heart")
                                slowprint("Although you're right, its probably not worth it to worry over!")
                                time.sleep(1.4)
                                break

                            else:
                                slowprint("... I'm gonna take that as a no ...")
                                slowprint("Really? That was the only thing keeping the tree alive and you basically")
                                slowprint("literally and metaphorically ripped out its heart")
                                slowprint("Although you're right, its probably not worth it to worry over!")
                                break

                        elif choice == '3':
                            print("Oh really? Well", name, ", my name is Mempha and I suppose you didn't mean any harm...")
                            slowprint("1 : 'That's not what I said.'")
                            slowprint("2 : 'No I didn't know you were alive'")
                            slowprint("3 : *In your head* Huh ... That's some nice firewood ...")
                            choice = input("What do you do?")
                            if choice == "1":
                                slowprint("'What?'")
                                slowprint("\nYou proceed to bite into the tree with all the force of a thousand chipmunks")
                                slowprint("As you dig into her woody flesh, you snap the wand off of her branch")
                                slowprint("Slowly and painfully Mempha fades away into nothingness ... NEAT YOU GOT A WAND!")
                                player.wand = True
                                time.sleep(2)
                                break

                            elif choice == "2":
                                slowprint("Ok, well now you do. I'm afraid I can't give you my wand ... I'm very sorry.")
                                slowprint("[1] 'That's ok. You need it more than I do.'")
                                slowprint("[2] 'But I'm defensless... I'll die without it.'")
                                slowprint("[3] 'FORGET THAT YOU OLD BAG OF FIREWOOD! GIVE IT TO ME!!!!'")
                                cho = input()
                                if cho == "1" or "that" in cho.lower():
                                    slowprint("'You're darn tootin I do! Now scram before I explode yur mind!' ")

                                elif cho == "2" or "but" in cho.lower():
                                    slowprint("'Oh ... I suppose you have a point. I can't leave you all alone here ...")
                                    slowprint("Ok ... I will give you my wand. ... Just give me a minute.'")
                                    time.sleep(3)
                                    slowprint("'Ok ... here you go.'")
                                    slowprint("Do you want to continue?")
                                    cho = input()
                                    if "y" in cho.lower():
                                        player.wand = True
                                        slowprint("You breaks off the wand and hands it to you.")
                                        slowprint("You feel power surging through your body and as you look")
                                        slowprint("back at Mempha ... she is shrivaled up ...")
                                        slowprint("Do you want to try and bring her back to life?")
                                        cho = input()
                                        if "y" in cho.lower():
                                            slowprint("ok ... here goes nothing ...")
                                            magic = random.randint(1,3)
                                            if magic <= 1:
                                                slowprint("You cast a spell and the tree sprouts back to life")
                                                slowprint("Mempha opens her eyes in disbelief ...")
                                                slowprint("'You ... you saved me... Thank you so much! I won't forget this!'")
                                                time.sleep(1.3)
                                                break

                                            elif magic == 2:
                                                slowprint("You cast a spell and then nothing happens ... although you see a small spark")
                                                slowprint("You run out of the forest and then the whole forest goes up in flames")
                                                slowprint("... at least you got the wand ...")
                                                time.sleep(1.3)
                                                break

                                            elif magic == 3:
                                                slowprint("You cast a spell and then a new tree sprouts.")
                                                slowprint("The tree is full of life ... but Mempha is not there")
                                                slowprint("Then out of nowhere, a woman comes from behind the tree.")
                                                slowprint("'I ... I'm me again ... my husband turned me into a tree but ... I'm free! '")
                                                slowprint("'I won't forget this, see you later friend!'")
                                                slowprint("Mempha wanders away and disappears.")
                                                party.mempha = True
                                                time.sleep(2)
                                                break

                                        elif "n" in cho.lower():
                                            slowprint("You ponder and wave your arms, but in the end it's probably best not to try. You don't know how to control it.")
                                            slowprint("Then out of nowhere, a woman comes from behind the tree.")
                                            slowprint("'I ... I'm me again ... my husband turned me into a tree but ... I'm free! '")
                                            slowprint("'I won't forget this, see you later friend!'")
                                            slowprint("Mempha wanders away and disappears.")
                                            party.mempha = True
                                            break

                                    elif "n" in cho.lower():
                                        slowprint("'I'M GIVING YOU MY LIFE OUT OF THE KINDNESS OF MY HEART!")
                                        slowprint("AND YOU DARE REJECT IT!? DO YOU KNOW HOW HARD THIS WAS FOR ME!?")
                                        slowprint("FINE! YOU WON'T GET THE WAND! ENJOY BEING A BOWL OF SOUP!!!'")
                                        slowprint("She waves her wand and you feel noticablly shorter ... and wetter ... and soupier...")
                                        game_over()
                                        time.sleep(2.3)
                                        sys.exit()

                                elif cho == "3" or "for" in cho.lower():
                                    slowprint("You lunge forward to grab the wand but she waves it and turns you into a bag of firewood")
                                    slowprint("... ironic ... ")
                                    game_over()
                                    time.sleep(2)
                                    sys.exit()

                            elif choice == "3":
                                slowprint("You proceed to set poor Mempha on fire. although you also carelessly started a forest fire!")
                                slowprint("The whole forest is burning and then all at once the fire disappears")
                                slowprint("Everything is now frozen and you see that Mempha frozen with the wand in hand")
                                slowprint("She is completely defensless, but even you wouldn't dare desecrate her corpse")
                                slowprint("After the good she has done ... right?")
                                cho = input()
                                if "y" in cho.lower() or "righ" in cho.lower():
                                    slowprint("Awesome, best leave her alone.")
                                elif "n" in cho.lower() or "des" in cho.lower():
                                    slowprint(" ... You are a monster ... a very mean monster ...")
                                    player.wand = True
                                    slowprint("Congrats ... you got a wand ...")
                                    time.sleep(1.3)
                                    break

                    elif "n" in tree_choice:
                        slowprint("\n'Um excuse me ... What are you doing back there? ...'")
                        slowprint("1 : Rip the wand off the tree")
                        slowprint("2 : Walk away")
                        slowprint("3 : Mess with the clearly magical tree")
                        choice = input("What do you want to do?\n")

                        if choice == "1" or "rip" in choice.lower() or "take" in choice.lower():
                            slowprint("You slowly and painfully rip the wand off the tree.")
                            slowprint("The tree lets out a scream pleading for its life, but you've already made up your mind.")
                            slowprint("With one last yank, you feel a powerful surge cross your body.")
                            slowprint("One last screech lets out, and you have in your hands a wand.")
                            slowprint("You have obtained the wand")
                            player.wand = True
                            flag = False
                            time.sleep(3)
                            break

                        elif choice == "2" or "walk" in choice.lower():
                            slowprint("'YOU COME BACK HERE AND FACE ME LIKE A MORTAL YOU INSECT!'")
                            slowprint("'I BETTER NOT SEE YOU AGAIN!'")
                            time.sleep(2)

                        elif choice == "3" or "mess" in choice.lower():
                            slowprint("You start poking the tree with it's own branches mocking it.")
                            slowprint("You demand the tree stop hitting itself and the tree clearly upset")
                            slowprint("spontaneously combusts into flames and explodes.")
                            slowprint("Suddenly it explodes and you lose 1 health")
                            player.health -= 1
                            print("HEALTH:", player.health)
                            if player.health < 1:
                                game_over()
                                sys.exit()
                            slowprint("When the dust clears you see the wand crystalized and you feel")
                            slowprint("even more power eminating from it.")
                            slowprint("You got a crystal wand!!!")
                            player.wand = True
                            time.sleep(3)
                            break
                else:
                    slowprint("You rip off the branch and you hear crying closeby.")
                    for i in range(3):
                        slowprint("...")
                        time.sleep(1.4)
                    slowprint("Well it was probably nothing and you've got the wand!")
                    player.wand = True
                    time.sleep(1)
                    flag = False
                    break
            else:
                ##################################
                ## TODO:
                ##################################
                slowprint("That's what I thought!")
            flag = True


        elif weapon.lower() == "duck":
            duck_try = True
            duck_worth = random.randint(1,3)
            duck_take = random.randint(1,5)
            if duck_take > duck_worth:
                slowprint("You pick up the duck, but it feels less epic and useless now ...")
                player.duck = True
                flag = False
            elif duck_take < duck_worth:
                slowprint("... I'm not sure how, but you are actually not worthy to take this useless duck.")
        elif weapon.lower() == "ducky":
            slowprint("You approach the ducky with a sense of awe and wonder.\
it feels as if something fantastical will occur if you try to pick it up. Would \
you like to pick it up?\n")
            epic = input()
            if "y" in epic:
                worthy = random.randint(1,6)
                if worthy == 1 or worthy == 4:
                    slowprint("You reach down and with all the epicness of the world you grasp the ducky")
                    slowprint("and lift it into the air! If there were music it would be epic!")
                    slowprint("You have obtained the ducky and sunglasses spontaneously generated")
                    slowprint("on your face and now you exude coolness!")
                    player.ducky = True
                    flag = False

                else:
                    slowprint("WHAT? THAT'S STUPID! YOU'RE STUPID! STOP BEING STUPID! \
YOU CAN'T HANDLE IT!")
                    slowprint("Apparantly you weren't deemed worthy.")
                    ducky_try = True
                    player.ducky = False
                    flag = True




def game_over():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n________________________________________________________________________________")
    print("                           G  A  M  E     O  V  E  R")
    print("________________________________________________________________________________\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def main():
    # intro()
    story_wake_up(intro())
    chapter_two()

if __name__ == '__main__':
    main()
