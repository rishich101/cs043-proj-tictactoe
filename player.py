# This file will create player class.

# Player class creates an object with player id.
class Player:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return "Player {}".format(self.type)