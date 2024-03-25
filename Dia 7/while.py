""" 
while condicion:
    #codigo a ejercutar

"""
# Solicitar al usuario que ingrese una contraseña
password = input("Ingrese su contraseña:\n")

# Validar que la longitud de la contraseña sea al menos 6 caracteres
while len(password) < 6:
    password = input("Ingrese su contraseña con largo superior o igual a 6 caracteres:\n")

# Verificar si la contraseña ingresada es "Hola Mundo"
while password != "Hola Mundo":
    password = input("No adivinaste la contraseña, ingrese su contraseña nuevamente:\n")

# Mensaje de contraseña correcta
print("\n¡Contraseña correcta!")
# Resto del programa
print("Fin del programa")

# Iterar 10 veces e imprimir el valor de i en cada iteración
i = 0
while i < 10:
    print(f"El valor de i es: {i}")
    i += 1  # Incrementar i en 1 en cada iteración

# Imprimir el valor de i fuera del bucle while
print(f"Fuera del bucle, valor de i= {i}")

# Bucle while infinito con break
while True:
    print("Acciones infinitas")
    if condicion:
        # Código a ejecutar si se cumple la condición
    else:
        break  # Salir del bucle si no se cumple la condición

# Concatenación de cadenas
saludo = "Hola"
saludo = saludo + " Mundo"  # Concatenar " Mundo" a la cadena "Hola"
print(saludo)

saludo += "chao"  # Agregar "chao" a la cadena resultante
print(saludo)