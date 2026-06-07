def pedir_entero_positivo(mensaje):
    while True:
        try:
            valor=int(input(mensaje))
        except ValueError:
            print('Por favor, ingrese un numero valido.')
        else:
            if valor > 0:
                return valor
            else:
                print('Por favor, ingrese un numero positivo.')

cultivo=input('Cual es el nombre del cultivo? ').lower()
dias=pedir_entero_positivo('Cuantos dias se van a registrar? ')

kilosrecogidos=[]
for i in range(dias):
    kilos=pedir_entero_positivo('Cuantos kilos se recogieron el dia ' + str(i+1) + '? ')
    kilosrecogidos.append(kilos)
    
total=0
for kilos in kilosrecogidos:
    total+=kilos
print(f'En total se recogieron {total} kilos de {cultivo}') 
promedio=total/dias
print(f'El promedio de kilos recogidos por dia es {promedio:.2f} kilos') 
diamayor=kilosrecogidos[0]
for i in range(len(kilosrecogidos)):
    if kilosrecogidos[i]>diamayor:
        diamayor=kilosrecogidos[i]
print(f'El dia que se recogieron mas kilos fue el dia {kilosrecogidos.index(diamayor)+1} con {diamayor} kilos')
if promedio > 100:
    print('Buena temporada')
elif promedio > 50:
    print('Temporada normal')
else:
    print('Temporada baja')