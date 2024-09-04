# Inicializa contadores y sumadores para hombres y mujeres
contadorHombres = 0
contadorMujeres = 0
sumaEdadesHombres = 0
sumaEdadesMujeres = 0

# Solicita al usuario la cantidad total de alumnos
cantidadAlumnos = int(input("Ingrese la cantidad total de alumnos: "))

# Itera a través de cada alumno para registrar su sexo y edad
for i in range(cantidadAlumnos):
    # Solicita al usuario que ingrese el sexo del alumno (H para Hombre, M para Mujer)
    sexoAlumno = input("Ingrese el sexo del alumno (H/M): ").upper()
    
    # Solicita al usuario que ingrese la edad del alumno
    edadAlumno = int(input("Ingrese la edad del alumno: "))
    
    # Clasifica al alumno por sexo y actualiza contadores y sumadores correspondientes
    if sexoAlumno == 'H':
        # Incrementa el contador de hombres y suma la edad del hombre
        contadorHombres += 1
        sumaEdadesHombres += edadAlumno
    elif sexoAlumno == 'M':
        # Incrementa el contador de mujeres y suma la edad de la mujer
        contadorMujeres += 1
        sumaEdadesMujeres += edadAlumno

# Calcula el promedio de edad para hombres
if contadorHombres > 0:
    promedioEdadHombres = sumaEdadesHombres / contadorHombres
else:
    promedioEdadHombres = 0

# Calcula el promedio de edad para mujeres
if contadorMujeres > 0:
    promedioEdadMujeres = sumaEdadesMujeres / contadorMujeres
else:
    promedioEdadMujeres = 0

# Calcula el promedio de edad para el grupo total
if cantidadAlumnos > 0:
    promedioEdadGrupo = (sumaEdadesHombres + sumaEdadesMujeres) / cantidadAlumnos
else:
    promedioEdadGrupo = 0

# Imprime los resultados
print(f"Promedio de edad por grupo:")
print(f"Hombres: {promedioEdadHombres:.2f} años")
print(f"Mujeres: {promedioEdadMujeres:.2f} años")
print(f"Grupo total: {promedioEdadGrupo:.2f} años")
