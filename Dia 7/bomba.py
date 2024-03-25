import sys, time

# Imprime los argumentos pasados desde la línea de comandos
print(sys.argv)  # ['dia7/bomba.py', '8']
print(sys.argv[0])  # Nombre del script
print(sys.argv[1])  # Primer argumento (número de segundos)

# Convierte el argumento (número de segundos) en un entero
i = int(sys.argv[1])

# Inicia un temporizador regresivo
while i > 0:
    print(f"El valor de i {i}")  # Imprime el valor actual de i
    time.sleep(1)  # Espera 1 segundo
    i -= 1         # Decrementa i en 1 en cada iteración

# Imprime un mensaje después de que el temporizador haya terminado
print("BOOOOOOMMMM!!!")

#los comentarios muestran el resultado esperado  de cada paso !