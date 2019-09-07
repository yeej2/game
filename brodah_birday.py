import random
import time
import sys

import player as pl
import player_party as pp
import player_flags as pf
import game_status as g


import intro
import chapter_one as one
import chapter_two as two
import chapter_three as three

def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./90)

def stats():
    print("Name ", pl.player.name)
    print("Weapon")

def main():
    intro.intro()
    one.story_wake_up()
    two.chtwo()
    three.chthree()

if __name__ == '__main__':
    main()
