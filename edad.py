# Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:
from time import localtime
time = localtime()
 


print("Ingrese su fecha de nacimiento. ")
dia = int(input("Dia: "))
mes = int(input("Mes: "))
año = int(input("Año: "))

if (time.tm_mday <= dia) and (time.tm_mon <= mes):
    edadActual = time.tm_year - año
    print(f"Usted tiene {edadActual} años")
else:
    edadActual = (time.tm_year - año) + 1
    print(f"Usted tiene {edadActual} años")
    






    