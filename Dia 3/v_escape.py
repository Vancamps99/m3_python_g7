import math

# Solicitar al usuario el radio y la constante g
r = float(input("Ingrese el radio en Kilómetros: "))
g = float(input("Ingrese la constante g: "))

# Convertir el radio de kilómetros a metros
r_metros = r * 1000

# Calcular la velocidad de escape
ve = math.sqrt(2 * g * r_metros)

# Mostrar el resultado
print(f"La velocidad de Escape es {ve} [m/s]")