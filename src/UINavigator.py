from plattform import Plattform
from player import Player
from tournament import Tournament

class UINavigator:

    def startTournament(self):
        print "Tournament started"

        amount_of_players = raw_input("How many players will participate in the tournament? _")

        players = self.createPlayers(amount_of_players)

        tournament = Tournament(players)
        tournament.create_tournament_tree()

    def print_menu(self):
        print("[S]tart game")
        print("[T]ournament")
        print("[Q]uit game")


    def choose_mode(self):

        done = False

        while not done:

            self.print_menu()

            select_option = raw_input("What do you want to do? _").lower()

            if select_option == "s":
                self.startQuickMatch()

            elif select_option == "t":
                self.startTournament()

            elif select_option == "q":
                select_option_quit = raw_input("Do you really want to quit? \n[y]/[n]\n").lower()
                if select_option_quit == "y":
                    done = True
                elif select_option_quit == "n":
                    continue

            else:
                print("You have not selected a vaild option ")

    def createPlayers(self, amount_of_players):

        players = []

        for i in range(1, amount_of_players + 1):
            print "Creating player number " + str(i) + "\n"

            player = Player()
            player_name = raw_input("Choose name for player " + str(i) + " _")

            player.name = player_name
            player.isAI = False
            player.level = None

            while True:
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





    def startQuickMatch(self):

        select_option_singlegame = raw_input(
            "Do you want to play: \n1. Player vs Player \n2. Player vs AI \n3. AI vs AI \n4. Go back to menu\n").lower()


        if select_option_singlegame != "4":

            plattform = Plattform()


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
            if select_option_singlegame == "2":

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

            if select_option_singlegame == "3":

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




if __name__ == '__main__':

    ui = UINavigator()
    ui.choose_mode()
