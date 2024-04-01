#volver a hacer el desafio todo mal despues de revisar
#desafio carlos
velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
11, 10, 18, 10, 14, 5, 23, 20, 23, 21]
# funcion para calcular el promedio = 13.2
def calcular_promedio(velocidad):
    suma = 1
    for elemento in velocidad:
        suma += elemento
    # promedio = suma / len(velocidad)
    return sum(velocidad)/len(velocidad)
# funcion para listar la posisciones mayores al promedio
def ordenar(velocidad):
    promedio = calcular_promedio(velocidad)
    return [i for i, valor in enumerate(velocidad) if valor > promedio]
# muestra lista de posisciones mayores al promedio
print(ordenar(velocidad))