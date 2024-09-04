# Inicializa contadores y acumuladores para cada grupo etario
contadorNiños = contadorJovenes = contadorAdultos = contadorAncianos = 0
sumaPesoNiños = sumaPesoJovenes = sumaPesoAdultos = sumaPesoAncianos = 0

# Simulación de la entrada de datos para 50 personas
for i in range(50):
    # Solicita al usuario que ingrese la edad de la persona
    edadPersona = int(input("Ingrese la edad de la persona: "))
    
    # Solicita al usuario que ingrese el peso de la persona en kilogramos
    pesoPersona = float(input("Ingrese el peso de la persona (kg): "))
    
    # Clasifica a la persona en una categoría de edad y actualiza contadores y sumadores
    if edadPersona <= 12:
        # Persona es un niño (12 años o menos)
        contadorNiños += 1
        sumaPesoNiños += pesoPersona
    elif edadPersona <= 29:
        # Persona es un joven (entre 13 y 29 años)
        contadorJovenes += 1
        sumaPesoJovenes += pesoPersona
    elif edadPersona <= 59:
        # Persona es un adulto (entre 30 y 59 años)
        contadorAdultos += 1
        sumaPesoAdultos += pesoPersona
    else:
        # Persona es un anciano (60 años o más)
        contadorAncianos += 1
        sumaPesoAncianos += pesoPersona

# Cálculo de promedios utilizando estructuras condicionales tradicionales
if contadorNiños > 0:
    # Calcula el promedio de peso para niños si hay al menos un niño
    promedioPesoNiños = sumaPesoNiños / contadorNiños
else:
    # Si no hay niños, el promedio es 0
    promedioPesoNiños = 0

if contadorJovenes > 0:
    # Calcula el promedio de peso para jóvenes si hay al menos un joven
    promedioPesoJovenes = sumaPesoJovenes / contadorJovenes
else:
    # Si no hay jóvenes, el promedio es 0
    promedioPesoJovenes = 0

if contadorAdultos > 0:
    # Calcula el promedio de peso para adultos si hay al menos un adulto
    promedioPesoAdultos = sumaPesoAdultos / contadorAdultos
else:
    # Si no hay adultos, el promedio es 0
    promedioPesoAdultos = 0

if contadorAncianos > 0:
    # Calcula el promedio de peso para ancianos si hay al menos un anciano
    promedioPesoAncianos = sumaPesoAncianos / contadorAncianos
else:
    # Si no hay ancianos, el promedio es 0
    promedioPesoAncianos = 0

# Imprime los resultados de los promedios de peso por categorías de edad
print(f"Promedio de peso por categorías de edad:")
print(f"Niños: {promedioPesoNiños:.2f} kg")
print(f"Jóvenes: {promedioPesoJovenes:.2f} kg")
print(f"Adultos: {promedioPesoAdultos:.2f} kg")
print(f"Ancianos: {promedioPesoAncianos:.2f} kg")
