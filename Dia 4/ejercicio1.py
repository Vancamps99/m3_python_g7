""" 
Sumar dos números enteros ingresados por el usuario
mostrar el resultado de la suma
inicio
    Leer numero1          # Solicitar al usuario que ingrese el primer número entero
    Leer numero2          # Solicitar al usuario que ingrese el segundo número entero
    numero1+numero2       # Realizar la suma de los dos números (esta línea no tiene efecto ya que no está asignada a ninguna variable)
    Mostrar numero1+numero2   # Mostrar el resultado de la suma de los dos números
fin
"""

# Solicitar al usuario que ingrese el primer número entero
numero1 = int(input("Ingrese el primer número: "))

# Solicitar al usuario que ingrese el segundo número entero
numero2 = int(input("Ingrese el segundo número: "))

# Calcular la suma de los dos números y mostrar el resultado
print(f"El resultado de la suma es: {numero1 + numero2}")


# Solicitar al usuario que ingrese la base del rectángulo
base = float(input("Ingrese la base del rectángulo: "))

# Solicitar al usuario que ingrese la altura del rectángulo
altura = float(input("Ingrese la altura del rectángulo: "))

# Calcular y mostrar el área del rectángulo
print(f"El área del rectángulo es: {base * altura}")