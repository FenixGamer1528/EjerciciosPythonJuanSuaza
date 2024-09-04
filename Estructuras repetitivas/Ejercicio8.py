# Inicializa los contadores para cada rango de calificación
contadorMenor50 = 0
contadorEntre50y69 = 0
contadorEntre70y79 = 0
contadorMayor80 = 0

# Itera a través de 23 estudiantes para clasificar sus calificaciones
for i in range(23):
    # Solicita al usuario que ingrese la calificación del estudiante (entre 1 y 100)
    calificacionEstudiante = float(input("Ingrese la calificación del estudiante (1-100): "))
    
    # Clasifica la calificación en uno de los rangos y actualiza el contador correspondiente
    if calificacionEstudiante < 50:
        # Incrementa el contador para calificaciones menores a 50
        contadorMenor50 += 1
    elif 50 <= calificacionEstudiante < 70:
        # Incrementa el contador para calificaciones entre 50 y 69
        contadorEntre50y69 += 1
    elif 70 <= calificacionEstudiante < 80:
        # Incrementa el contador para calificaciones entre 70 y 79
        contadorEntre70y79 += 1
    else:
        # Incrementa el contador para calificaciones de 80 o más
        contadorMayor80 += 1

# Imprime la cantidad total de estudiantes en cada rango de calificación
print(f"Menor a 50: {contadorMenor50}, Entre 50 y 69: {contadorEntre50y69}, Entre 70 y 79: {contadorEntre70y79}, Mayor o igual a 80: {contadorMayor80}")
