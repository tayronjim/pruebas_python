frace = "Hola Mundo"

cadenas = frace.split()
mayusculas = frace.upper()
minusculas = frace.lower()
letraCapital = frace.capitalize()
reemplazo = frace.replace("Mundo", "Tayron")

print(cadenas)
print(mayusculas)
print(minusculas)
print(letraCapital)
print(reemplazo)

## Las tuplas no puedes modificar sus valores, son inmutables, pero se le pueden asignar valores mutables
## tupla = (1,2)
## tupla[0] = 5  // Esto da error
## tupla = (1,[4,6],2)
## tupla[1][0] = 3   //  si lo cambia y queda (1,[3,6],2)


tupla1 = (1,2)
print(tupla1)

tupla2 = (("persona1",24),("persona2",14),("persona3",28),("persona4",5))

for nombre, edad in tupla2:
    if edad >= 18:
        print(f"{nombre} es mayor de edad con {edad} años")

tupla3 = (10,20,30,40,50)

sumatorio = sum(tupla3)

print("La sumatoria de tupla3 es: ", sumatorio)



frutas = ("manzana", "banana" , "cereza")

palabra_buscar = input("Introduce el nombre de una fruta a buscar: ")

############ Buscar con un for ############

encontrada = False
for fruta in frutas:
    if fruta == palabra_buscar:
        encontrada = True

if encontrada:
     print("La palabra está en la tupla.")
else: print("La palabra no está en la tupla.")

########## Buscar directamente con un if ##############

if palabra_buscar in frutas:
    print("La palabra está en la tupla.")
else:
    print("La palabra no está en la tupla.")
    
