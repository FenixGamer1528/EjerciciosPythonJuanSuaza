# Inicializa los contadores y acumuladores
contadorHombres = 0
contadorMujeres = 0
sumaAltura = 0
contadorMayorA170 = 0
contadorMenorOIgualA150 = 0

# Comienza un bucle infinito que terminará cuando el usuario ingrese 0 como edad
while True:
    # Solicita al usuario que ingrese la edad del alumno (0 para finalizar)
    edadAlumno = int(input("Ingrese la edad del alumno (Ingrese 0 para finalizar): "))
    
    # Si la edad es 0, termina el bucle
    if edadAlumno == 0:
        break
    
    # Solicita al usuario que ingrese el sexo del alumno (H para Hombre, M para Mujer)
    sexoAlumno = input("Ingrese el sexo del alumno (H/M): ").upper()
    
    # Solicita al usuario que ingrese la altura del alumno en centímetros
    alturaAlumno = float(input("Ingrese la altura del alumno (en cm): "))
    
    # Acumula la altura total de los alumnos
    sumaAltura += alturaAlumno
    
    # Actualiza el contador de hombres o mujeres según el sexo ingresado
    if sexoAlumno == 'H':
        contadorHombres += 1
    elif sexoAlumno == 'M':
        contadorMujeres += 1
    
    # Actualiza los contadores para los rangos de altura especificados
    if alturaAlumno > 170:
        contadorMayorA170 += 1
    elif alturaAlumno <= 150:
        contadorMenorOIgualA150 += 1

# Calcula el total de alumnos registrados
totalAlumnos = contadorHombres + contadorMujeres

# Calcula el promedio de altura si hay al menos un alumno registrado
if totalAlumnos > 0:
    promedioAltura = sumaAltura / totalAlumnos
else:
    promedioAltura = 0

# Imprime los resultados de los análisis realizados
print(f"Cantidad de hombres: {contadorHombres}")
print(f"Cantidad de mujeres: {contadorMujeres}")
print(f"Altura promedio: {promedioAltura:.2f} cm")
print(f"Cantidad de alumnos con altura mayor a 1.70 cm: {contadorMayorA170}")
print(f"Cantidad de alumnos con altura menor o igual a 1.50 cm: {contadorMenorOIgualA150}")
