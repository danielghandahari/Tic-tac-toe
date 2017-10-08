# ------------------------------------------------------------------------------
# -- File Name:       player.py
# -- University:      Uppsala University
# -- Department:      Information Technology
# -- Course:          Software Engineering and Project Management
# -- Project:         Tic-Tac-Toe         
# -- Author:          Group D
# -- Description:     In this class implement the player handling. 
# --                  It handles players attributes i.e name, human ior AI, and AI level.
# ------------------------------------------------------------------------------

class Player:

    def __init__(self):
        self.name = None
        self.isAI = None
        self.level = None
        self.Moves = 5

    def __str__(self):
        str =  "Players name is: " + self.name + "\n"

        if(self.isAI):
            return str + " and is AI with level %d  \n" % self.level

        return str