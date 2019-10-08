
import logging
import logging.config

from blackjack import BlackJack

def main():
    # logging.config.fileConfig(fname='../../conf/logging.conf', disable_existing_loggers=False)
    logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')

    # Get the logger specified in the file
    logger = logging.getLogger(__name__)

    logger.debug('This is a debug message')

    game = BlackJack("blackjack1")
    game.printname()
    game.whatsTheGame()
    game.play()

if __name__ == "__main__":
    print("start\n")
    main()


