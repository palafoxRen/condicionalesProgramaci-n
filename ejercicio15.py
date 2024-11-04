# Juego Piedra Papel y Tijera
# Programa que lea las opciones de 2 jugadores, y muestra el resultado
# Empate, gana jugador 1 o gana jugador 2
# Si introducimos una opción que no coindica con piedra, papel o tijera
# Diga que opción Incorrecta

player1 = str(input('Primer jugador, elige piedra, papel o tijera: '))
player2 = str(input('Segundo jugador, elige piedra, papel o tijera: '))

if player1 == player2:
    print('Jugadores empatados')
elif (player1 == 'piedra' and player2 == 'tijera') or \
     (player1 == 'tijera' and player2 == 'papel') or \
     (player1 == 'papel' and player2 == 'piedra'):
    print('El jugador 2 GANA1')
elif (player2 == 'piedra' and player1 == 'tijera') or \
     (player2 == 'tijera' and player1 == 'papel') or \
     (player2 == 'papel' and player1 == 'piedra'):
     print('El jugador 2 GANA!')
else: 
    print('Opción INCORRECTA')         