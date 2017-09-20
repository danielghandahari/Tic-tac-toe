import player

class Plattform:


    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.winner = None
        self.gameEngine = None
        board = [" ", " ", " ",
                 " ", " ", " ",
                 " ", " ", " "]




    def print_board(self):
        """FUnction to print the board"""
        print("======= Your movement =======")
        print("           " + "-------")
        print("           " + "|" + self.board[0] + "|" + self.board[1] + "|" + self.board[2] + "|")
        print("           " + "-------")
        print("           " + "|" + self.board[3] + "|" + self.board[4] + "|" + self.board[5] + "|")
        print("           " + "-------")
        print("           " + "|" + self.board[6] + "|" + self.board[7] + "|" + self.board[8] + "|")
        print("           " + "-------")
        print("============================= \n")

    def print_board_dummies(self):
        """FUnction to print the board dummies, so the player know the position"""
        print("======= Board Dummies =======")
        print("           " + "-------")
        print("           " + "|" + "1" + "|" + "2" + "|" + "3" + "|")
        print("           " + "-------")
        print("           " + "|" + "4" + "|" + "5" + "|" + "6" + "|")
        print("           " + "-------")
        print("           " + "|" + "7" + "|" + "8" + "|" + "9" + "|")
        print("           " + "-------")
        print("============================= \n")

    def start_match(self):
        "Logic for starting a match"
        print "Match started \n Under progress \n \n \n"

    def player_x_move(self):
        """Function to handle player X movement"""
        self.print_board()
        # Capture player X movement
        try:
            move = raw_input("Where do you want to move " + "Player-X" + "? ")
            move = int(move) - int(1)
            # Check if the player inputs valid input i.e 0-8
            if move > -1 and move < 9:
                # Check if the space is empty or not
                if self.board[move] == " ":
                    self.board[move] = "X"
                else:
                    print("The space is taken!")
                    self.player_x_move()
            else:
                print("Please write valid input i.e 1-9!")
                self.player_x_move()
        # If user enter non-integer input
        except ValueError:
            print("Please write valid input i.e 1-9!")
            self.player_x_move()

    def player_o_move(self):
        """Function to handle player O movement"""
        self.print_board()
        # Capture player O movement
        try:
            move = raw_input("Where do you want to move " + "Player-O" + "? ")
            move = int(move) - int(1)
            # Check if the player inputs valid input i.e 0-8
            if move > -1 and move < 9:
                # Check if the space is empty or not
                if self.board[move] == " ":
                    self.board[move] = "O"
                else:
                    print("The space is taken")
                    self.player_o_move()
            else:
                print("Please write valid input i.e 1-9!")
                self.player_x_move()
        # If user enter non-integer input
        except ValueError:
            print("Please write valid input i.e 1-9!")
            self.player_x_move()

