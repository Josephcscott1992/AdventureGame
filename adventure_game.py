import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if response == option1:
            break
        elif response == option2:
            break
        else:
            print_pause("That is not an option, try again.")
    return response


def intro():
    day = ["Day 40:", "Day 173:", "Day 386:"]
    days = random.choice(day)
    print(days)

    print_pause("You are sleeping in the cabin of your pirate ship sailing "
                "across the ocean on a dark and calmly night.")
    print_pause("Suddenly your ship starts to shake violently!!!")
    print_pause("You immediately get up and decide what to do next.\n")


def decision():
    response = valid_input("Enter 1 to go outside onto the deck and see what "
                           "is going on.\n"
                           "Enter 2 to wait it off and see if it was due to "
                           "weather or just a minor hiccup.\n",
                           "1", "2")
    if "1" in response:
        print_pause("You approach to open the door, but hesistate and "
                    "ponder if you should "
                    "bring a weapon for assurance.")
        print_pause("You look around and found your weapon.")
        weapon = valid_input("Should you bring your weapon? "
                             "'yes' or 'no'.\n",
                             "yes", "no")
        if "yes" in weapon:
            print_pause("You take your weapon and then head to the deck!")
            print_pause("You head out to the deck and look into the water "
                        "and see a giant squid!")
            print_pause("The giant squid tries to grab you, but luckily "
                        "you brought your weapon!")
            fight()
        elif "no" in weapon:
            print_pause("You do not grab your weapon and head to the deck!")
            print_pause("You head out to the deck and look into the water "
                        "and see a giant squid!")
            weapon = valid_input("Should you run back into the cabin and "
                                 "grab your weapon? "
                                 "'yes' or 'no'.\n",
                                 "yes", "no")
            if "yes" in weapon:
                print_pause("You run back into the cabin then take your "
                            "weapon and then head to the deck!")
                print_pause("You head out to the deck and look into the "
                            "water and see a giant squid!")
                print_pause("The giant squid tries to grab you, but "
                            "luckily you brought your weapon!")
                fight()
            elif "no" in weapon:
                print_pause("You try and fight off the giant squid with "
                            "your bare hands!")
                print_pause("The giant squid pulls you into the sea!")
                print_pause("Game Over...")

            play_again()

    elif "2" in response:
        print_pause("You wait and see if the shaking stops...")
        print_pause("The shaking continues...")
        print_pause("The shaking becomes more violent! Which forces you "
                    "to check what is going on outside of the cabin.\n")
        decision()


def fight():
    fight = valid_input("Should you fight off the giant squid?"
                        "'yes' or 'no'\n",
                        "yes", "no")
    if "yes" in fight:
        print_pause("You ward it off with your weapon and the giant squid "
                    "breaks away and returns to sea!")
        print_pause("You are victoriuous and can return into the cabin for "
                    "more sleep!")
        print_pause("YOU WIN!!!")
    elif "no" in fight:
        print_pause("The giant squid pulls you into the sea!")
        print_pause("Game Over...")

    play_again()


def play_again():
    restart = valid_input("Would you like to play again...?"
                          "'yes' or 'no'\n",
                          "yes", "no")
    if "yes" in restart:
        print_pause("Restarting game...")
        intro()
        decision()
    elif "no" in restart:
        print_pause("Good bye see you next time!")
    else:
        print_pause("That is not an option, try again.")


intro()
decision()
