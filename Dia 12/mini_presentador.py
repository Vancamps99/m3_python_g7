import sys

#se ejecuta desde terminal #ojo con la ubicacion de donde se lanza pq lanza error
nombre=sys.argv[1] 
apellido=sys.argv[2]
print(f"mi nombre es\n {nombre}")#poner nombre el el shell
print(f"Apellido\n{apellido}")#poner Apellido en el shell
print(f"nombre de este archivo es\n{sys.argv[0]}")#imprime el nombre del codigo "mini presentador"
print(type(sys.argv)) #muestra que es una lista

