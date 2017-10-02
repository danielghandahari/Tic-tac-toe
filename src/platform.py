class Plattform:


    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.winner = None
        self.gameEngine = None
        self.board = [" ", " ", " ",
                 " ", " ", " ",
                 " ", " ", " "]

    def __str__(self):
        return self.player1.name + " VS " + self.player2.name




    def print_board(self):

        print("======= Your movement =======")
        print("           " + "-------")
        print("           " + "|" + self.board[0] + "|" + self.board[1] + "|" + self.board[2] + "|")
        print("           " + "-------")
        print("           " + "|" + self.board[3] + "|" + self.board[4] + "|" + self.board[5] + "|")
        print("           " + "-------")
        print("           " + "|" + self.board[6] + "|" + self.board[7] + "|" + self.board[8] + "|")
        print("           " + "-------")
        print("============================= \n")

    def print_board_instruction(self):

        print("======= Board instruction =======")
        print("           " + "-------")
        print("           " + "|" + "1" + "|" + "2" + "|" + "3" + "|")
        print("           " + "-------")
        print("           " + "|" + "4" + "|" + "5" + "|" + "6" + "|")
        print("           " + "-------")
        print("           " + "|" + "7" + "|" + "8" + "|" + "9" + "|")
        print("           " + "-------")
        print("============================= \n")

    def check_winner(self, tile):

        if((tile == "X") or (tile == "O")):

            if (self.board[0] == tile and self.board[1] == tile and self.board[2] == tile) or \
                    (self.board[3] == tile and self.board[4] == tile and self.board[5] == tile) or \
                    (self.board[6] == tile and self.board[7] == tile and self.board[8] == tile) or \
                    (self.board[0] == tile and self.board[3] == tile and self.board[6] == tile) or \
                    (self.board[1] == tile and self.board[4] == tile and self.board[7] == tile) or \
                    (self.board[2] == tile and self.board[5] == tile and self.board[8] == tile) or \
                    (self.board[0] == tile and self.board[4] == tile and self.board[8] == tile) or \
                    (self.board[2] == tile and self.board[4] == tile and self.board[6] == tile):

                    return True

        return False

    def check_tie(self):
        if (" " not in self.board):
            print("Tie! No player wins!")
            return True


    def clean_board(self):
        self.board = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]

    def start_match(self):

        while True:

            self.print_board_instruction()

            # Check if player X wins
            self.move_player(self.player1.name, "X")
            x_winner = self.check_winner("X")
            if(x_winner):
                print("Congratulation, " + self.player1.name + " win!")
                self.print_board()
                break

            # Check tie
            tie = self.check_tie()
            if tie:
                self.print_board()
                break

            # Check if player O wins
            self.move_player(self.player2.name, "O")
            o_winner = self.check_winner("O")
            if (o_winner):
                print("Congratulation, " + self.player2.name + " win!")
                self.print_board()
                break

            # Check tie
            tie = self.check_tie()
            if tie:
                self.print_board()
                break

        self.clean_board()


    def move_player(self, name, tile):
        """Function to handle player O movement"""
        self.print_board()
        # Capture player O movement
        try:
            move = raw_input("Where do you want to move " + name + "? ")
            move = int(move) - int(1)
            # Check if the player inputs valid input i.e 0-8
            if move > -1 and move < 9:
                # Check if the space is empty or not
                if self.board[move] == " ":
                    self.board[move] = tile
                else:
                    print("The space is taken")
                    self.move_player(name, tile)
            else:
                print("Please write valid input i.e 1-9!")
                self.move_player(name, tile)
        # If user enter non-integer input
        except ValueError:
            print("Please write valid input i.e 1-9!")
            self.move_player(name, tile)

    __repr__ = __str__