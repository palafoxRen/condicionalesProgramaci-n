# Realiza un programa que calcule la potencia, para ello pide por teclado 
# la base y el exponente. Pueden ocurrir tres cosas:
# * El exponente sea positivo, sólo tienes que imprimir la potencia.
# * El exponente sea 0, el resultado es 1.
# * El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

n = int(input('Ingresa un número: '))
exp = int(input('Escribe su exponente: '))
if n > 0:
   print( n ** exp)
elif exp == 0:
   print ('1')
else:
   print(n ** abs(exp))