import suma
import resta as r
from input import captura_datos

opcion = int( input("""Esto es una calculadora:
¿Qué operación le gustaría realizar?
1. Sumar
2. Restar
0. Salir
> """))

if opcion == '1':
    x, y = captura_datos # 3ra forma de importar
    suma.suma(x,y) # 1era forma de importar
elif opcion == '2':
    x, y = captura_datos # 3ra forma de importar
    r.resta(x,y) # 2da forma de importar
elif opcion == '0':
    print('Nos vemos a la próxima')
else:
    print('No existe esta Operación')