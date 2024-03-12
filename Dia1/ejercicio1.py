#esto es un comentario
"""
Este es un comentario de mas de una linea "con triple comillas"

"""

print("hola mundo")
print(3+4)
numero=23
print(2/2) #el resultado siempre sera un float
print(2*4)
print("numero")
#print(2/0) ZeroDivisionError: division by zero

"""
Limitantes

No tiene permitido la suma de numeros y letras  arroja el siguiente //error can only concatenate str (not "int") to str//
ejemplo

"""
print("texto"+"34")

#INTERPOLACION
print(f"el numero es {numero}")
#no solo con numeros tambien con str
nombre= "Alberto"
print (f"Tu nombre es {nombre}") # !esto es interpolacion!
print("Tu nombre es "+nombre) #esto es concatenar
print(f"Tu nombre es {nombre} y tu edad es {numero}")

#string.format()
print("Tu nombre es {} y tu edad es {}".format(nombre,numero))
# formato con %: %s para string y %d para numeros
print("Tu nombre es %s y tu edas es %d" % (nombre,numero))

#metodo con cadena 
apellido="Neculhueque Guzman"
print(apellido.title)