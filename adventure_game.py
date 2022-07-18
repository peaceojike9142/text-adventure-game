import items
import time
import random
from items import valid_input
from items import print_pause


def intro():
    is_key = False
    while is_key is False:
        response = valid_input("(1) to begin (2) to exit (3) for help ",
                               "1", "2", "3")
        if response == "1":
            print_pause("THIS GAME IS CALLED FIND THE KEYS")
            print_pause("You wake up late on a monday morning,")
            print_pause("You discovered you're late for school, "
                        "and it's 8:00am already,")
            print_pause("after dressing up it's time to leave the house "
                        "but you cant find the keys")
            print_pause("and your mom left early "
                        "and locked the doors "
                        "because she knew you had a keys")
            print_pause("but you can't find them, "
                        "now it's a race to find the keys")
            print_pause(items.back())
            break
        elif response == "2":
            print(" THANK YOU FOR PLAYING BYE")
            exit()
            break
        elif response == "3":
            items.help1()


def going_out():
    is_key = True
    while is_key is True:
        items.door()
        break


def living():
    while True:
        key = [1, 2, 3, 4]
        keys = random.choice(key)
        n = input("press 1")
        if n == "1":
            if keys == 2:
                print_pause("that's it you won ")
                break
            else:
                print_pause("that's not the key try again")
        else:
            print_pause("please press 1 ")


def out_the_door():
    while True:
        response = valid_input("(1) to go to door (2) to go back (3) for help",
                               "1", "2", "3")
        if response == "1":
            print_pause("you're now at the door")
            print_pause("but there's a little problem")
            print_pause("you don't know which key to use")
            print_pause("press 1 to try different keys randomly")
            living()
            break
        elif response == "2":
            items.door()
        elif response == "3":
            items.help1()


def play_again():
    while True:
        response = valid_input("would you like to play again"
                               "(1) for yes (2) for no (3) for help",
                               "1", "2", "3")
        if response == "1":
            print_pause("thank you lets play")
            intro()
            going_out()
            out_the_door()
        elif response == "2":
            print_pause(" thank you for playing bye")
            break
        elif response == "3":
            items.help1()


def play_game():
    intro()
    going_out()
    out_the_door()
    play_again()


play_game()
