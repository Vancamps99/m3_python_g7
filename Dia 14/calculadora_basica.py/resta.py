def resta(x, y):

    
    """Esta función resta y de x y luego imprime el resultado."""
    print(f"El resultado de la resta es {x - y}")
if __name__ == "__main__":
    print("Probando el método resta:")
    x = float(input("Ingrese el primer número: "))
    y = float(input("Ingrese el segundo número: "))
    resta(x, y)
