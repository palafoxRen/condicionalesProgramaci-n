#La política de cobro de una compañía telefónica es: cuando se realiza una 
#llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros 
#cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos,
#los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
#Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno
#de mañana, 15 %, y en turno de tarde, 10 %. 
#Realice un programa para determinar cuánto debe pagar por cada concepto 
#una persona que realiza una llamada.

call = float(input('Minutos: '))
time = str(input('Ingrese el tiempo: horario mañana o tarde o el día domingo: '))

domingo = call/100*3
mañana = call/100*15
tarde = call/100*10

precio1 = 11*1
precio2 = 11*0.8
precio3 = 11*0.7
precio4 = 11*0.5

if call>=0 and call<=5 and time=='mañana':
    print(f'El costo de la llamada es {precio1 + mañana} euros')
elif call>=0 and call<=5 and time== 'tarde':
    print(f'El costo de la llamada es {precio1 + tarde} euros')
elif call>=0 and call<=5 and time== 'domingo':
    print(f'El costo de la llamada es {precio1 + domingo} euros')

elif call>=5 and call<=8 and time=='mañana':
    print(f'El costo de la llamada es {precio2 + mañana} euros')
elif call>=5 and call<=8 and time== 'tarde':
    print(f'El costo de la llamada es {precio2 + tarde} euros')
elif call>=5 and call<=8 and time== 'domingo':
    print(f'El costo de la llamada es {precio2 + domingo} euros')

elif call>=8 and call<=10 and time=='mañana':
    print(f'El costo de la llamada es {precio3 + mañana} euros')
elif call>=8 and call<=10 and time== 'tarde':
    print(f'El costo de la llamada es {precio3 + tarde} euros')
elif call>=8 and call<=10 and time== 'domingo':
    print(f'El costo de la llamada es {precio3 + domingo} euros') 

elif call>=10 and time=='mañana':
    print(f'El costo de la llamada es {precio4 + mañana} euros')
elif call>=10 and time== 'tarde':
    print(f'El costo de la llamada es {precio4 + tarde} euros')
elif call>=10 and time== 'domingo':
    print(f'El costo de la llamada es {precio4 + domingo} euros')