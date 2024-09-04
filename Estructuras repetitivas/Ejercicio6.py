# Solicita al usuario que ingrese la cantidad total de personas en el salón
cantidadPersonas = int(input("Ingrese la cantidad total de personas en el salón: "))

# Inicializa los contadores para hombres y mujeres
contadorHombres = 0
contadorMujeres = 0

# Itera a través de cada persona en el salón
for i in range(cantidadPersonas):
    # Solicita al usuario que ingrese el sexo de la persona (H para Hombre, M para Mujer)
    sexoPersona = input("Ingrese el sexo de la persona (H/M): ").upper()
    
    # Verifica si la entrada es 'H' (Hombre)
    if sexoPersona == 'H':
        # Incrementa el contador de hombres
        contadorHombres += 1
    # Verifica si la entrada es 'M' (Mujer)
    elif sexoPersona == 'M':
        # Incrementa el contador de mujeres
        contadorMujeres += 1

# Imprime la cantidad total de hombres y mujeres
print(f"Hombres: {contadorHombres}, Mujeres: {contadorMujeres}")
