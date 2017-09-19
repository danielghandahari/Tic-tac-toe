class UINavigator:

    def startTournament(self):
        print("Tournament started")

    def print_menu(self):
        print("[S]tart game")
        print("[T]ournament")
        print("[Q]uit game")


    def choose_mode(self):
        self.print_menu()

        select_option = raw_input("What do you want to do ").lower()

        if select_option == "s":
            self.startQuickMatch()

        elif select_option == "t":
            self.startTournament()

        elif select_option == "q":
            select_option_quit = raw_input("Do you really want to quit \n[y]/[n] \n").lower()
            if select_option_quit == "y":
                loop = False
            elif select_option_quit == "n":
                print("")

        else:
            print("You have not selected a vaild option ")



    def startQuickMatch(self):
        # prints the options for the user and takes an input 1-3
        select_option_singlegame = raw_input(
            "Do you want to play: \n1. Player vs Player \n2. Player vs AI \n3. Go back to menu\n").lower()

        # Player vs Player
        if select_option_singlegame == "1":
            # add the player name for player 1
            player1 = raw_input("Enter the name of player 1: ")
            # add the player name for player 2
            player2 = raw_input("Enter the name of player 2: ")
            # not needed in later versions
            print("player1:" + player1 + "\n player2:" + player2)
        # now start the game and call the platform
        # send information about player names to platform

        # Player vs AI
        elif select_option_singlegame == "2":
            # add the player name send this to the platform
            player = raw_input("Enter the name of the player: ")

            # get the difficulty for the AI (int)
            ai_level = is_AI()
            print(ai_level)
            # send difficulty to platfrom

if __name__ == '__main__':

    ui = UINavigator()
    ui.choose_mode()