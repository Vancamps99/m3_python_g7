
# input.py
def captura_datos():
    x = float(input("Ingrese el primer número: "))  # Cerrando correctamente la llamada a la función
    y = float(input("Ingrese el segundo número: "))  # Cerrando correctamente la llamada a la función
    return x, y

if __name__ == "__main__":

 print ( "captura de datos")

x, y = captura_datos()
print("Los números capturados son:", x, "y", y)
