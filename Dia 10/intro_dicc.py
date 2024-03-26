"""
DICCIONARIOS 
ESTRUCTURA de datos de pares clave:valor
se accede a los elementos a traves de la clave, no importando la posicion
las claves no se generan automaticamente,no hay un orden
claves pueden ser string,numerico,incluso boleano

!Si no se tiene un clave valor se crea sino , se reemplaza!
"""
notas={}
print(len(notas))
notas = {
"Camila": 7,
"Antonio": 5,
"Felipe": 6,
"Daniela": 5,
"Vicente": 7,
"Felipe":1

}
print(len(notas))
print(notas)
#acceso a valores
print(notas["Antonio"])
print(notas["Felipe"])#1 reemplaza al numero 7

#agregar un elemento a un diccionario
notas["Andres"] =4
print(notas)
#modificar por clave:valor (cambiar valor)
notas["Andres"]=5
print(notas)

#eliminar clave de un diccionario

del notas ["Andres"]
print(notas) #primera forma

#2da forma pop
eliminado=notas.pop("Camila")
print("valor eliminado",eliminado)
print(notas)

#unir diccionario  
#crear 2do dicci
notas2={
"Hernan":2,
"Eduardo":6,
"Felipe":3
}

#notas.update(notas2) #agrega la nota 2 al diccionario principal
#print(notas)
notas2.update(notas) #agrega la nota  al diccionario secundario
print(notas2)

#Colisiones :AL EXISTIR una dupla de valores (mismo valor) , se conserva el valor del diccionario que se unio
print(notas2.keys())
print( )
print (notas2.values())
print()
print(notas2.items())
print()
#get clave retonra el valor asociado a la clave         #none es un tipo de dato !NO ES VACIO!
print(notas2.get("Felipe"))

#consultar un valor que no existe
print()
print(notas2.get("Alfredo")) #none      es un tipo de dato !NO ES VACIO!
#se puede especificar el valor de retorno al no existir la clave
print(notas2.get("Alfredo","Valor no existente"))


