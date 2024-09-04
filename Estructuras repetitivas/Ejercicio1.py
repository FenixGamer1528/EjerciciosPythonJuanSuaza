# Definir las variables para contar diferentes tipos de números
contadorPositivos = 0    # Contador para números mayores a 0
contadorNegativos = 0    # Contador para números menores a 0
contadorNeutros = 0      # Contador para números que son igual a 0

# Bucle que se repite 20 veces para ingresar números reales
for i in range(20):
    # Solicita al usuario que ingrese un número
    numeroIngresado = int(input("Ingrese un número: "))
    
    # Clasifica el número ingresado y actualiza el contador correspondiente
    if numeroIngresado > 0:
        # Si el número es mayor a 0, incrementa el contador de positivos
        contadorPositivos += 1
    elif numeroIngresado < 0:
        # Si el número es menor a 0, incrementa el contador de negativos
        contadorNegativos += 1
    else:
        # Si el número es igual a 0, incrementa el contador de neutros
        contadorNeutros += 1

# Imprime el conteo de números positivos, negativos y neutros
print(f"Positivos: {contadorPositivos}, Negativos: {contadorNegativos}, Neutros: {contadorNeutros}")
