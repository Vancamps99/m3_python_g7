""""
PRIMER REQUERIMIENTO
precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}
#Funcion de filtro
def filtrar_productos(precios, umbral):
    productos_filtrados = [producto for producto, precio in precios.items() if precio > umbral]
    mensaje = "Los productos mayores al umbral son: " + ", ".join(productos_filtrados)
    return mensaje

umbral = int(input("Ingrese el umbral de precio: "))

productos_mayores = filtrar_productos(precios, umbral)
print(productos_mayores) """
#Modificando para cumpliar ambos requisitos
precios = {
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

productos_filtrados = filtrar_productos(precios, umbral, tipo)
print(productos_filtrados)

