for i in range(10): #imprime {0,1,2,3,4,5,6,7,8,9}
    print(i)

for i in range(4,10): #4,5,6,7,8,9
    print(i)

for i in range(10):
    print(i) 



#for en js 
print("")
"""
for (let index = 4; index < 10; index++) {
    console.log(index);
}
"""  
#lista
numeros=[2,"4",True,3,"gato"]
for numero in numeros:
  print(numero)
print("")
texto="hola mundo"
for caracter in texto:
    print(caracter)

datos_personales={
    "Nombre": "Alberto",
    "Apellido": "Neculhueque",
    "edad": 24,
}
for clave in datos_personales:
  print(clave)
print("")

print("")
#claves osea valor diccionario
for clave in datos_personales:
    print(datos_personales[clave])#

#imprime ambas opciones 
for clave,valor in datos_personales.items():
   print(f"clave:{clave}-valor:{valor}")#
print("")
for par in datos_personales.items():
   print(par)
print("")

for clave in datos_personales.keys():
   print(clave)

for     





prefijo = ['La','El','La','El']
frutas = ['manzana', 'platano','frutilla','tomate']
colores = ['verde','amarillo','roja','rojo']
for p, fruta, color in zip(prefijo, frutas, colores):
print(f'{p} {fruta} es de color {color}')

numeros=[2,"4",True,3,"5",[2,5,8],{"clave":"valor"}]
for numero in numeros:
    print(numero)