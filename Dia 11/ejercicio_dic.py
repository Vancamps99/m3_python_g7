#Crear diccionario

cumpleaños={
 "Septiembre":8,
 "Agosto":15,

}
#agregar fecha dia
cumpleaños["Noviembre"]=15
cumpleaños ["Enero"]=2
#mostrar 
print(cumpleaños)
#modificar clave
cumpleaños["Noviembre"]=6
print(cumpleaños)
del cumpleaños ["Enero"]
print("Diccionario actualizado",cumpleaños)