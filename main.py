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


def game_two_players():
    player_one = inital_cards()
    player_two = inital_cards()
    waiting(0)
    tux('Escribe ahora el nombre del primer jugador: ')
    name_player_one = input('Mi nombre es: ')
    tux('Escribe ahora el nombre del segundo jugador: ')
    name_player_two = input('Mi nombre es: ')
    is_player_one = choice([name_player_one,name_player_two])
    if is_player_one == name_player_one:
        is_player_two = name_player_two
    else:
        is_player_two = name_player_one
    waiting(0)
    tux('El jugador que va a empezar es...')
    waiting(5)
    tux(f'{is_player_one.upper()} es el primero en jugar. {is_player_two.upper()} te toca retirarte hasta que el primero en jugar termine su turno.')
    waiting(8)
    tomar_carta = 's'
    while tomar_carta == 's':
        waiting(0)
        print('Estas son tus cartas:')
        show_cards_player(player_one)
        tomar_carta = input(f'Quieres tomar otra carta? sumas un total de {points(player_one)} puntos actualmente. (s/n) ').lower()
        if tomar_carta == 's':
            if len(player_one) != 30:
                eleccion = take_card(tomar_carta,player_one,player_two)
                player_one.append(eleccion)
            else:
                print('Ya te haz acabado el maso... que conio ases loko?')
                waiting(10)
    waiting(0)
    tux(f'Bien, ahora que ya a terminado el turno del primer jugador, le toca a {is_player_two.upper()} de jugar')
    stop = input('Presiona enter para continuar')
    tomar_carta = 's'
    while tomar_carta == 's':
        waiting(0)
        print('Estas son tus cartas:')
        show_cards_player(player_two)
        tomar_carta = input(f'Quieres tomar otra carta? sumas un total de {points(player_two)} puntos actualmente. (s/n) ').lower()
        if tomar_carta == 's':
            if len(player_two) != 30-len(player_one):
                eleccion = take_card(tomar_carta,player_one,player_two)
                player_two.append(eleccion)
            else:
                print('Ya te haz acabado el maso... que conio ases loko?')
                waiting(10)
    winner = result(player_one,player_two)
    waiting(0)
    if winner == 'TIE':
        print(f'Las cartas de {is_player_one} han sido:')
        show_cards_player(player_one)
        waiting(5)
        print(f'Las cartas de {is_player_two} han sido:')
        show_cards_player(player_two)
        waiting(5)
        print(f'''El total de puntos del jugador {is_player_one.upper()} es de {points(player_one)}.
Mientras que el total de puntos del jugador {is_player_two.upper()} es de {points(player_two)}.
Por lo que al final el ganador es...j''')
        waiting(8)
        tux('Los dos han empatado :0!!!')
        again = input('Quieren volver a jugar? (s/n) ').lower()
        return again
    elif winner == True:
        print(f'Las cartas de {is_player_one} han sido:')
        show_cards_player(player_one)
        waiting(5)
        print(f'Las cartas de {is_player_two} han sido:')
        show_cards_player(player_two)
        waiting(5)
        print(f'''El total de puntos del jugador {is_player_one.upper()} es de {points(player_one)}.
Mientras que el total de puntos del jugador {is_player_two.upper()} es de {points(player_two)}.
Por lo que al final el ganador es...''')
        waiting(8)
        tux(f'Jugador {is_player_one}...')
        waiting(2,Clean_screen=False)
        print(WINNER)
        again = input('Quieren volver a jugar? (s/n) ').lower()
        return again
    elif winner == False:
        print(f'Las cartas de {is_player_one} han sido:')
        show_cards_player(player_one)
        waiting(5)
        print(f'Las cartas de {is_player_two} han sido:')
        show_cards_player(player_two)
        waiting(5)
        print(f'''El total de puntos del jugador {is_player_one.upper()} es de {points(player_one)}.
Mientras que el total de puntos del jugador {is_player_two.upper()} es de {points(player_two)}.
Por lo que al final el ganador es...j''')
        waiting(8)
        tux(f'Jugador {is_player_two}...')
        waiting(2,Clean_screen=False)
        print(WINNER)
        again = input('Quieren volver a jugar? (s/n) ').lower()
        return again
        


def main():
    try:
        introduccion()
    except KeyboardInterrupt :
        pass
    jugar = 's'
    while jugar == 's':
        waiting(0)
        tux('Selecciona el modo de juego:')
        print('''Jugador vs Maquina = 
Jugador vs Jugador = 2
Salir del juego = 3''')
        modo = int(input('Mi modo de juego será... '))
        if modo == 1:
            otra_vez_modo = 's'
            while otra_vez_modo == 's':
                otra_vez_modo = game()
        elif modo == 2:
            otra_vez_modo = 's'
            while otra_vez_modo == 's':
                otra_vez_modo = game_two_players()
        else:
            jugar = 'n'
    waiting(0)
    tux('Pues aquí se partio una jerga...')
    waiting(5,False)
    tux('Y cada quien alv')
    waiting(5)
    tux('Gracias por jugar!!!')


if __name__ == '__main__':
    main()