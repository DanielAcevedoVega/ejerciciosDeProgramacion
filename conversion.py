#Escriba un programa que convierta de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros.
longitud_cm = int(input("Ingrese longitud en cm: "))
conversion = longitud_cm / 2.54

print(f"{longitud_cm} cm = {conversion} in")