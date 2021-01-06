# main.py
# Midnight Rider
# A text adventure game that is riveting.
# IGN gives it 4 stars out of 100

import random
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
    C. Drive full throttle
    D. Stop for fuel at a refuelling station (No tofu in stock)
    E. Status Check
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

    # Constants
    MAX_FUEL_LEVEL = 50
    MAX_TOFU_LEVEL = 3

    # variables
    done = False
    km_traveled = 0  # 100km traveled is the goal
    agents_distance = -20.0
    turns = 0  # amount of turns taken
    tofu = MAX_TOFU_LEVEL # 3 is max tofu
    fuel = MAX_FUEL_LEVEL  # 50 is full tank
    hunger = 0  # hunger increases with num

    # LOOP
    while not done:
        pass
        # Check if they reached end game

        # Give the player their choices
        print(CHOICES)

        # Handle users' input
        users_choice = input("What do you want to do? ").lower().strip("!.,?")

        if users_choice == "c":
            # Drive fast
            player_distance_now = random.randrange(10, 16)
            agent_distance_now = random. randrange(7, 15)

            # Burn fuel
            fuel -= random.randrange(5, 11)

            # Player distance traveled
            km_traveled += player_distance_now

            # Agent distance traveled
            agents_distance -= (player_distance_now - agent_distance_now)
            # Feedback to player
            print()
            print(f"-------- You sped ahead {player_distance_now} KMs")
            print()

        if users_choice == "d":
            # Refueling
            # Fill the fuel tank
            fuel = MAX_FUEL_LEVEL

            # Consider the agents coming closer
            agents_distance += random.randrange(7, 15)

            # Give the user feedbackd
            print("")
            print("-------- You filled the fuel tank")
            print("-------- The agents got closer...")
            print("")

        if users_choice == "e":

            print(f"\t---Status---")
            print(f"km_traveled: {km_traveled}")
            print(f"Fuel left: {fuel}")
            print(f"Agents are {abs(agents_distance)} KMs behind you")
            print(f"You have {tofu} tofu left")
            print("---------------\n")
        elif users_choice == "q":
            done = True


# Outroduction

print("Thank you for playing this game.")

# TODO: Change environment based on choices and RNG


if __name__ == '__main__':
    main()
