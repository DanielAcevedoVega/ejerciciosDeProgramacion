#Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por cuántas letras lo es.

palabra1 = input("Palabra 1: ")
palabra2 = input("Palabra 2: ")
count1 = len(palabra1)
count2 = len(palabra2)

if count1 > count2:
    diferencia = count1 - count2
    print(f"La palabra {palabra1} tiene {diferencia} letras mas que {palabra2}")
elif count2 > count1:
     diferencia = count2 - count1
     print(f"La palabra {palabra2} tiene {diferencia} letras mas que {palabra1}")
else:
     print("Las dos palabras tienen el mismo largo")