from ascii_art import POKER_HAND,All_cards
from os import system
from time import sleep
from cowsay import tux
from getpass import getuser
from random import choice



def waiting(Time,Clean_screen=True):
    sleep(Time)
    if Clean_screen == True:
        system('clear')


def change_az(lista:list)->int:
    i = 0
    for point in lista:
        if point == 11:
            if sum(lista) > 21:
                lista[i] = 1
            else:
                pass
        i+=1
    return lista


def addcoma(letra:list)->list:
    if len(letra) == 0:
        return letra
    elif letra[len(letra)-1] == ',':
        return letra
    else:
        letra += ','
        return letra


def join_list(lista:list)->list:
    lista = "".join(lista)
    return lista


def take_card(dic:dict)->list:
    i=0
    todes_cartes = dict(All_cards)
    for card in All_cards:
        if dic.get(card) != None:
            del todes_cartes[card]
    for xd in todes_cartes:
        print(xd)



def tutotrial():
    pass


def introduccion():
    tux(f'Bienvendio {getuser().capitalize()}!!!')
    waiting(5)
    tux('En estaocación, vamos a jugar BlackJack!!!')
    print(POKER_HAND)
    waiting(5)
    tux('Antes de empezar... Sabes como jugar?')
    print('''Si se jugar = S
No sé jugar = N''')
    tuto = input('La verdad es que...').lower()
    if tuto == 's':
        waiting(0,Clean_screen=False)
        tux('Excelente, entonces empezemos con el juego')
    else:
        tutotrial()



if __name__ == '__main__':
    pass