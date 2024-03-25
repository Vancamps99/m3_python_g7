# Importar el módulo getpass para solicitar contraseñas de forma segura
import getpass

# Solicitar al usuario que ingrese su contraseña de forma segura
password = getpass.getpass("Ingrese su contraseña: ")

# Verificar si la contraseña ingresada es igual a "12345"
if password == "12345":
    print("El password es incorrecto")
# Verificar si la longitud de la contraseña es menor que 6 caracteres
elif len(password) < 6:
    print("El password es demasiado corto")