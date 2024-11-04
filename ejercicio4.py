# Crea un programa que pida al usuario dos números y muestre su división 
# si el segundo no es cero, o un mensaje de aviso en caso contrario.

n1 = float (input("Ingresa un número: "))
n2 = float (input("Ingresa un número: "))
if n2 == 0:
   print ('RESULTADO INVÁLIDO')
else:
   print (n1/n2)