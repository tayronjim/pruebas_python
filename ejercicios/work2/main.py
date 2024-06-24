numero = int(input("Untroduce numero entero: "))

match numero:
    case numero if numero < 0:
        print("Números negativos (menores que 0)")
    case numero if numero >=0 and numero < 10:
        print("Números entre 0 (incluido) y 10 (excluido)")
    case numero if numero >= 10:
        print("Números mayores o iguales a 10")
    case _:
        print("Numero no reconocido")