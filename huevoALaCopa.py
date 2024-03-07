#Escriba un programa que reciba como entrada la temperatura original del huevo y muestre como salida el tiempo 
#en segundos que le toma alcanzar la temperatura máxima para prepararlo a la copa.
import math

m_pequeño = 47
m_grande = 67
p = 1.038
c = 3.7
k = 5.4e-3

T_o = float(input("Ingrese la temperatura original del huevo (°C): "))
T_y = 70

To = T_o + 273.15
Ty = T_y + 273.15

M = m_pequeño if m_pequeño <= 50 else m_grande
Tw = 100 + 273.15

t = (M ** (2/3)) * (c * p ** (1/3)) / (k * math.pi ** 2 * (4 * math.pi / 3) ** (2/3)) * math.log(0.76 * (To - Tw) / (Ty - Tw))

# Salida del resultado
print("El tiempo en segundos que le toma al centro de la yema alcanzar la temperatura máxima es:", t)

    