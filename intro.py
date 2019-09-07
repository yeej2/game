import random
import time
import sys
import brodah_birday as bb
import player as pl

def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./90)

def intro():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    slowprint("----------------------")
    slowprint("C H A P T E R   O N E ")
    slowprint("----------------------")

    name = input("\nWhat is your name:\n")
    if "jon" in name.lower() or "oo" in name.lower() or "ok" in name.lower() or "oy" in name.lower() or "bro" in name.lower():
        slowprint("BRODAH!!! I HAVE PLANS FOR YOU!!!")
        brodah = True


    else:
        slowprint("Alrighty! ")
        print(name)

    # else:
    #     slowprint("Sorry, either you didn't take this seriously enough or you're not brodah")
    #     slowprint("Soooooo yeah, see ya ...")
    #     time.sleep(2)
    #     game_over()
    #     slowprint("You weren't cool enough to play yo")
    #     time.sleep(2)
    #     sys.exit()

    adv = input("Are you ready for an adventure? : ")
    if "y" in adv.lower():
        pl.player.name = name

    elif "n" in adv.lower():
        slowprint("Oh ... ok")
        game_over()
        slowprint("Guess you were too cool to play :(")
        time.sleep(2)
        sys.exit()

    else:
        slowprint("I don't think you answered right ... but you meant yes right!? :D")
        time.sleep(2)
        pl.player.name = name
