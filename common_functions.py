from os import system
from time import sleep


def waiting(Time,Clean_screen=True):
    sleep(Time)
    if Clean_screen == True:
        system('clear')

if __name__ == '__main__':
    pass