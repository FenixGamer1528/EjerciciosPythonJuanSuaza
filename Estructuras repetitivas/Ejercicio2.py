# Definir las variables para almacenar la suma de números positivos
sumaPositivos = 0

# Bucle que se repite 10 veces para ingresar números negativos
for i in range(10):
    # Solicita al usuario que ingrese un número negativo
    numeroIngresado = int(input("Ingrese un número negativo: "))
    
    # Verifica si el número ingresado es negativo
    if numeroIngresado < 0:
        # Convierte el número negativo a positivo utilizando la función abs()
        numeroPositivo = abs(numeroIngresado)
        # Suma el número positivo a la suma acumulada
        sumaPositivos += numeroPositivo
    else:
        # Informa al usuario si el número ingresado no es negativo
        print("El número ingresado no es negativo.")

# Imprime el resultado de la suma de los números convertidos a positivos
print(f"La suma de los números convertidos a positivos es: {sumaPositivos}")
