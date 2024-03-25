"""
Listas
() ----> tuplas
{} ---->DICCIONARIO
[] ---->listas
especificaiones de listas
son contenedores 
son mutables
conjunto de datos, separados por coma,
 ordenados , segun su ingreso
 
"""
import os


lista_pares=[2,4,6,8,10,13] #tamaño lista 5 #modifica en el min 11 creo #tamaño 6
print(lista_pares)
#indice es la posicion que toma el dato desde [0,....] de cero hasta ...
#para saber las posicion de un elemento en este caso el inicial sera
print(len(lista_pares))#imprime el tamaño de la lista
print(lista_pares[0])
print(lista_pares[1])
print(lista_pares[2])
print(lista_pares[3])
print(lista_pares[4])
#print(lista_pares[5])#list index out of range
print("")
print(lista_pares[-1])#imprime el ultimo valor de la lista
print(lista_pares[-2])#imprime el penultimo elemento de la lista

lista_vacia=[] #tamaño cero

#metodos
print(lista_pares.__dir__)
print(lista_pares.__dir__())
print("")
#append(dato)=>agregar un elemento al final de la lista
#en este caso agregaremos un elemento a la lista vacia
lista_vacia.append("Lunes")
lista_vacia.append("martes")
lista_vacia.append("miercoles")
print(lista_vacia)
#metodo insert(indice) ==> inserta un elemento en una posicion especifica
lista_vacia.insert(3,"jueves")
print(lista_vacia)
lista_vacia.insert(3,"viernes") #ojo aca que no reemplaza el "jueves" lo dezplaza a la derecha y se ubica en la posicion de jueves
print(lista_vacia)
#para reemplazar la posicion de un elemento
lista_vacia[3]="jueves" #a la derecha del 3er elemento (miercoles) reemplaza el elemento jueves 
print(lista_vacia) 
#ojo que es distinto agregar o manipular elementos de listas en javascript y python hora 10 aprox
lista_vacia[4]="viernes"#luego del elemento 4 reemplaza el elemento a viernes !
print(lista_vacia)



#metodo pop
lista_vacia.pop() #saca el ultimo  elemento  de la lista
print(lista_vacia)#muestra hasta el jueves por que el viernes lo elimino
print("")
lista_vacia.pop(2)#como lunes ocupa pos #0 y martes pos#1 y miercoles !pos#2 elimina miercoles! no martes
print(lista_vacia)#ver 10:30

#remove (valor) ===>elimina el valor
lista_vacia.remove("martes")
print(lista_vacia)
lista_vacia.append("jueves")
print(lista_vacia)
lista_vacia.remove("jueves") #elimina la primera coincidencia de izquierda a derecha
print(lista_vacia)
#metodo reverse muestra la posicion y el cambio es permanente
lista_vacia.reverse()
print(lista_vacia)

lista_vacia.insert(2,"martes")
lista_vacia.insert(3,"miercoles")

lista_vacia.append("viernes")
lista_vacia.append("sabado")
lista_vacia.append("domingo")
lista_vacia.pop(0)
lista_vacia.insert(3,"jueves")

print(lista_vacia)#revisar denuevo como ordene la lista

lista_pares.sort()
print(lista_pares)
lista_pares.pop()
print(lista_pares)
lista2 =lista_pares.copy() #este si es un respaldo  de la lista original
print(lista2)
lista3=lista_pares[:]
print(lista3)
lista_pares.pop()
print(lista_pares)


#sorted(lista, reverse= True), ordena descendentemente, pero no es permanente
sorted(lista_pares, reverse= True)#ordena desc
sorted(lista_pares)#ordena asc
sorted(lista_pares, reverse= False)#ordena asc

print(sorted(lista_pares, reverse= True))#[10, 8, 6, 4, 2]
print(lista_pares)#[2, 4, 6, 8, 10]

#index(elemento)=> retorna el indice  del elemento que se busca en una lista

print("indice del elemento 8 es: ",lista_pares.index(8))
#print("indice del elemento 13 es: ",lista_pares.index(13))#ValueError: 13 is not in list

lista_final = lista_pares + lista_vacia
print("lista final",lista_final)




