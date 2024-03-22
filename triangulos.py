# Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:
#     si acaso el triángulo es inválido; y
#     si no lo es, qué tipo de triángulo es.

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

if(a+b > c) and (b+c > a) and (c+a > b):
    if(a == b == c):
          print("El triangulo es equilatero")
    elif(a == b != c) or (b==c != a) or (a == c != b):
         print("El triangulo es isoceles")
    elif(a != b != c):
         print("El triangulo es escaleno")
else:
    print("No es un triangulo valido.")
   







    