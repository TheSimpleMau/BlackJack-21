from making_cards import *

POKER_HAND = '''
             __                                               
        _..-''--'----_.                                        
      ,''.-''| .---/ _`-._                                     
    ,' \ \  ;| | ,/ / `-._`-.                                  
  ,' ,',\ \( | |// /,-._  / /                                  
  ;.`. `,\ \`| |/ / |   )/ /                                   
 / /`_`.\_\ \| /_.-.'-''/ /                                    
/ /_|_:.`. \ |;'`..')  / /                                     
`-._`-._`.`.;`.\  ,'  / /                                      
    `-._`.`/    ,'-._/ /                                       
      : `-/     \`-.._/                                        
      |  :      ;._ (                                          
      :  |      \  ` \                                         
       \         \   |                                         
        :        :   ;                                         
        |           /                                          
        ;         ,'                                           
       /         /                                             
      /         /                                              
               /          
'''

#Código para cambiar nombres y generar diccionario con todas las cartas
tipo = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
valor = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

All_cards = {}
for nombe_carta in tipo:
    if nombe_carta == 'Spades':
        new_name = 'Espadas'
    elif nombe_carta == 'Diamonds':
        new_name = 'Diamantes'
    elif nombe_carta == 'Hearts':
        new_name = 'Corazones'
    elif nombe_carta == 'Clubs':
        new_name = 'Trebol'
    for nombre_valor in valor:
        if nombre_valor == 'Ace':
            new_name_two = 'Az'
        elif nombre_valor == 'Jack':
            new_name_two = 'Jota'
        elif nombre_valor == 'Queen':
            new_name_two = 'Reina'
        elif nombre_valor == 'King':
            new_name_two == 'Rey'
        else:
            new_name_two = nombre_valor
        All_cards.update({f'{new_name} {new_name_two}':ascii_version_of_card(Card(nombe_carta,nombre_valor))})


if __name__ == '__main__':
    pass