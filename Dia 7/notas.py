# Solicitar al usuario la cantidad de notas que va a ingresar
cant_notas = int(input("Ingrese cantidad de notas\n"))

# Inicializar el contador de notas y la suma de notas
i = 0
suma_notas = 0

# Iterar mientras aún haya notas por ingresar
while i < cant_notas:
    # Solicitar al usuario que ingrese la nota
    nota = float(input(f"Ingresa tu {i+1} nota\n"))
    # Sumar la nota a la suma total de notas
    suma_notas = suma_notas + nota
    # Incrementar el contador de notas
    i += 1

# Calcular y mostrar el promedio de las notas
print(f"El promedio de notas es: {round(suma_notas/cant_notas, 2)}")