# Solicita al usuario que ingrese un número para calcular su tabla de multiplicar
numeroMultiplicar = int(input("Ingrese un número para calcular su tabla de multiplicar: "))
# Itera a través de los números del 1 al 10 para calcular y mostrar la tabla de multiplicar
for i in range(1, 11):
    productoMultiplicacion = numeroMultiplicar * i
    # Imprime el resultado en un formato claro: "numeroMultiplicar * i = productoMultiplicacion"
    print(f"{numeroMultiplicar} * {i} = {productoMultiplicacion}")