## Dicionarios

personas = {
    "persona1":{
        "nombre": "mi nombre 1",
        "edad": 10,
        "ciudad":"Gdl 1"
    },
    "persona2":{
        "nombre": "mi nombre 2",
        "edad": 20,
        "ciudad":"Gdl 2"
    },
    "persona3":{
        "nombre": "mi nombre 3",
        "edad": 30,
        "ciudad":"Gdl 3"
    }
}

perfil1 = personas["persona1"]

print(perfil1)

datos_personales = {
    "nombre":None,
    "edad": None,
    "ciudad": None,
    "telefono": None
}

datos_personales["nombre"] = input("introduce el nombre: ")
datos_personales["edad"] = input("introduce la edad: ")
datos_personales["ciudad"] = input("introduce la ciudad: ")
datos_personales["telefono"] = input("introduce el telefono: ")

print(datos_personales)
print(f"Nombre: {datos_personales['nombre']}, Edad: {datos_personales['edad']}, Ciudad: {datos_personales['ciudad']} y su Telefono: {datos_personales['telefono']}")


