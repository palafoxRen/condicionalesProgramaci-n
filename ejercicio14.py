#Escribe un programa que pida un número entero entre uno y doce e imprima el 
#número de días que tiene el mes correspondiente.
# Si introducimos otro número nos da un error.

mes = int(input('Ingrese un número del 1 al 12: '))
if mes == 1:
   print ('Corresponde a enero. Tiene 31 días.')
elif mes == 2:
   print ('Corresponde a febrero. Tiene 28 días.')
elif mes == 3:
   print ('Corresponde a marzo. Tiene 31 días.')
elif mes == 4:
   print ('Corresponde a abril. Tiene 30 días.')
elif mes == 5:
   print ('Corresponde a mayo. Tiene 31 días.')  
elif mes == 6:
   print ('Corresponde a junio. Tiene 30 días.') 
elif mes == 7:
   print ('Corresponde a julio. Tiene 31 días.')
elif mes == 8:
   print ('Corresponde a agosto. Tiene 30 días.')  
elif mes == 9:
   print ('Corresponde a septiembre. Tiene 31 días.')
elif mes == 10:
   print ('Corresponde a octubre. Tiene 31 días.')
elif mes == 11:
   print ('Corresponde a noviembre. Tiene 30 días.')      
elif mes == 12:
   print ('Corresponde a diciembre. Tiene 31 días.')           
else:   
   print ('ERROR. Número inválido!')   