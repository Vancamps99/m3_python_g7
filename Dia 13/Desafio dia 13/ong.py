def factorial(numero):
    valor = 1
    for n in range(1, numero + 1):
        valor *= n
    return valor

def productoria(lista):
    valor = 1
    for elemento in lista:
        valor *= elemento
    return valor

def calcular(**parametros):
    for clave, valor in parametros.items():
        if "fact" in clave:
            print(f"El resultado del factorial de {valor} es: {factorial(valor)}")
        else:
            print(f"La productoria de los elementos {valor} es: {productoria(valor)}")

calcular(fact_1=5, prod_1=[4, 6, 7, 4, 3], fact_2=6)

#perdon profe, no entendi el ejercicio. 😞