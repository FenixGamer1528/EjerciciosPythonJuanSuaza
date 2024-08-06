#Ejercicio4

# Construya un algoritmo que calcule el sueldo total de un vendedor, dado su sueldo base y las 
# comisiones de sus ventas. Para esto es necesario definir una variable que almacene el nombre del 
# vendedor, una variable que almacene el sueldo y otra variable que almacene el valor de la comisión 
# de las ventas realizadas. Se debe calcular el valor final de sueldo. El algoritmo debe imprimir el 
# nombre del vendedor, el valor del sueldo, el valor de su comisión y el sueldo total del vendedor.

Nombre=(input("Ingrese su nombre "))
Sueldo=int(input("Ingrese su sueldo "))
Comision=int(input("Ingrese sus comisiones "))

Sueldo_total= (Sueldo + Comision)
print (f"El vendedor " ,Nombre, ",tiene un sueldo de " ,Sueldo, ",durante el mes obtuvo una comision de " ,Comision, "su sueldo total es " ,Sueldo_total)