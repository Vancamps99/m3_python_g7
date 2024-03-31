def imprimir_menu():
    print('Opciones: ')
    print('1) De acuerdo')
    print('2) En desacuerdo')
    print('3) No me interesa')#si una funcion no es llamada mejor dicho invocar
    
    #no hace nada
print(imprimir_menu)

#QUE ES EL PRINCIPIO DE DRY  -----------> Redundancia de codigo.

# se habia puesto 
#con esta def se optimizo el codigo
"""
print(f'La respuesta a la pregunta 1 fue {respuestas[0]}')
print(f'La respuesta a la pregunta 2 fue {respuestas[1]}')
print(f'La respuesta a la pregunta 3 fue {respuestas[2]}')
"""
def imprimir_respuesta(respuestas):
    for i in range(len(respuestas)):
        print(f'La respuesta a la pregunta {i+1} fue {respuestas[i]}')

preguntas = ['Enunciado Pregunta 1', 'Enunciado Pregunta 2', 'Enunciado Pregunta 3']

# Hacer preguntas
respuestas = []  
for pregunta in preguntas:
    print(pregunta)
    imprimir_menu()
    respuestas.append(input('> '))
    print("")

# Mostrar respuestas
imprimir_respuesta(respuestas)



#si una funcion no es llamada mejor dicho invocar
    #no hace nada
#QUE ES EL PRINCIPIO DE DRY  -----------> Redundancia de codigo.