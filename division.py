#Escriba un programa que pida dos números enteros y que calcule la división, indicando si la división es exacta o no:

dividiendo = int(input("Dividiendo: "))
divisor = int(input("Divisor: "))
conciente = dividiendo // divisor
resto = dividiendo % divisor 
if resto != 0:
    print("La division no es exacta")
    print(f"Conciente: {conciente}")
    print(f"Resto: {resto}")
else:
    print("La division es exacta")
    print(f"Conciente: {conciente}")
    print(f"Resto: {resto}")
