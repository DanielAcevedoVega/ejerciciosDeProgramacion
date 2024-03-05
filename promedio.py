#Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:
primera_nota = int(input("Introduzca la primera nota: "))
segunda_nota = int(input("Introduzca la segunda nota: "))
tercera_nota = int(input("Introduzca la tercera nota: "))
cuarta_nota = int(input("Introduzca la cuarta nota: "))

promedio = (primera_nota + segunda_nota + tercera_nota + cuarta_nota) / 4

print(f"El promedio es: {promedio}")