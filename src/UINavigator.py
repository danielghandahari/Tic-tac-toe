# ------------------------------------------------------------------------------
# -- File Name:       UINavigator.py
# -- University:      Uppsala University
# -- Department:      Information Technology
# -- Course:          Software Engineering and Project Management
# -- Project:         Tic-Tac-Toe         
# -- Author:          Group D
# -- Description:     In this class implement the UI Navigator. 
# --                  It handles the user inputs and return it to the specific function.
# ------------------------------------------------------------------------------

from plattform import Plattform
from player import Player
from tournament import Tournament

class UINavigator:
   
    #function for not a valid input option
    def notValidInput(self):
        """
        Function: Print warning if the user does not select a valid input.
        """

        print("")
        print("You have not selected a valid option!")
        print("")
   
    #function for creating a tournament with enterd amount of players.
    def startTournament(self):
        """
        Function: Create the tournament tree with entered amount of player
        """

        try:
            amount_of_players = int(raw_input("How many players will participate in the tournament? _"))

            players = self.createPlayers(amount_of_players)

            tournament = Tournament(players)
            tournament.print_tournament()
        except ValueError:
            print "Incorrect input for amount of participants, try again!"
            self.startTournament()


    #fucntion for priting the start menu. 
    def print_menu(self):
        """
        Function: Print the Main Menu
        """

        print("")
        print("")
        print("******TIC***TAC***TOE***MENU***********")
        print("")
        print("[S]tart game")
        print("[T]ournament")
        print("[Q]uit game")
        print("")
        print("****************************************")
        print("")

    def choose_mode(self):
        """
        Function: Handle the user valid-input based on the main menu.
        """

        done = False

        while not done:

            self.print_menu()

            select_option = raw_input("What do you want to do? Please choose between S, T, or Q _").lower()

            if select_option == "s":
                self.startQuickMatch()

            elif select_option == "t":
                self.startTournament()

            elif select_option == "q":
                loopQuit = True
                while loopQuit:
                    select_option_quit = raw_input("Do you really want to quit? \n[Y]es / [N]o \n").lower()
                    if select_option_quit == "y":
                        print("")
                        print("Thanks for playing!")
                        print("Goodbye")
                        loopQuit = False
                        done = True
                    elif select_option_quit == "n":
                        loopQuit = False
                    else:
                        self.notValidInput()
            else:
                self.notValidInput()

    
    def createPlayers(self, amount_of_players):
        """
        Function:   Handle the player creation if it is a human or AI, and also the AI level. 
        Return:     List of created players 
        """

        # Creates a list of players
        players = []

        for i in range(1, amount_of_players + 1):
            print "\nCreating player number " + str(i)
            # Creates a new player
            
            player = Player()
            player_name = raw_input("Choose name for player " + str(i) + " _")

            player.name = player_name
            player.isAI = False
            player.level = None

            while True:
                # User can define the player type, Human or AI 
                player_type = raw_input("Choose the type for " + str(player_name) + "\n1. Player" + "\n2. AI _").lower()

                if(player_type == "1"): break
                if (player_type == "2"): break



            # Choosing AI level
            if(player_type == "2"):

                player.isAI = True
                while True:
                    ai_level = raw_input(
                        "Choose the AI level for " + str(player_name) + "\n1.Easy \n2.Medium \n3.Hard").lower()

                    if (ai_level == "1"): break
                    if (ai_level == "2"): break
                    if (ai_level == "3"): break

                player.level = ai_level

            players.append(player)

        return players;

    #function for starting a quickmatch with different options PvP PvAI, AIvAI
    def startQuickMatch(self):
        """
        Function: Handle a single game. It can be Player vs Player, Player vs AI, or AI vs AI.
        """

        loopQuit = True
        plattform = Plattform()
        while loopQuit:

            # Menu for startQuickMatch
            print("")
            print("")
            print("******GAME MODE ***********************")
            print("")
            print("1. Player vs Player ")
            print("2. Player vs AI ")
            print("3. AI vs AI ")
            print("4. Go back to menu")
            print("****************************************")
            print("")
            select_option_singlegame = raw_input("Enter number on what type of game you wanna play: ")

            '''
            select_option_singlegame = raw_input(
                "Do you want to play: \n"
                "1. Player vs Player \n"
                "2. Player vs AI \n"
                "3. AI vs AI \n"
                "4. Go back to menu\n").lower()
            '''
            # Player vs Player
            if select_option_singlegame == "1":
                p1_name = raw_input("Enter the name of player 1: ")
                p2_name = raw_input("Enter the name of player 2: ")

                player1 = Player()
                player1.name = p1_name
                player1.isAi = False
                player1.level = None

                player2 = Player()
                player2.name = p2_name
                player2.isAi = False
                player2.level = None

                plattform.player1 = player1
                plattform.player2 = player2

                plattform.start_match()

            # Player vs AI
            elif select_option_singlegame == "2":

                p1_name = raw_input("Enter the name of player 1: ")
                ai_name = raw_input("Enter the name of the AI: ")

                correctAiLevelGiven = False

                while not correctAiLevelGiven:

                    try:
                        ai_level = raw_input("Enter the level the AI: ")
                        ai_level_int = int(ai_level)

                        player1 = Player()
                        player1.name = p1_name
                        player1.isAi = False
                        player1.level = None

                        ai_player = Player()
                        ai_player.name = ai_name
                        ai_player.isAi = True
                        ai_player.level = ai_level_int

                        plattform.player1 = player1
                        plattform.player2 = ai_player

                        plattform.start_match()

                        correctAiLevelGiven = True
                    except ValueError:
                        print 'Invalid input for AI level, number expected \n'

            elif select_option_singlegame == "3":
                # AI vs AI
                ai1_name = raw_input("Enter the name of the first AI: ")
                ai2_name = raw_input("Enter the name of the second AI: ")

                correctAiLevelGiven = False

                while not correctAiLevelGiven:

                    try:
                        ai1_level = raw_input("Enter the level of " + ai1_name)
                        ai1_level_int = int(ai1_level)

                        ai2_level = raw_input("Enter the level of " + ai2_name)
                        ai2_level_int = int(ai2_level)

                        ai1_player = Player()
                        ai1_player.name = ai1_name
                        ai1_player.isAi = True
                        ai1_player.level = ai1_level_int

                        ai2_player = Player()
                        ai1_player.name = ai2_name
                        ai1_player.isAi = True
                        ai1_player.level = ai2_level_int

                        plattform.player1 = ai1_player
                        plattform.player2 = ai2_player

                        plattform.start_match()

                        correctAiLevelGiven = True
                    except ValueError:
                        print 'Invalid input for AI level, number expected\n'
            elif select_option_singlegame == "4":
                loopQuit = False

            else:
                self.notValidInput()


# Main loop with a new UINavigator
if __name__ == '__main__':

    try:
        ui = UINavigator()
        ui.choose_mode()
    except KeyboardInterrupt:
        print "\nGoodbye, see ya!"
