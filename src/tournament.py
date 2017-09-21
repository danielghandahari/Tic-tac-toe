import random

from plattform import Plattform


class Tournament:

    def __init__(self, players):

        self.amount_of_players = players.__len__()


        tournament_tree = []

    # TODO andra players till self.players??
    def create_tournament_tree(self, players):

        shuffled_players_list = random.shuffle(players)

        tournament_tree = []

        i = shuffled_players_list.__len__()
        print "LEENGTH: " + i
        while i > 0:
            plattform = Plattform()
            plattform.player1 = shuffled_players_list[i]
            plattform.player2 = shuffled_players_list[i+1]

            tournament_tree.append([plattform])
            --i

