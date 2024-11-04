#Realiza un programa que pida el dí­a de la semana (del 1 al 7) y escriba 
#el dí­a correspondiente. 
# Si introducimos otro número nos da un error.

d = int(input('Ingrese el número del día de la semana: '))
if d == 1:
   print ('Lunes')
elif d == 2:
   print ('Martes')
elif d == 3:
   print ('Miércoles')
elif d == 4:
   print ('Jueves')   
elif d == 5:
   print ('Viernes') 
elif d == 6:
   print ('Sábado')
elif d == 7:
   print ('Domingo') 
else:
   print ('ERROR. Número inválido!')         