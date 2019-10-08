
class CardGame:
    def __init__(self,game):
        self.game = game

    def printname(self):
        print(self.game)

    def play(self):
        pass  # abstract defined by child
