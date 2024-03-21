# Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y división.
def numeroFloatoInt(nu):
    nu = int(nu) if a.is_integer() else nu
    return nu

while True:
    a = float(input("Operando: "))
    operador = input("Operador: ")
    b = float(input("Operando: "))

    if operador == "+":
        c = a + b
        print(f"{numeroFloatoInt(a)} + {numeroFloatoInt(b)} = {numeroFloatoInt(c)}")
    elif operador == "-":
        c = a - b
        print(f"{numeroFloatoInt(a)} - {numeroFloatoInt(b)} = {numeroFloatoInt(c)}")
    elif operador == "*":
        c = a * b
        print(f"{numeroFloatoInt(a)} * {numeroFloatoInt(b)} = {numeroFloatoInt(c)}")
    elif operador == "/":
        if b !=0:
            c = a / b
            print(f"{numeroFloatoInt(a)} / {numeroFloatoInt(b)} = {numeroFloatoInt(c)}")
        else:
            print("Error dividir en 0")
    elif operador == "**":
        c = a**b
        print(f"{numeroFloatoInt(a)} ** {numeroFloatoInt(b)} = {numeroFloatoInt(c)}")

    continuar = input("Deseas realizar otra operacion?(s/n): ")
    if continuar.lower() != "s":
        break





    