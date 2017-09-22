class Player:

    def __init__(self):
        self.name = None
        self.isAI = None
        self.level = None

    def __str__(self):
        str =  "Players name is: " + self.name + "\n"

        if(self.isAI):
            return str + " and is AI with level " + self.level + "\n"

        return str