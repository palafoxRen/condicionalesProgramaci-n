# Programa que pida un número y diga si es positivo, negativo o 0.

n1 = input("Escribe un número: ")
numero = int(n1)
if numero == 0:
    print("Tu número es 0")
elif numero < 0:
    print("Tu número es negativo")
else:
    print("Tu número es positivo")