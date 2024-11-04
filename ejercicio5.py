# Escribe un programa que pida un nombre de usuario y una contraseña 
# y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", 
# sino se da un error.

user = str(input("Ingresa tu nombre de usuario: "))
password = str(input ("Ingresa tu contraseña: "))
if user == 'pepe' and password == "asdasd":
    print ("Has entrado correctamente!")
else:
    print ("Acceso denegado, usuario y contraseña invalidos!")