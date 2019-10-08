from cardgame import CardGame

class BlackJack(CardGame):

    def __init__(self,name):
        CardGame.__init__(self,name)
        self.maxPlayers = 5
        self.timeTill

    def whatsTheGame(self):
        print ("blackjack")

    def play(self):
        """ open messageQueue table
            Wait for players to connect
            - wait for game start (table full | Go signal )
            """
        pass

