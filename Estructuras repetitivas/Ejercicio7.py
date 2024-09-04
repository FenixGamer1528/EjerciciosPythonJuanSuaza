# Solicita al usuario que ingrese la cantidad total de autos
cantidadAutos = int(input("Ingrese la cantidad total de autos: "))

# Inicializa los contadores para cada color de auto
contadorRojo = 0
contadorVerde = 0
contadorAmarillo = 0
contadorAzul = 0
contadorBlanco = 0

# Itera a través de cada auto para clasificarlo según el último dígito de la placa
for i in range(cantidadAutos):
    # Solicita al usuario que ingrese el último dígito de la placa del auto
    placaAuto = input("Ingrese el último dígito de la placa del auto: ")
    
    # Convierte el último dígito de la placa a un entero
    ultimoDigitoPlaca = int(placaAuto[-1])
    
    # Clasifica el auto según el último dígito de la placa y actualiza el contador correspondiente
    if ultimoDigitoPlaca == 1 or ultimoDigitoPlaca == 2:
        # Incrementa el contador de autos rojos
        contadorRojo += 1
    elif ultimoDigitoPlaca == 3 or ultimoDigitoPlaca == 4:
        # Incrementa el contador de autos verdes
        contadorVerde += 1
    elif ultimoDigitoPlaca == 5 or ultimoDigitoPlaca == 6:
        # Incrementa el contador de autos amarillos
        contadorAmarillo += 1
    elif ultimoDigitoPlaca == 7 or ultimoDigitoPlaca == 8:
        # Incrementa el contador de autos azules
        contadorAzul += 1
    elif ultimoDigitoPlaca == 9 or ultimoDigitoPlaca == 0:
        # Incrementa el contador de autos blancos
        contadorBlanco += 1

# Imprime la cantidad total de autos de cada color
print(f"Rojo: {contadorRojo}, Verde: {contadorVerde}, Amarillo: {contadorAmarillo}, Azul: {contadorAzul}, Blanco: {contadorBlanco}")
