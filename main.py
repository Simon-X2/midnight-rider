# main.py
# Midnight Rider
# A text adventure game that is riveting.
# IGN gives it 4 stars out of 100

import textwrap
import sys
import time

INTRODUCTION = """

WELCOME TO MIDNIGHT RIDER

WE'VE STOLEN A CAR. WE NEED TO GET IT HOME.
THE CAR IS SPECIAL.

THE GOVERNMENT WANTS IT FOR THEIR OWN GAIN.


WE CAN'T LET THEM HAVE IT.

ONE GOAL: SURVIVAL...and THE CAR.
REACH THE END BEFORE THE MAN GON GETCHU.

"""
CHOICES = """
    ----
    Q. QUIT
    ----
"""


def intro():

    for char in textwrap.dedent(INTRODUCTION):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)

def main():
    intro()

    done = False

    # LOOP
    while not done:
        pass
    # TODO: Check if they reached end game

    # Give the player their choices
        print(CHOICES)
    # Handle users' input
        users_choice = input("What do you want to do? ").lower().strip("!.,?")
        if users_choice == "q":
            done = True


# Outroduction

print("Thank you for playing this game.")





    # TODO: Change environment based on choices and RNG


if __name__ == '__main__':
    main()
