# Definimos la lista de velocidades
velocidades = [25, 12, 19, 16, 11, 11, 24, 1, 14, 14, 16, 10, 6, 23, 13, 25, 4, 19, 14, 20,
               18, 9, 18, 4, 18, 1, 3, 4, 2, 14, 23, 19, 23, 9, 18, 20, 22, 14, 1, 10, 5,
               23, 3, 5, 9, 5, 3, 12, 20, 5, 11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

def promedio_velocidades(velocidades):
    # Calculamos el promedio de las velocidades
    promedio = sum(velocidades) / len(velocidades)
    return promedio

def correas_sobre_promedio(velocidades):
    promedio = promedio_velocidades(velocidades)
    # Obtenemos las posiciones de las correas con velocidades sobre el promedio
    posiciones = [indice for indice, velocidad in enumerate(velocidades) if velocidad > promedio]
    return posiciones

# Llamamos a la función para obtener las posiciones de las correas sobre el promedio
posiciones_sobre_promedio = correas_sobre_promedio(velocidades)
# Imprimimos el resultado
print(posiciones_sobre_promedio)
