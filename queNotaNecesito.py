#Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, 
#y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

certamen_1 = int(input("Ingrese nota certamen 1: "))
certamen_2 = int(input("Ingrese nota certamen 2: "))
nota_laboratorio = int(input("Ingrese nota laboratorio: "))

nota_necesita = ((3 * (60-(nota_laboratorio * 0.3))) / 0.7) - 100

print(f"Necesita nota {round(nota_necesita)} en el certamen 3")
