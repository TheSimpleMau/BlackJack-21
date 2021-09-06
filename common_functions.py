from ascii_art import *
from os import system
from time import sleep
from cowsay import tux
from getpass import getuser
from random import choice


tipo = ['Espadas','Diamantes','Corazones','Trebol']
valor = ['As','2','3','4','5','6','7','8','9','10','Jota','Reina','Rey']
Todas_cartas = []
for tipe in tipo:
    for value in valor:
        Todas_cartas.append(tipe+' '+value)

def waiting(Time,Clean_screen=True)->None:
    sleep(Time)
    if Clean_screen == True:
        system('clear')


def show_cards_player(cards_player:list)->None:
    for i in cards_player:
        print(All_cards[i])


def inital_cards()->list:
    cards = [choice(tipo)+' '+choice(valor)]+[choice(tipo)+' '+choice(valor)]
    return cards


def points(cartas:list)->int:
    cartas = "".join(cartas)
    puntos = []
    i=0
    for num in cartas:
        if num == '1':
            puntos.append(10)
        elif num == '2' or num == '3' or num == '4' or num == '5' or num == '6' or num == '7' or num == '8' or num == '9':
            puntos.append(int(num))
        elif num == ' ':
            if cartas[i+1] == 'A':
                if sum(puntos)+11 <= 21:
                    puntos.append(11)
                else:
                    puntos.append(1)
            if cartas[i+1] == 'J' or cartas[i+1] == 'R':
                puntos.append(10)
        i+=1
    return sum(puntos)


def take_card(desicion:str,cartas_jugador:list,cartas_maquina:list)->str:
    if desicion == 's':
        quitando_cartas = list(Todas_cartas)
        for k in cartas_maquina:
            if k in quitando_cartas:
                quitando_cartas.remove(k)
        for i in cartas_jugador:
            if i in quitando_cartas:
                quitando_cartas.remove(i)
        if len(quitando_cartas) != 0:
            return choice(quitando_cartas)
        else:
            return []
    else:
        return []


def take_cards_machine(cartas_jugador:list,cartas_maquina:list)->list:
    i = 0
    while points(cartas_maquina) < 17:
        quitando_cartas = list(Todas_cartas)
        for k in cartas_maquina:
            if k in quitando_cartas:
                quitando_cartas.remove(k)
        for i in cartas_jugador:
            if i in quitando_cartas:
                quitando_cartas.remove(i)
        cartas_maquina.append(choice(quitando_cartas))
    return cartas_maquina


def result(cartas_jugador:list,cartas_maquina:list):
    puntos_jugador = points(cartas_jugador)
    puntos_maquina = points(cartas_maquina)
    if puntos_jugador == puntos_maquina:
        return 'TIE'
    elif puntos_jugador > puntos_maquina:
        if puntos_jugador <= 21:
            return True
        else:
            return False
    elif puntos_maquina > puntos_jugador:
        if puntos_maquina <= 21:
            return False
        else:
            return True


def tutotrial():
    tux('Jugar BlackJack es muy fácil')
    waiting(7)
    tux('Lo único que tienes que hacer es juntar cartas hasta que tengas un total de 21 puntos o menos')
    waiting(7)
    tux('Si te pasas de 21 y tu oponente no, entonces pierdes')
    waiting(7)
    tux('E igual, el jugador que esté más cerca de 21, entonces ganará')
    waiting(7)
    tux('Listo, ahora ya sabes jugar, vamos a ello')
    waiting(7)


def introduccion():
    tux(f'Bienvendio {getuser().capitalize()}!!!')
    waiting(5)
    tux('En esta ocación, vamos a jugar BlackJack!!!')
    print(POKER_HAND)
    waiting(5)
    tux('Antes de empezar... Sabes como jugar?')
    print('''Si se jugar = S
No sé jugar = N''')
    try:
        tuto = input('La verdad es que... ').lower()
    except AssertionError:
        tux('Escribe solo S para sí y N para no. Daré por hecho que no sabes jugar >:|')
        waiting(7)
        tuto = 'n'
    if tuto == 's':
        tux('Excelente, entonces empezemos con el juego')
        waiting(5,False)
    else:
        tutotrial()



if __name__ == '__main__':
    pass