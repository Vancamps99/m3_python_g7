recordatorios = [
    ['2021-01-01', "11:00", "Levantarse y ejercitar"],
    ['2021-05-01', "15:00", "No trabajar"],
    ['2021-07-15', "13:00", "No hacer nada es feriado"],
    ['2021-09-18', "16:00", "Ramadas"],
    ['2021-12-25', "00:00", "Navidad"]
]
#modificando la lista
# Paso 1 Agregando un evento a los recordatorios
recordatorios.append(['2021-01-02', '06:00', 'Empezar el Año'])
print("añadiendo una fecha\n",recordatorios)
print()
# Paso2 modificar elemento de la lista
recordatorios[2] = ['2021-07-16', '13:00', 'No hacer nada es feriado']
print("modificando elemento en posicion dos de la lista\n",recordatorios)
print()
# Paso3 Eliminar elemento de la lista
del recordatorios[1]  
print("Eliminando elemento posicion 1 de la lista",recordatorios)
print()
#agregando tanto cena de navidad y cena año nuevo
recordatorios.append(['2021-12-24', '22:00', 'Cena de Navidad'])  
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])  
print("Añadiendo ultimos eventos a el recordatorio ",recordatorios)#mostrara una lista desordenada
print("\n")
recordatorios.sort()#ordeno por fecha pero debo ejercitar al mover elemntos con pop e insert
# Imprimir el calendario actualizado y final
print("Calendario Actualizado y final:", recordatorios)

