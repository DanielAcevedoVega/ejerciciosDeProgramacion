#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

numero = float(input("Ingrese un numero: "))

numero_decimal = abs(numero) - abs(int(numero))

print(f"{numero_decimal:.2f}")