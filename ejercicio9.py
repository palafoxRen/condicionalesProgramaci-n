#Programa que pida tres números y los muestre ordenados (de mayor a menor);

n1 = int(input('Ingrese el primero número: '))
n2 = int(input('Ingrese el segundo número: '))
n3 = int(input('Ingrese el tercer número: '))
if (n1>n2 and n2>3):
    print("",n1," - ",n2," - ",n3)
elif(n2>n1 and n1>n3):
    print("",n2," - ",n1," - ",n3)
elif(n3>n1 and n1>n2):
    print("",n3," - ",n1," - ",n2)   
elif(n3>n2 and n2>n1):
    print("",n3," - ",n2," - ",n1)   
elif(n1>n3 and n3>n2):
    print("",n1," - ",n3," - ",n2)   
elif(n2>n3 and n3>n1):
    print("",n2," - ",n3," - ",n1)
    