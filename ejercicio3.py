# Escribe un programa que lea un número e indique si es par o impar

n = int(input("Escribe un número: "))
if n % 2 == 0:
    print(n, "es par.")
else:
    print(n, "es impar.")