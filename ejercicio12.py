#Realiza un programa que pida por teclado el resultado (dato entero) obtenido 
#al lanzar un dado de seis caras y muestre por pantalla el número en letras 
#(dato cadena) de la cara opuesta al resultado obtenido.
#* Nota 1: En las caras opuestas de un dado de seis caras están los números: 
#1-6, 2-5 y 3-4.
#* Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, 
#se mostrará el mensaje: "ERROR: número incorrecto.".

ntexto= {
    1: 'uno',
    2: 'dos',
    3: 'tres',
    4: 'cuatro',
    5: 'cinco',
    6: 'seis'
}

def opuesto(num):
    if num == 1:
        return 6
    elif num == 2:
        return 5
    elif num == 3:
        return 4
    elif num == 4:
        return 3
    elif num == 5:
        return 2
    elif num == 6:
        return 1
n = int(input('Ingresa el resultado del dado (1-6): '))

if 1 <= n <= 6:
    nopuesto= opuesto(n)
    print(f'El número opuesto es: {ntexto[nopuesto]}')
else:
    print('ERROR: número incorrecto.')