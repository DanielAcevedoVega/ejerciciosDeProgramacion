#Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. En caso que sea letra, determine si es mayúscula o minúscula:

while True:
    caracter = input("Ingrese caracter: ")
    if len(caracter) == 1:
        if caracter.isdigit():
            print("Es número.")
        elif caracter.isalpha():
            if caracter.islower():
                print("Es letra minúscula.")
            elif caracter.isupper():
                print("Es letra mayúscula.")
        else:
            print("No es letra ni número.")
    else:
        print("Por favor, ingrese solo un caracter.")



    