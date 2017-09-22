import random

from plattform import Plattform


class Tournament:

    def __init__(self, players):

        self.players = players
        self.tournament_tree = self.create_tournament_tree()



    def create_tournament_tree(self):

        random.shuffle(self.players)

        """
        check if odd, then add ai, here!
        """

        tournament_tree = []

        i = 0
        while i < len(self.players):
            plattform = Plattform()
            plattform.player1 = self.players[i]
            plattform.player2 = self.players[i+1]
            tournament_tree.append([plattform])
            i = i + 2

        return tournament_tree

    def print_welcome_message(self):
        print "\n\n######################################"
        print "########## Let the games begin! ######"
        print "######################################\n\n"

    def print_tournament(self):

        self.print_welcome_message()
        for plattform in self.tournament_tree:

            print "---------" + str(plattform)

            # Checks if player is last
            if(plattform is self.tournament_tree[len(self.tournament_tree)-1]):
                break

            for i in range(0,8):
                print "|"