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
    slowprint("However, since you have yours truly,")
    slowprint("I bet he'll take it easy on you!'")
    slowprint("\nDid you want to approach him?")
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

        else:
            slowprint("\n'No of course not ... anyways this here is")
            slowprint(pl.player.name)
            slowprint("I met them and they wanted to meet you!'")
            slowprint("The wizard turns to face you, 'Well, then")
            slowprint("Here I am! But first I must give you a quick test.")
            slowprint("Pick a number between 1 and 5. If you get it right")
            slowprint("I'll give you something amazing and invite you into my home")
            slowprint("If you get it 1 off, I will still invite you in, but no other prize.")
            slowprint("However if you get it 2 off, I must ask you to leave.")
            slowprint("You don't want to know what happens if you get it more than 3 off ...'")
            slowprint("So then friend, ...")
            time.sleep(.7)
            slowprint("Pick a number'")
            guess = input()
            pick = random.randint(1,5)
            if guess == "1":
                guess = 1
            elif guess == "2":
                guess = 2
            elif guess == "3":
                guess = 3
            elif guess == "4":
                guess = 4
            elif guess == "5":
                guess = 5

            else:
                "BAH YOU DIDN'T CHOOSE CORRECTLY! BEGONE SPAWN OF MEMPHA BEGONE!!!"

            if guess == pick:
                slowprint("CORRECT!!! right on the money!!!")

            elif guess == pick+1 or guess == pick -1:
                slowprint("OH so close, only one off though!")
                print("for reference my number was ", pick)

            elif guess == pick + 2 or guess == pick - 2:
                slowprint("Sorry friend, I'm gonna have to ask you to leave ...")
                slowprint("It was about two off.")
                print("This was my number: ",pick)

            else:
                slowprint("As soon as you say the number the wizard looks at you with sadness")
                slowprint("'I'm sorry friend, but that's very wrong ... my number was")
                print(pick)
                slowprint("I wish I could help you ... but it's beyond my power.'")

                if pl.player.wand == False:
                    slowprint("Your body starts to feel strange, like ... wierd strange.")
                    slowprint("Like the i before e except after c has way more exceptions than it should wierd")
                    slowprint("... WIERD ... anyways you start vomiting pigeons and then out of nowhere")
                    return None

                elif pl.player.wand == True:
                    slowprint("You look puzzled by what the wizard has said and then all")
                    slowprint("of a sudden your wand starts to glow.")
                    slowprint("The wizard looks shocked and then he flinches away from you.")
                    return None
    elif "n" in path:
        slowprint(" ... ")
        time.sleep(1)
        slowprint("Ya know ... I worked hard on this ... you're missing all the story!")
        time.sleep(1)
        slowprint("'I mean ... Oh yeah I'll see ya later lazer!")
        slowprint("Fine ... you continue past the hut or whatever chapter 4 yada yada yada.")
