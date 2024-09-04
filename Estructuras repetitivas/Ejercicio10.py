# Inicializa la variable para almacenar el resultado de la multiplicación
resultadoMultiplicacion = 1

# Bucle que recorre los números del 1 al 19 (inclusive)
for i in range(1, 20):
    # Multiplica el resultado acumulado por el número actual
    resultadoMultiplicacion *= i

# Imprime el resultado final de la multiplicación de los primeros 19 números naturales
print(f"El producto de los primeros 20 números naturales es: {resultadoMultiplicacion}")
