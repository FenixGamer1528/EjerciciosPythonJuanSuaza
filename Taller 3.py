#Ejercicio 3

# Elabore un algoritmo que calcule el promedio de tres números, los cuales deben ser almacenados
# previamente en tres variables. El algoritmo debe imprimir el siguiente mensaje: El promedio de los
# números ingresado es: xxxx

Nota1=int(input("Ingrese su primera nota: "))
Nota2=int(input("Ingrese su segunda nota: "))
Nota3=int(input("Ingrese su tercera nota: "))

Promedio= (Nota1 + Nota2 + Nota3) / 3

print (f"El promedio de sus tres notas es: ", Promedio)