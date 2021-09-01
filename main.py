import random
from general_functions import *
from cowsay import tux
from ascii_art import *
from time import time


def introduccion():
    tux('Bienvendio al BlackJack!!!')
    waiting(5)


def game():
    introduccion()


def main():
    game()


if __name__ == '__main__':
    main()