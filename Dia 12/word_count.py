with open("lorem_ipsum.txt","r") as file:
    lorem_ipsum=file.read()

print(lorem_ipsum)    
# Contar caracteres y palabras distintas 
#¿que hace set? set() se utiliza para crear un conjunto de caracteres o palabras únicos a partir de una secuencia
#Cuando se aplica set() a una cadena de texto, se obtiene un conjunto que contiene todos los caracteres únicos en esa cadena.
caracteres_distintos = len(set(lorem_ipsum))
palabras_distintas = len(set(lorem_ipsum.split()))
#split() divide la cadena en palabras basadas en espacios en blanco.
#En el contexto de este código, texto.split() divide el contenido del archivo de texto en palabras individuales.

# Mostrar los resultados
print(f"El número de caracteres distintos es: {caracteres_distintos}")
print(f"El número de palabras distintas es: {palabras_distintas}")