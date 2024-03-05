#Escriba un programa que reciba como entrada las longitudes de los dos catetos y que entregue como salida el largo de la hipotenusa
from math import sqrt

cateto_a = int(input("Ingrese cateto a: "))
cateto_b = int(input("Ingrese cateto b: "))

hipotenusa = sqrt((cateto_a)**2 + (cateto_b)**2)

print(f"La hipotenusa es: {hipotenusa}")
    