#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

hora_actual = int(input("Hora acutal: "))
cantidad_horas = int(input("Cantidad de horas: "))

hora_marcara = hora_actual + cantidad_horas

hora_marcara %= 24

print(f"En {cantidad_horas} horas, el reloj marcara las {hora_marcara}")
    