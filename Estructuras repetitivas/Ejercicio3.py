# Definir la variable para almacenar la suma de las calificaciones
sumaCalificaciones = 0

# Inicializar las variables para las calificaciones más alta y baja
calificacionAlta = -float('inf')  # Se utiliza -infinito para asegurar que cualquier calificación ingresada sea mayor
calificacionBaja = float('inf')   # Se utiliza infinito para asegurar que cualquier calificación ingresada sea menor

# Bucle para ingresar 20 calificaciones
for i in range(20):
    # Solicita al usuario que ingrese la calificación del alumno
    calificacionIngresada = float(input("Ingrese la calificación del alumno: "))
    
    # Suma la calificación ingresada al total de calificaciones
    sumaCalificaciones += calificacionIngresada
    
    # Actualiza la calificación más alta si la calificación ingresada es mayor
    if calificacionIngresada > calificacionAlta:
        calificacionAlta = calificacionIngresada
    
    # Actualiza la calificación más baja si la calificación ingresada es menor
    if calificacionIngresada < calificacionBaja:
        calificacionBaja = calificacionIngresada

# Calcular el promedio de las calificaciones
promedioCalificaciones = sumaCalificaciones / 20

# Imprimir el promedio, la calificación más alta y la calificación más baja
print(f"Promedio: {promedioCalificaciones:.2f}, Calificación más alta: {calificacionAlta}, Calificación más baja: {calificacionBaja}")
