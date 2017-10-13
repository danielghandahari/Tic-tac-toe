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

    # function for continue and finish the tournament.
    def continueTournament(self, tournament):
        newPlayersList = []
        playersOfTournament = tournament.players
        tournament.print_tournament()
        tournamentContinues = True
        winnersName = ""

        while True:
            # Loops with 2 step each time to avoid that same player plays multiple times.
            for x in range(0, len(playersOfTournament)-1, 2):
                plattform = Plattform()
                plattform.player1 = playersOfTournament[x]
                plattform.player2 = playersOfTournament[x+1]

                while (winnersName == ""):
                    winnersName = plattform.start_match()

                    if (winnersName == ""):
                        print "\n\n######################################"
                        print "############# It's a tie! ############"
                        print "######################################"

                print("Congratulation, " + winnersName + " win!")

                # Add the player that won the game.
                if winnersName == playersOfTournament[x].name:
                    # Reset th players moves.
                    winnersName = ""
                    plattform.player1.Moves = 5
                    newPlayersList.append(plattform.player1)
                else:
                    # Reset th players moves.
                    winnersName = ""
                    plattform.player2.Moves = 5
                    newPlayersList.append(plattform.player2)
            # Check if the tournament is finished.
            if len(newPlayersList) == 1:
                tournamentContinues = False

            # If the tournament is not finished it start over with the player that are left.
            if tournamentContinues:
                NewTournament = Tournament(newPlayersList)
                self.continueTournament(NewTournament)
            else:
                print newPlayersList[0].name + " has won the tournament!!"
                break
            break

    #function for creating a tournament with enterd amount of players.
    def startTournament(self):
        """
        Function: Create the tournament tree with entered amount of player
        """

        try:
            print "How many players will participate in the tournament?"
            amount_of_players = int(raw_input("Choose between 2,4 or 8 participates: _"))
            if 2 == amount_of_players or amount_of_players == 4 or amount_of_players == 8:
                players = self.createPlayers(amount_of_players)
                tournament = Tournament(players)
                self.continueTournament(tournament)

            else:
                print "Incorrect input for amount of participants, try again!\n\n"
                self.startTournament()
        except ValueError:
            print "Incorrect input for amount of participants, try again!\n\n"
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

            # Choosing type pf player
            while True:
                print("1. Player ")
                print("2. AI ")
                player_type = raw_input("Choose the type of the player _").lower()

                if(player_type == "1" or player_type == "2"):
                    break
                else:
                    print "Invalid input for choosing player type!"

            if(player_type == "1"):

                player_name = raw_input("Choose name for player " + str(i) + " _")

                player.name = player_name
                player.isAI = False
                player.level = None



            # Choosing AI level
            if(player_type == "2"):

                player.isAI = True

                correctAiLevelGiven = False

                while not correctAiLevelGiven:

                    try:
                        self.printAiOptions()
                        ai_level = raw_input()
                        ai_level_int = int(ai_level)

                        if (ai_level_int == 1 or ai_level_int == 2 or ai_level_int == 3):

                            ai_name = self.getAiName(ai_level_int)

                            player.name = ai_name
                            player.level = ai_level_int

                            correctAiLevelGiven = True
                        else:
                            self.notValidInput()
                            continue
                    except ValueError:
                        print 'Invalid input for AI level, number expected \n'

            players.append(player)

        return players;

    def printAiOptions(self):
        print("******CHOOSE AI ***********************")
        print("")
        print("1. Easy Eric ")
        print("2. Medium Munira ")
        print("3. Ultra Kim ")
        print("****************************************")

    def getAiName(self, level):

        if(level == 1):
            return "Easy Eric"
        elif(level == 2):
            return "Medium Munira"
        elif(level == 3):
            return "Ultra Kim"
        else:
            return ""

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
            print("3. Go back to menu")
            print("****************************************")
            print("")
            select_option_singlegame = raw_input("Enter number on what type of game you wanna play: ")

            '''
            select_option_singlegame = raw_input(
                "Do you want to play: \n"
                "1. Player vs Player \n"
                "2. Player vs AI \n"
                "3. Go back to menu\n").lower()
            '''
            winnersName = ""
            # Player vs Player
            if select_option_singlegame == "1":
                p1_name = raw_input("\n\n\nEnter the name of player 1: ")
                p2_name = raw_input("Enter the name of player 2: ")
                print(" \n \n")

                player1 = Player()
                player1.name = p1_name
                player1.isAI = False
                player1.level = None

                player2 = Player()
                player2.name = p2_name
                player2.isAI = False
                player2.level = None

                plattform.player1 = player1
                plattform.player2 = player2

                # if a game is tie, winnersName will be ""
                while(winnersName == ""):
                    winnersName = plattform.start_match()

                    if(winnersName == ""):
                        print "\n\n######################################"
                        print "############# It's a tie! ############"
                        print "######################################"

                print "\n\n######################################"
                print "####### Congratulation, " + winnersName + " win! #######"
                print "######################################"

            # Player vs AI
            elif select_option_singlegame == "2":

                p1_name = raw_input("Enter the name of player 1: ")

                correctAiLevelGiven = False

                while not correctAiLevelGiven:

                    try:
                        self.printAiOptions()
                        ai_level = raw_input()
                        ai_level_int = int(ai_level)

                        if(ai_level_int == 1 or ai_level_int == 2 or ai_level_int == 3):

                            ai_name = self.getAiName(ai_level_int)

                            player1 = Player()
                            player1.name = p1_name
                            player1.isAI = False
                            player1.level = None

                            ai_player = Player()
                            ai_player.name = ai_name
                            ai_player.isAI = True
                            ai_player.level = ai_level_int

                            plattform.player1 = player1
                            plattform.player2 = ai_player
                        else:
                            self.notValidInput()
                            continue

                        # if a game is tie, winnersName will be ""
                        while (winnersName == ""):
                            winnersName = plattform.start_match()
                            if (winnersName == ""):
                                print "\n\n######################################"
                                print "############# It's a tie! ############"
                                print "######################################"

                        print "\n\n######################################"
                        print "####### Congratulation, " + winnersName + " win! #######"
                        print "######################################"

                        correctAiLevelGiven = True
                    except ValueError:
                        print 'Invalid input for AI level, number expected \n'
            elif select_option_singlegame == "3":
                loopQuit = False

            else:
                self.notValidInput()
            #  Option prepared to add AI VS AI mode.
            '''elif select_option_singlegame == "3":
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
                        ai1_player.isAI = True
                        ai1_player.level = ai1_level_int

                        ai2_player = Player()
                        ai1_player.name = ai2_name
                        ai1_player.isAI = True
                        ai1_player.level = ai2_level_int

                        plattform.player1 = ai1_player
                        plattform.player2 = ai2_player

                        winnerName = plattform.start_match()
                        print("Congratulation, " + winnersName + " win!")

                        correctAiLevelGiven = True
                    except ValueError:
                        print 'Invalid input for AI level, number expected\n'
            '''


# Main loop with a new UINavigator
if __name__ == '__main__':

    try:
        ui = UINavigator()
        ui.choose_mode()
    except KeyboardInterrupt:
        print "\nGoodbye, see ya!"
