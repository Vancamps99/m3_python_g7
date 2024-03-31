# La lista original de velocidades
velocidad = [
25, 12, 19, 16, 11, 11, 24, 1, 14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2, 14, 23, 19, 23, 9, 18, 20, 22,
14, 1, 10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5, 11, 10, 18, 10, 14, 5,
23, 20, 23, 21]

def elementos_quitar(velocidades):
# Convertir la lista en un conjunto para eliminar los elementos repetidos
 velocidades_sin_repetir_set = set(velocidades) #set muestra los elementos sin repetirse(los deja como elementos unicos)
    
# Devolver el conjunto o la lista según sea necesario
 # Convertir el conjunto nuevamente en una lista
 velocidades_sin_repetir_lista = list(velocidades_sin_repetir_set) #ojo aca que devuelve un conjunto (para esto se modifica con  list)
 return velocidades_sin_repetir_lista  
#si ponemos return velocidades_sin_repetir_set
#arroja un conjunto {1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 16, 18, 19, 20, 21, 22, 23, 24, 25}

# Llamar a la función y guardar el resultado en una variable
resultado = elementos_quitar(velocidad)

# Imprimir el resultado
print("Datos sin repetir:", resultado)
#lista velocidades no se ha modificado  sino que en base a ella se hizo otra lista para mostrar /lista resultados
