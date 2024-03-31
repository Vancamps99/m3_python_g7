suma=3 #variable global
def sumar(numero1,numero2):
    suma=numero1+numero2 #esta variable esta siendo limitada por la funcion #fuera de ella no se mostrara si se llama
    return suma
#llama a la funcion
suma=1 #    variable local
sumar(14,15)
#no se visualiza
#que pasa si
print(sumar(15,16))#31
print()
#entonces se tiene que capturar el valor de retorno
valor_retorno=sumar(16,17)
print(valor_retorno)