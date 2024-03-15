# Solicitar al usuario el precio de suscripción, número de usuarios y gastos totales
P = float(input("Ingrese el precio de suscripción: "))
U = int(input("Ingrese el número de usuarios: "))
GT = float(input("Ingrese los gastos totales: "))

# Calcular las utilidades
utilidades = P * U - GT

# Mostrar el resultado
print(f"Las utilidades del proyecto son: {utilidades}")