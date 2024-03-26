# Creamos un diccionario vacío para almacenar las mascotas ingresadas por el usuario
mascotas = {}

# Solicitamos al usuario que ingrese la cantidad de mascotas que desea ingresar
cant_mascotas = int(input("Ingrese cantidad de mascotas a ingresar: "))

# Iteramos sobre el rango de la cantidad de mascotas ingresadas
for i in range(cant_mascotas):
    
    # Creamos un diccionario temporal para almacenar los detalles de cada mascota
    mascota = {
        "nombre": "",
        "raza": "",
        "peso": 0.0,
        "chip": False,
    }

    # Solicitamos al usuario que ingrese los detalles de la mascota
    for key in mascota.keys():
        mascota[key] = input(f"Ingrese la {key} de su mascota: ")

    # Imprimimos los detalles de la mascota ingresada
    print("Detalles de la mascota:")
    print(mascota)
    print("")

    # Imprimimos los valores de cada detalle de la mascota
    print("Valores de la mascota:")
    for valor in mascota.values():
        print(valor)
    print("")

    # Imprimimos las claves y valores de la mascota
    print("Claves y valores de la mascota:")
    for clave, valor in mascota.items():
        print(f"clave {clave} - valor {valor}")

    # Almacenamos la mascota en el diccionario principal utilizando su nombre como clave
    mascotas[mascota["nombre"]] = mascota

# Imprimimos el diccionario de mascotas completo
print("Diccionario completo de mascotas:")
print(mascotas)
