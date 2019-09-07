import random
import time
import sys

import player as pl
import player_party as pp
import player_flags as pf
import game_status as g


def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./90)


def chthree():

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

    slowprint("You follow the path and eventually you see a small hut.")
    if pp.party.pig == True:
        wizard_pig()
    else:
        wizard()

    slowprint("")
    print("\n\n\n________________________________________________________________________________")
    print("                           C O M I N G    S O O N")
    print("________________________________________________________________________________\n\n\n")

    time.sleep(3)


    def wizard():
        slowprint("You see an old man in a cloak sitting outside. Do you want to approach him?")
        path = input()
        if "y" in path or "sur" in path:
            slowprint("you approach the hut and the old man gets up to greet you")
            slowprint("'Why hello friend. What are you doing here?'")
            slowprint("[1] I dunno how I even got here.")

        elif "n" in path:
            slowprint(" ... ")
            time.sleep(1)
            slowprint("Ya know ... I worked hard on this ... you're missing all the story!")
            time.sleep(1)
            slowprint("Fine ... you continue past the hut or whatever chapter 4 yada yada yada.")


    def wizard_pig():
        slowprint("The pig turns to you and says, 'LOOK THAT'S THE HUT!")
        slowprint("This is where the wizard lives. I should warn you though,")
        slowprint("he likes to test people who visit him. So unless you have a way to ")
        slowprint("Deflect or protect yourself from his magic, or you're just super sturdy,")
        slowprint("You should probably pass by and we'll part ways.")
        slowprint("However, since you have yours truly and you saved my life from whatever hurt me,")
        slowprint("I bet he'll take it easy on you!'")
        slowpritn("\nDid you want to approach him?")
        path = input()

        if "y" in path or "abs" in path or "sur" in path:
            slowprint("You apprach the old man. He turns to you and says,")
            slowprint("'Welcome friend, ... and ROCKY!!! I have been so worried about you!")
            slowprint("I thought you tried to run away from me just like my wife ...'")

            if pf.player_flag.pig_heal == True:
                slowprint("Rocky tells the wizard about how he was savagely attacked by an")
                slowprint("unknown stranger and you managed to heal him! The wizard turns to you")
                slowprint("and says,\n'Thank you friend for saving Rocky's life!")
                slowprint("As a reward ...' The wizard puts forward two fists and says to you,")
                slowprint("'Pick a hand.'")
                slowprint("Which hand do you want to choose?")
                hand = input()
                fate = random.randint(1,10)
                if fate >=3:
                    slowprint("You think about it and you decide to point to the hand on the")
                    slowprint(hand)
                    slowprint("The wizard opens his hand and you are pleasantly surprised to")
                    slowprint("the smell of a lovely breakfast!")
                    slowprint("You sit around a table with the wizard and Rocky and share this meal.")
                    slowprint("The food is so incredible that your health is fully restored!")
                    pl.player.health = 5
                    print("HEALTH :",pl.player.health)

                elif fate <3:
                    slowprint("You think about it and you decide to point to the hand on the")
                    slowprint(hand)
                    slowprint("You await this stranage surprise when all of a sudden you start growing")
                    slowprint("limbs ... but the kind that's on a tree!!!")
                    slowprint("Oh unlucky for you I suppose that's gotta hurt a lot!")
                    pl.player.health -= 3
                    if pl.player.health <= 0:
                        slowprint("You fight and you fight but you have no more left in you.")
                        slowprint("Rocky and the wizard wave goodbye and you start your new life ... er ")
                        slowprint("death as a tree.")
                        slowprint("HEALTH : 0")
                        time.sleep(1.5)
                        g.game_over()
                        slowprint("(HINT you take 3 damage from this, try to keep more of your health!)")
                        sys.exit()

                    elif pl.player.health > 0:
                        slowprint("You fight and you fight, and you manage to have enough will power")
                        slowprint("to break free of the curse!")
                        slowprint("'BRAVO!' the wizard exclaims.")
