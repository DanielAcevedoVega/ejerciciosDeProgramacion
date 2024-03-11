#Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a mayor:
lista = list()
n1 = int(input("Ingrese numero: "))
n2 = int(input("Ingrese numero: "))
lista.extend([n1, n2])
lista.sort()
print(f"{lista[0]} {lista[1]}")

#A continuación, escriba otro programa que haga lo mismo con tres números:

lista = list()
n1 = int(input("Ingrese numero: "))
n2 = int(input("Ingrese numero: "))
n3 = int(input("Ingrese numero: "))
lista.extend([n1, n2, n3])
lista.sort()
print(f"{lista[0]} {lista[1]} {lista[2]}")

#Finalmente, escriba un tercer programa que ordene cuatro números:

lista = list()
n1 = int(input("Ingrese numero: "))
n2 = int(input("Ingrese numero: "))
n3 = int(input("Ingrese numero: "))
n4 = int(input("Ingrese numero: "))
lista.extend([n1, n2, n3, n4])
lista.sort()
print(f"{lista[0]} {lista[1]} {lista[2]} {lista[3]}")
