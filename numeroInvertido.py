#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:longitud_cm = int(input("Ingrese longitud en cm: "))
numero = int(input("Ingrese un numero de tres digitos: "))

if (numero > 99 and numero < 1000):
    numeroInvertido = str(numero)[::-1]
    print(numeroInvertido)
else:
    print("Error el numero tiene que ser de solo tres digitos")


    