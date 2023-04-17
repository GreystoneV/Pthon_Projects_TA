#
# Python:    Version 3.11
#
# Author:    Benjamin Pritchard
#
# Purpose:   The Tech Academy - Python Course, Creating our first program together.
#            Demonstrating how to pass variables from function to function
#            while producing a functional game.


def start(nice=0, mean=0, name=''):
    # get users name
    name = describe_game(name)
    nice_mean(nice, mean, name)
    #  I removed 'nice, mean, name =' because they weren't being used, and it doesn't affect
    #  The functionality as far as I can tell


def describe_game(name):
    # check if new game or not
    # if it is get users name
    # else thank player for playing again

    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name\n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}".format(name))
                    print("\nIn this game you will be greeted \nby several different people. \nYou"
                          " can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name


def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approaches you for a \nconversation. Will be nice \nor mean? (N/M) \n>>> ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == 'm':
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice, mean, name)  # Pass the 3 variables to the score()


def show_score(nice, mean, name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name, nice, mean))


def score(nice, mean, name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2:  # if condition is valid, call win function passing in the variables, so it can use them
        lose(nice, mean, name)
    if mean > 2:  # if condition is valid. call lose function passing in the variables, so it can use them
        win(nice, mean, name)
    else:         # else, call nice_mean function passing in the variables, so it can use them
        nice_mean(nice, mean, name)


def win(nice, mean, name):
    show_score(nice, mean, name)
    # Substitute the {} wildcards with our variable values
    print("\nIt wasn't fun, but you were left alone! \n{}, you kept your wallet \nand enjoy a picnic, "
          "\nby the river.".format(name))
    # call again function and pass in our variables
    again(nice, mean, name)


def lose(nice, mean, name):
    show_score(nice, mean, name)
    # Substitute the {} wildcards with our variable values
    print("\nSorry {}, you were too nice! \nSomeone robbed you and you've \nlost your wallet.".format(name))
    # call again function and pass in our variables
    again(nice, mean, name)


def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>>").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( y ) for 'YES', ( n ) for 'NO':\n>>>")


def reset(nice, mean, name):
    nice = 0
    mean = 0
    # notice I do not reset name var as that same user has elected to play again
    start(nice, mean, name)


if __name__ == "__main__":
    start()
