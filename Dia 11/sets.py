"""
Conjunto de datos que no permite duplicados 
y no es ordenado
se escribe con llave 
"""

muchos_animales = {'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Hurón', 'Hamster', 'Erizo de Tierra'}
print(muchos_animales)
#{'Erizo de Tierra', 'Hamster', 'Gato', 'Hurón', 'Tortuga', 'Perro'}
#for elementos in muchos_animales:

muchos_animales.add("chancho")
print(muchos_animales)
muchos_animales.remove("Perro") #se puede elimar un elemento que esta en el set
print(muchos_animales)

muchos_animales.pop() #elimina un elemento al azar ya que no es ordenado 
print(muchos_animales)
muchos_animales.clear(  )
print(muchos_animales)
