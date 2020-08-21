import json
f = open("archivojson.json", "r")
content = f.read()
jsondecoded = json.loads(content)

for empleado in jsondecoded["empleados"]:
    id = empleado["id"]
    nombre = empleado["nombre"]
    apellido = empleado["apellido"]
    telefono = empleado["telefono"]
    email = empleado["email"]
    print(id)
    print(nombre)
    print(apellido)
    print(telefono)
    print(email)
    print(type(empleado))
    print()