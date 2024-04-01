"""precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}
def filtrar_productos(precios, umbral, tipo):
    if tipo == "mayor":
        productos_filtrados = [producto for producto, precio in precios.items() if precio > umbral]
        mensaje = f"Los productos mayores al umbral son: {', '.join(productos_filtrados)}"
    elif tipo == "menor":
        productos_filtrados = [producto for producto, precio in precios.items() if precio < umbral]
        mensaje = f"Los productos menores al umbral son: {', '.join(productos_filtrados)}"
    else:
        mensaje = "Lo sentimos, no es una operación válida"
    return mensaje


umbral = int(input("Ingrese el umbral de precio: "))
tipo = input("Ingrese 'mayor' o 'menor' para filtrar productos: ").lower()

# Llamar la función
productos_filtrados = filtrar_productos(precios, umbral, tipo)
print(productos_filtrados)

#era con argumentos . 
#validador tambien falto"""

#desafio claudio, me habia equivocado en leer el desafio 

# Importamos solo argv del módulo sys
from sys import argv

#diccionario
precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

# Definimos la función de filtrado
def filtrar(precios, umbral, opcion=False): # Se cambia '==' por '='
    filtro = []
    if opcion == 'menor':
        # List Comprehension para obtener los productos menores al umbral
        filtro = [producto for producto in precios if precios[producto] < umbral]
        print(f'Los productos menores al umbral son: {", ".join(filtro)}')  # Se cambia '{' por '('
    elif opcion == False:  # Cambiamos el valor por defecto de 'None' a 'False'
        # List Comprehension para obtener los productos mayores al umbral
        filtro = [producto for producto in precios if precios[producto] > umbral]
        print(f'Los productos mayores al umbral son: {", ".join(filtro)}')  # Se cambia '{' por '('
    else:
        print('Lo sentimos, no es una operación válida')

# Capturamos el umbral desde los argumentos de la línea de comandos
umbral = int(argv[1])

# Capturamos la opción (mayor/menor) desde los argumentos de la línea de comandos, si se proporciona
if len(argv) == 3:
    opcion = argv[2]
else:
    opcion = False  # Cambiamos el valor por defecto de 'None' a 'False'

# Llamamos a la función de filtrado con los argumentos proporcionados
filtrar(precios, umbral, opcion)
