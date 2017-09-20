from plattform import Plattform
from player import Player

class UINavigator:

    def notValidInput(self):
        print("")
        print("You have not selected a valid option!")
        print("")

    def startTournament(self):
        print("Tournament started")

    def print_menu(self):
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

        done = False

        while not done:

            self.print_menu()

            select_option = raw_input("What do you want to do?: ").lower()

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


    def startQuickMatch(self):

        loopQuit = True
        plattform = Plattform()
        while loopQuit:

            # Menu for startQuickMatch
            select_option_singlegame = raw_input(
                "Do you want to play: \n"
                "1. Player vs Player \n"
                "2. Player vs AI \n"
                "3. AI vs AI \n"
                "4. Go back to menu\n").lower()

            # Player vs Player
            if select_option_singlegame == "1":

                p1_name = raw_input("Enter the name of player 1: ")
                p2_name = raw_input("Enter the name of player 2: ")

                player1 = Player(p1_name, False, None)
                player2 = Player(p2_name, False, None)

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

                        player1 = Player(p1_name, False, None)
                        ai_player = Player(ai_name, True, ai_level_int)

                        plattform.player1 = player1
                        plattform.player2 = ai_player

                        plattform.start_match()

                        correctAiLevelGiven = True
                    except ValueError:
                        print 'Invalid input for AI level, number expected \n'

            elif select_option_singlegame == "3":

                ai1_name = raw_input("Enter the name of the first AI: ")
                ai2_name = raw_input("Enter the name of the second AI: ")

                correctAiLevelGiven = False

                while not correctAiLevelGiven:

                    try:
                        ai1_level = raw_input("Enter the level of " + ai1_name)
                        ai1_level_int = int(ai1_level)

                        ai2_level = raw_input("Enter the level of " + ai2_name)
                        ai2_level_int = int(ai2_level)

                        ai1_player = Player(ai1_name, True, ai1_level_int)
                        ai2_player = Player(ai2_name, True, ai2_level_int)

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





if __name__ == '__main__':

    ui = UINavigator()
    ui.choose_mode()
