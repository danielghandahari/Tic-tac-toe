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

import os
from GameEngine import GameEngine
from random import randint

class Plattform:


    def __init__(self):
        self.quitGame = False
        self.player1 = None
        self.player2 = None
        self.winner = None
        self.gameEngine = None
        self.board = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]
        ''' Need this for the AI players '''
        self.winningCombinations = (
            [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        )

    def __str__(self):
        return self.player1.name + " VS " + self.player2.name

    """
    Function: Print out the number of moves each players has left.
    Argument: A int which decides which turn it is. 1 for Player 1 and 2 for player 2.
    """
    def print_players_moves_left(self,playersTurn):

        print("")
        print("")

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
        winnersName = ""
        playerNumber = 0
        while True:
            # Player 2 has give up so Player 1 wins the game.
            if self.quitGame:
                self.print_board()
                winnersName = self.player1.name
                break
            # Print out number of moves the players has left.
            self.print_players_moves_left(0)
            # set which players turn it is and move player.
            playerNumber = 1
            self.move_player(self.player1.name, "X", playerNumber)
            # Check if player X wins
            x_winner = self.check_winner("X")
            if(x_winner):
                self.print_board()
                winnersName = self.player1.name
                break

            # Check tie
            tie = self.check_tie()
            if tie:
                self.print_board()
                """"
                self.clean_board()
                self.player1.Moves = 5
                self.player2.Moves = 5
                self.winner = None
                self.start_match()
                """
                winnersName = ""
                break

            # Player 1 has give up so Player 2 wins the game.
            if self.quitGame:
                self.print_board()
                winnersName = self.player2.name
                break
            # Print out number of moves the players has left.
            self.print_players_moves_left(1)
            # set which players turn it is and move player.
            playerNumber = 2
            self.move_player(self.player2.name, "O", playerNumber)
            # Check if player O wins
            o_winner = self.check_winner("O")
            if (o_winner):
                self.print_board()
                winnersName = self.player2.name
                break

            # Check tie
            tie = self.check_tie()
            if tie:
                winnersName = ""
                self.print_board()
                break
        self.quitGame = False
        # Moves are restored for ties
        self.player1.Moves = 5
        self.player2.Moves = 5
        self.clean_board()
        return winnersName

    '''********************************************************************'''
    ''' Functions that are required to get the component GameEngine to work'''

    '''
    This function returns the board updated with the new AI move. Depending on the difficulty chosen
    different AIs will be used.
    Param: AIlevel (int) the difficulty of the AI, can be a number between 1 and 3
    Param: player (int) who the current player is, should be either the number 1 or 2
    Return: board (list). If invalid player or AIlevel function returns 0
    '''

    def AImove(self, AIlevel, playerNumber, tile):
        AI = GameEngine()

        '''if player != 1 and player != 2:
            return 0
        '''

        if AIlevel == 1:
            move = AI.getAImove1(self)
            self.board[move] = tile
            os.system('clear')
            return
        elif AIlevel == 2:
            move = AI.getAImove2(playerNumber, self)
            self.board[move] = tile
            os.system('clear')
            return
        elif AIlevel == 3:
            move = AI.getAImove3(playerNumber, self)
            self.board[move] = tile
            os.system('clear')
            return
        else:
            return 0

    def checkWinner(self):
        for combination in self.winningCombinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] == 1:
                return 1
            elif self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] == 2:
                return 2
        return 0

    def updateBoard(self, move, player):
        self.board[move - 1] = player
        return self

    '''
    This function checks if the move is valid.
    Return: Bool
    '''

    def checkValidMove(self, move):
        if self.board[move] == " ":
            return True
        return False

    def anySpaceLeft(self):
        for tile in range(0, 8):
            if self.board[tile] == " ":
                return True
        return False

    ''' End of GameEngine help functions '''
    '''********************************************************************'''

    def move_player(self, name, tile, playerNumber):
        """
        Function: Handle the players movement
        """
        self.print_board_instruction()
        self.print_board()

        # Check if the player is a AI and which turn the player has.
        if playerNumber == 1 and self.player1.isAI:
            self.AImove(self.player1.level, playerNumber, tile)
        elif playerNumber == 2 and self.player2.isAI:
            self.AImove(self.player2.level, playerNumber, tile)

        else:
            # Capture player movement
            try:
                print "Enter Q if you want to quit the game."
                move = raw_input("Where do you want to move " + name + "? ")
                #Option to end the game.
                if move == "q" or move == "Q":
                    self.quitGame = True
                    return
                move = int(move) - int(1)
                # Check if the player inputs valid input i.e 0-8
                if move > -1 and move < 9:
                    # Check if the space is empty or not
                    if self.board[move] == " ":
                        self.board[move] = tile
                        os.system('clear')
                    else:
                        os.system('clear')
                        print("\nThe space is taken!\n")
                        self.move_player(name, tile, playerNumber)
                else:
                    print("Please write valid input i.e 1-9!")
                    self.move_player(name, tile, playerNumber)
                    os.system('clear')
            # If user enter non-integer input
            except ValueError:
                print("Please write valid input i.e 1-9!")
                self.move_player(name, tile, playerNumber)
                os.system('clear')

    __repr__ = __str__