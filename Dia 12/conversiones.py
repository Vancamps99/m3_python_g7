import sys 
#quizas poner un validador pero no lo dice 
 #considerar  tasas de conversión sp :0,0046 parg:0093 dlrs:0.0013
tasa_sol_peruano=float(sys.argv[1])
tasa_peso_argentino=float(sys.argv[2])
tasa_dolar_americano=float(sys.argv[3])
#ingresar el cuarto valor 
valor_peso_chileno = float(sys.argv[4])

# Mostrar las tasas de conversión
print(f"Tasa de conversión de Sol Peruano a Peso Argentino: {tasa_sol_peruano}")
print(f"Tasa de conversión de Sol Peruano a Dólar Americano: {tasa_peso_argentino}")
print(f"Tasa de conversión de Peso Argentino a Dólar Americano: {tasa_dolar_americano}")
print(f"El monto ingresado en peso chilenos es :\n {valor_peso_chileno}")

# Calcular el valor convertido en las tres divisas
valor_en_sol = valor_peso_chileno * tasa_sol_peruano
valor_en_peso_argentino = valor_peso_chileno * tasa_peso_argentino
valor_en_dolar_americano = valor_peso_chileno * tasa_dolar_americano

# Imprimir los resultados
print(f"Valor en Sol Peruano: {valor_en_sol}")
print(f"Valor en Peso Argentino: {valor_en_peso_argentino}")
print(f"Valor en Dólar Americano: {valor_en_dolar_americano}")

