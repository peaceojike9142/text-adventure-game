import time


def valid_input(prompt, option1, option2, option3):
    while True:
        response = input(prompt)
        if option1 in response:
            return response
        elif option2 in response:
            return response
        elif option3 in response:
            return response
        else:
            print_pause("Sorry, I don't understand.")


def help1():
    print_pause("the game is easy")
    print_pause("follow the info")
    print_pause("he find the keys")
    print_pause("then leave the house")
    print_pause("the try of keys part")
    print_pause("is based on randomness")


def print_pause(msg):
    time.sleep(2)
    print(msg)


def back():
    while True:
        response = valid_input("where do you want to go,"
                               "(1) for bedroom,"
                               "(2) for kitchen,"
                               "(3) for living room",
                               "1", "2", "3")
        if response == "1":
            time.sleep(2)
            bedroom()
        if response == "2":
            time.sleep(2)
            kitchen()
            break
        if response == "3":
            print_pause("you don't have the keys try another room")


def door():
    while True:
        response = valid_input("where do you want to go,"
                               "(1) for bedroom,"
                               "(2) for kitchen,"
                               "(3) for living room",
                               "1", "2", "3")
        if response == "1":
            print_pause("you already have the keys leave the house")
        elif response == "2":
            print_pause(" what are you doing go to school")
        elif response == "3":
            print_pause("yes, you have the keys now go to the door")
            break


def bedroom():
    print_pause("You're now in your bed room ,"
                "there in a computer in your desk")
    print_pause("And there is a locker with a note,")
    print_pause("and a gaming set")
    print_pause("Check if you will see the keys ")
    while True:
        response = valid_input("1 for computer or 2 for locker"
                               "3 for gaming set", "1", "2", "3")
        if response == "1":
            print_pause(" there is nothing here")
        elif response == "2":
            print_pause(" it's a note from your mom,")
            print_pause(" ' hello my son when you wake up,")
            print_pause("the keys are in the kitcher carbinat'")
            break
        elif response == "3":
            print_pause("you need to get going sir")


def kitchen():
    print_pause("Okay you're now in the kitchen")
    print_pause(" You look around there is a locker,"
                "a carbinat , and a cooker ")
    print_pause("Let's check around ")
    while True:
        response = valid_input("(1) for locker, (2) for carbinate,"
                               "(3) for cooker", "1", "2", "3")
        if response == "1":
            print_pause(" it's no hope the key isn't here")
        elif response == "3":
            print_pause(" there's nothing here just food ")
        elif response == "2":
            print_pause(" yaahoooooooo i finally found it ")
            print_pause(" time to get out of here ,")
            print_pause(" go to the living room. ")
            break


def SorL():
    print_pause("""you're now in the living room
    do you have the keys if you do, go to the door""")
