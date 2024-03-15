# Solicitar al usuario el precio de suscripción, número de usuarios, gastos totales y utilidades del año anterior
P = float(input("Ingrese el precio de suscripción: "))
U = int(input("Ingrese el número de usuarios: "))
GT = float(input("Ingrese los gastos totales: "))
Uanterior = float(input("Ingrese las utilidades del año anterior: "))

# Calcular las utilidades actuales
utilidades_actuales = P * U - GT

# Calcular la razón entre las utilidades actuales y las del año anterior
razon_utilidades = utilidades_actuales / Uanterior

# Mostrar el resultado
print(f"La razón entre las utilidades actuales y las del año anterior es: {razon_utilidades:.2f}")