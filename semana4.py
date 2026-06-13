from datetime import date, timedelta
import statistics

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
fecha_inicio=input('Ingrese la fecha de inicio de la cosecha (YYYY-MM-DD): ')
dias=pedir_entero_positivo('Cuantos dias recogio fruta? ')
calendario=[]
for i in range(dias):
    fecha_cosecha = date.fromisoformat(fecha_inicio) + timedelta(days=i)
    calendario.append(fecha_cosecha)

kilosrecogidos=[]
for i in range(dias):
    kilos=pedir_entero_positivo('Cuantos kilos se recogieron el dia ' + str(i+1) + '? ')
    kilosrecogidos.append(kilos)
    
dias_con_kilos = dict(zip(calendario, kilosrecogidos))

print('Resumen de kilos recogidos por dia:')    
for fecha, kilos in dias_con_kilos.items():
    print(f'El {fecha}: {kilos} kilos')

total=0
for kilos in kilosrecogidos:
    total+=kilos
print(f'En total se recogieron {total} kilos de {cultivo}') 
media=statistics.mean(kilosrecogidos)
diamayor=kilosrecogidos[0]
for i in range(len(kilosrecogidos)):
    if kilosrecogidos[i]>diamayor:
        diamayor=kilosrecogidos[i]
print(f'El dia que se recogieron mas kilos fue el dia {kilosrecogidos.index(diamayor)+1} con {diamayor} kilos')
if media > 100:
    print('Buena temporada')
elif media > 50:
    print('Temporada normal')
else:
    print('Temporada baja')

print(f'La mediana de kilos recogidos por dia es {statistics.median(kilosrecogidos)} kilos')
print(f'La desviacion estandar de kilos recogidos por dia es {statistics.stdev(kilosrecogidos):.2f} kilos')
print(f'La media de kilos recogidos por dia es {media:.2f} kilos')