from common_functions import *
from ascii_art import *
from cowsay import tux


def game():
    waiting(0)
    cards_player = inital_cards()
    cards_machine = inital_cards()
    print('Tus cartas son:')
    show_cards_player(cards_player)
    waiting(5,False)
    print(f'''Las cartas de la computadora son:
{All_cards[cards_machine[0]]}''')
    print(ascii_version_of_hidden_card(Card('Diamonds', '4')))#Para ocultar todas las cartas menos la primera
    tomar_carta = 's'
    waiting(5)
    while tomar_carta == 's':
        waiting(0)
        print('Tus cartas:')
        show_cards_player(cards_player)
        tomar_carta = input(f'Quieres tomar otra carta? sumas un total de {points(cards_player)} puntos actualmente. (s/n) ').lower()
        if tomar_carta == 's':
            if len(cards_player) != 32:
                eleccion = take_card(tomar_carta,cards_player,cards_machine)
                cards_player.append(eleccion)
            else:
                print('Ya te haz acabado el maso... que conio ases loko?')
                waiting(10)
        else:
            cards_machine = take_cards_machine(cards_player,cards_machine)
    winner = result(cards_player,cards_machine)
    if winner == 'TIE':
        print('Las cartas de la maquina han sido...')
        show_cards_player(cards_machine)
        print(f'Sumando un total de {points(cards_machine)} puntos, por lo que...')
        waiting(8)
        print(TIE)
        again = input('Quieres volver a jugar? (s/n) ').lower()
        return again
    elif winner == True:
        print('Las cartas de la maquina han sido...')
        show_cards_player(cards_machine)
        print(f'Sumando un total de {points(cards_machine)} puntos, por lo que...')
        waiting(8)
        print(WINNER)
        again = input('Quieres volver a jugar? (s/n) ').lower()
        return again
    elif winner == False:
        print('Las cartas de la maquina han sido...')
        show_cards_player(cards_machine)
        print(f'Sumando un total de {points(cards_machine)} puntos, por lo que...')
        waiting(8)
        print(LOSER)
        again = input('Quieres volver a jugar? (s/n) ').lower()
        return again


def main():
    introduccion()
    jugar = 's'
    while jugar == 's':
        jugar = game()
    waiting(0)
    tux('Pues aquí se rompio una jerga...')
    waiting(5,False)
    tux('Y cada quien alv')
    waiting(5)
    tux('Gracias por jugar!!!')


if __name__ == '__main__':
    main()