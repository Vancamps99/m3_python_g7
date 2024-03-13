
#Dia 2 causa
edad="24" #str
numero=100 #num 242424
#duplacacion
print(3*edad) #se repite 3 veces edad (no opera por que es un caracter)
print (3*numero) #opera por que es numero
print(type(edad) )  #<class 'str'>
print(type(numero) ) # <class 'int'>

#metodo count()
print("Mapache, dime donde estas Mapache che".count("Mapache")) #esta contenido dos veces dentro de la oracion
print("Mapache, dime donde estas Mapache che".count("che")) #che esta dentro de mapa(che)x2 y el che serian 3

#metodo upper ()mayuscula  y lower()minuscula 
print("Soy malisIMo".upper()) #imprime la palabra en mayuscula "SOY MALISIMO"
print("BuEnOs DiAs" .lower()) #imprime la palabra en minuscula "buenos dias"
print("buenos dias gente ".title()) #Imprime como si se tratara de un nombre (iniciales con mayus)

#Este no es un "metodo" se debe pasar a str para que funcione  
#cuenta los caracteres incluyendo el espacio
print(len("Soy,¿puedo ser? ,ser asi .sera asi como acabe mi yo")) 

print("2".join(["a","b","c"])) #al inicio de la primera comilla va lo que se ve interpuesto entre la lista

#tipo de datos 
entero=7
decimal=9.5
cadena= "esto es una cadena"
boleano=False #t or f

print(type(entero))#<class 'int'> "entero"
print(type(decimal))#<class 'float'> "flotante"
print(type(cadena)) #<class 'str'>"caracter"
print(type(boleano)) #<class 'bool'>

numero2=200
numero2=numero2+100 #numero2= 100+100

texto1= "asd"
texto1=texto1+"" #imprime solo asd ya que " " estara vacio
print(texto1)
# no pasa lo mismo si
texto2="alfa"
texto2=texto2+" numerico"
print(texto2)

#precision de datos
promedio = (4+6+7)/3
print(f"el promedio es {promedio}")
print(f"resulta de la division {promedio:.4f}")
print(f"resulta de la division {round(promedio,3)}")

#ingreso de datos (input)
nombre=input("ingrese su nombre: ")
print(nombre)

#edad
edad=input("ingrese su edad ")
print(f"tu edad es {edad} ")
print(type(edad)) #<class 'str'>
