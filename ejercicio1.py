print ('Programa que lee dos números')
print('Nos dice cual es mayor')
num1 = int(input('Ingresa un número: '))
num2 = int(input('Ingresa otro número: '))
if num1 > num2:
    print(f'El { num1 } es mayor')   
elif num1 < num2:        
    print(f'El { num2 } es mayor')       
else: 
    print('Los números son iguales')