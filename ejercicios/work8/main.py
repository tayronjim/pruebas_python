def calculadora(num1, num2, op):
    match op:
        case "+": return num1 + num2
        case "-": return num1 - num2
        case "*": return num1 * num2
        case "/": return num1 / num2
        case _: return "operacion invalida"

## introduciendo toda la operacion separa por espacios
operacion = input("Introduce operacion de 2 numeros")
num1, op, num2 = operacion.split()
num1 = int(num1)
num2 = int(num2)

print(calculadora(num1, num2, op))

## introduciendo cada elemento por separado
num1 = int(input("Introduce primer numero: "))
num2 = int(input("Introduce segundo numero: "))
op = input("Introduce operacion: ")

print(calculadora(num1, num2, op))