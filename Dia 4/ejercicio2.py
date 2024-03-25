"""
diagrama de flujo 
y pseudocodigo

solicitar al usuario en ingreso de 3 numeros 
y determinar cuales de ellos es mayor que 33
solo numeros enteros 1 al 100 y determinar cual es mayor y cual es menor

"""


"""
Solicitar al usuario el ingreso de 3 números enteros entre 1 y 100.
Determinar cuáles de ellos son mayores que 33.
Además, determinar cuál es el número mayor y cuál es el número menor.
"""

# Solicitar al usuario que ingrese los 3 números enteros
numero1 = int(input("Ingrese el primer número (entre 1 y 100): "))
numero2 = int(input("Ingrese el segundo número (entre 1 y 100): "))
numero3 = int(input("Ingrese el tercer número (entre 1 y 100): "))

# Verificar si cada número es mayor que 33 e imprimir los resultados
if numero1 > 33:
    print(f"{numero1} es mayor que 33.")
if numero2 > 33:
    print(f"{numero2} es mayor que 33.")
if numero3 > 33:
    print(f"{numero3} es mayor que 33.")

# Determinar el número mayor usando la función max()
numero_mayor = max(numero1, numero2, numero3)

# Determinar el número menor usando la función min()
numero_menor = min(numero1, numero2, numero3)

# Imprimir el número mayor y el número menor
print(f"El número mayor es: {numero_mayor}")
print(f"El número menor es: {numero_menor}")