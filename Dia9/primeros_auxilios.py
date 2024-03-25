import sys

# Mensaje de bienvenida
print("Preguntas básicas para realizar primeros auxilios. Por favor, responda las preguntas con 'Sí' o 'No'.")

# Pregunta sobre la respuesta a estímulos
estimulos = input("¿La persona responde a estímulos? (Sí / No): ").lower()

# Evaluación de la respuesta a estímulos
if estimulos != "si":
    print("Abra la vía aérea.")
else:
    print("Valore la necesidad de llevarlo al hospital más cercano.")
    sys.exit()

# Pregunta sobre la respiración
respira = input("¿La persona respira? (Sí / No): ").lower()

# Evaluación de la respiración
if respira != "si":
    print("Administre 5 ventilaciones y llame a la ambulancia.")
else:
    print("Permita una posición con suficiente ventilación.")
    sys.exit()

# Inicialización de la variable ambulancia
ambulancia = "no"

# Bucle de espera de ambulancia
while ambulancia != "si":
    signos_vida = input("¿Tiene signos vitales? (Sí / No): ").lower()
    
    # Verificación de los signos vitales
    if signos_vida == "si":
        print("Revalúe mientras espera la ambulancia.")
        ambulancia = input("¿Ha llegado la ambulancia? (Sí / No): ").lower()
    else:
        print("Administre compresiones torácicas hasta que llegue la ambulancia.")
        ambulancia = input("¿Ha llegado la ambulancia? (Sí / No): ").lower()

# Mensaje de finalización del programa
print("Fin del programa.")