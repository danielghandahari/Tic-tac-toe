# ------------------------------------------------------------------------------
# -- File Name:       plattform.py
# -- University:      Uppsala University
# -- Department:      Information Technology
# -- Course:          Software Engineering and Project Management
# -- Project:         Tic-Tac-Toe         
# -- Author:          Group D
# -- Description:     In this class implement the plattform handling. 
# --                  It handles the gameplay and check if the game is tie or has a winner. 
# ------------------------------------------------------------------------------


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

    """
    Function: Print out the number of moves each players has left.
    Argument: A int which decides which turn it is. 1 for Player 1 and 2 for player 2.
    """
    def print_players_moves_left(self,playersTurn):

        if playersTurn == 0:
            print "Moves left:"
            print self.player1.name +":",
            for x in range(0, self.player1.Moves):
                print("X"),
            print " "
            print self.player2.name +":",
            for x in range(0, self.player2.Moves-1):
                print("O"),
            self.player1.Moves -= 1
            print " "
        elif playersTurn == 1:
            print "Moves left:"
            print self.player1.name + ":",
            for x in range(0,  self.player1.Moves):
                print("X"),
            print " "
            print self.player2.name + ":",
            for x in range(0,  self.player2.Moves-1):
                print("O"),
            self.player2.Moves -= 1
            print " "

    def print_board(self):
        """
        Function: Print the game board
        """

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
        """
        Function: Create the game board instruction, so the user know where to move
        """

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
        """
        Function: Check the winner
        """

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
        """
        Function: Check if the game is tie
        """

        if (" " not in self.board):
            print("Tie! No player wins!")
            return True


    def clean_board(self):
        """
        Function: Provide a clean board
        """

        self.board = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]

    def start_match(self):

        """
        Function: handle the match
        """

        while True:

            # Print out number of moves the players has left.
            self.print_players_moves_left(0)
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

            # Print out number of moves the players has left.
            self.print_players_moves_left(1)
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
        """
        Function: Handle the players movement
        """
        self.print_board_instruction()
        self.print_board()
        # Capture player movement
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