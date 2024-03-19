"""Condicionales"""

"""   IF  
Si se cumple la condicion, entonces se ejecuta el codigo 

"""

"""
Si este  print esta afuera del bloque if solo se mostrara fin del programa si esta dentro
mostrara eres mayor de edad y fin del programa en sucesion

"""
edad=int(input("ingrese su edad "))
if edad==18:
    print("Tienes 18 años")
elif edad>18:
    print("Eres mayor de edad ")
else:    
    print("eres menor de edad") #ojo con la alinacion o espacio que se le da al if y al else espaciado de 4 recomienda
    
if edad==0:
    print("la edad es cero")
elif edad%2==0:
    print("La edad es par")
else edad%2!=0:
    print("la edad es impar")
    
