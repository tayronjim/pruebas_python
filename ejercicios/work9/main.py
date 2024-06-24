import modulo_personalizado

numero = int(input("Ingresa un numero para saber si es par: "))

res = modulo_personalizado.es_par(numero)

if res: print("Es Par")
else: print("Es impar")