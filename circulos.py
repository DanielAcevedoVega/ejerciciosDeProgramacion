import math 
# programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:
radio = int(input("Ingrese el radio del circulo en cm: "))

perimetro = 2 * math.pi * radio

area = math.pi * radio**2

print(f"Perimetro: {perimetro}")
print(f"Area: {area}")
