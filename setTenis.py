# # Escriba ub prograaa set tebis:

a = int(input("Juegos gabados por A: "))
b = int(input("Juegos gabados por B: "))


if (a == 6 and b < 5) or (a == 7 and b >= 5 and b < 7): 
    print("Gano A")
elif (b == 6 and a < 5) or (b == 7 and a >= 5 and a < 7):
    print("Gano B")
elif (a < 7 and b < 7): 
    print("Aun no termina") 
else: 
    print("Invalido")






    