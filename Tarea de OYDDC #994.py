def decimal_a_binario(numero_decimal):
    return bin(numero_decimal)[2:]

def binario_a_decimal(numero_binario):
    return int(numero_binario, 2)

def es_binario(numero_binario):
    return all(bit == '0' or bit == '1' for bit in numero_binario)

opcion = input("Elige una opción:\n1. Decimal a binario\n2. Binario a decimal\n")

if opcion == '1':
    try:
        numero_decimal = int(input("Ingresa el número decimal: "))
        numero_binario = decimal_a_binario(numero_decimal)
        print(f"El número binario es: {numero_binario}")
    except ValueError:
        print("Valor inválido: Ingresa solo números")
elif opcion == '2':
    numero_binario = input("Ingresa el número binario: ")
    if es_binario(numero_binario):
        numero_decimal = binario_a_decimal(numero_binario)
        print(f"El número decimal es: {numero_decimal}")
    else:
        print("Valor inválido: Ingresa solo números binarios (0 y 1)")
else:
    print("Opción no válida")
