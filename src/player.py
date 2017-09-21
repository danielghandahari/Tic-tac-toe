class Player:

    def __init__(self):
        self.name = None
        self.isAI = None
        self.level = None

    def __str__(self):
        return "Players name is: " + self.name