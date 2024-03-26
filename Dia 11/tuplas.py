"""
Tuplas 

conjunto de datos ordenados e inmutables
se escriben con parentesis()
"""

tupla1=(1,3,5,7,9)
print(tupla1)
print(type(tupla1))#  <class 'tuple'>
tupla2=("nombre","Alberto")

nomb,caracter=tupla2
print(nomb)
print(caracter)
print(tupla2[0])#arroja nombre
print(tupla2[1])#arroja caracter
#print(tupla2[2])#arroja error   tuple index out of range

#a las tuplas no se les puede modificar (agregar o quitar elementos)
#tupla2[2]="hola" #arroja error TypeError: 'tuple' object does not support item assignment
print("")
#iterar tupla
for num in tupla1:
    print(num)



dicc1 = list({"nota1":5,"nota2":6}.items() )   #si quiero transformar un diccionario a una lista antes de mencionar el diccionario se pone list
print(dicc1)#[('nota1', 5), ('nota2', 6)]
print(dicc1[0])
print(dicc1[1])
print()
#"nota 1","5"
#"nota 2","6"
print(dicc1[0][0])#nota 1
print(dicc1[0][1])#nota5
print(dicc1[1][0])#2
print(dicc1[1][1])#6