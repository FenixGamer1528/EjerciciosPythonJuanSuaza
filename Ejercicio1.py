mensaje="Hola, estoy aprendiendo Python."
nombre="Juan"
Formacion="ADSO"
Edad=20
Estatura=1.75
Peso=55
#Primer forma de hacer print
print(mensaje, "Mi nombre es", nombre, "soy de la formacion", Formacion, "tengo", Edad, "años", "mido", Estatura, "y peso", Peso, "kg\n" )
#Segunda forma de hacer print
print(f"{mensaje} Mi nombre es {nombre}, soy de la formacion {Formacion}, tengo {Edad} años, mido {Estatura} y peso {Peso} kg")
#Ejercicio matematico
a=15
b=30
suma=a+b
resta=a-b
multiplicacion=a*b
division=a/b
print("\n La suma es igual a:", suma, "\n La resta es igual a:", resta, "\n La multiplicacion es igual a:", multiplicacion, "\n La division es igual a:", division)
#Ejercicio pidiendo datos
dato1=int(input("\nDigite un numero "))
dato2=int(input("Digite otro numero "))
print("\nLa suma es igual a:", dato1+dato2, "\nLa resta es igual a:", dato1-dato2, "\nLa multiplicacion es igual a:", dato1*dato2, "\nLa division es igual a:", dato1/dato2)