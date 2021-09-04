from common_functions import *
from cowsay import tux
from ascii_art import *
from time import time
from random import choices,choice




def game():
    cards_player = dict(choices(list(All_cards.items()),k=2))
    # cards_machine = choices(All_cards,k=2)
    kola = take_card(cards_player)
    


def main():
    # introduccion()
    game()


if __name__ == '__main__':
    main()
    # print(All_cards['Diamantes 3'])