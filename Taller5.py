#Ejercicio5

# Desarrolle un algoritmo que Programa que calcule el precio final de una compra, dado el valor de la
# compra y un descuento. Para esto es necesario declarar dos variables, una que guarde el valor de la
# compra y otra que almacene el valor del descuento. El algoritmo debe mostrar en pantalla, el valor
# de la compra el valor del descuento y el valor final a pagar. 

Compra=int(input("Ingrese el valor de la compra "))

Descuento=int(Compra * 0.15)
Valor_final= Compra - Descuento
print(f"El valor de la  compra es" ,Compra ,",el valor del descuento es" ,Descuento ,"y el valor final a pagar es" ,Valor_final)