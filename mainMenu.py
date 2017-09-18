# Name File: mainMenu.py
# Description   :
#       When name has been registred, a simple menu is shown with options for the user;
#       [1] : Play a new game - A player creates a new game (single game, other user or AI, creates a tournament)
#       [2]: Join a game - A player joins an already existing game (tournament)
#       [3]: Quit. - Quit the application
#       To access each options, the user has to press the respective number on the keyboard.
#       The input is captured as a single string character followed by a return.

def mainMenu():
    """Function to navigate the main menu"""
    print "What do you want to play?"
    print "[1] Play a new game"
    print "[2] Join a game"
    print "[3] Quit"

mainMenu()

ask = True

while ask:
    menu = str(raw_input("Please press [1] or [2] or [3]: "))
    mainMenu()
    if menu == "1":
        print "go to play new game func"
        ask = False
    elif menu == "2":
        print "go to join a game func"
        ask = False
    elif menu == "3":
        print "go to quit game func"
        ask = False
    else:
        print "Please enter a respective key \n"

