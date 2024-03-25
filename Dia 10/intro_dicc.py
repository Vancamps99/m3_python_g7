"""
DICCIONARIOS 
ESTRUCTURA de datos de pares clave:valor
se accede a los elementos a traves de la clave, no importando la posicion
las claves no se generan automaticamente,no hay un orden
claves pueden ser string,numerico,incluso boleano
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