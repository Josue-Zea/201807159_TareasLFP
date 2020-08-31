import webbrowser
file = open("Tarea4.html", "w")

class Registro:
    def __init__(self, numero, nombre, edad, activo, saldo):
        self.numero = numero
        self.nombre = nombre
        self.edad = edad
        self.activo = activo
        self.saldo = saldo

def CrearObjetos():
    r1 = Registro(1,"Mario",22,True,5000)
    ReporteF2(r1)
    r2 = Registro(2,"Pepe", 20, False, 1450)
    ReporteF2(r2)
    r3 = Registro(3,"Maria", 21, True, 6000)
    ReporteF2(r3)
    r4 = Registro(4,"Lupe", 25, True, 2500)
    ReporteF2(r4)
    r5 = Registro(5,"David", 20, False, 8000)
    ReporteF2(r5)
    r6 = Registro(6,"Jeanete", 19, True, 8500)
    ReporteF2(r6)
    r7 = Registro(7,"Marisa", 19, False, 2550)
    ReporteF2(r7)
    r8 = Registro(8,"Samuel", 27, True, 3000)
    ReporteF2(r8)
    r9 = Registro(9,"Roberto", 17, False, 4500)
    ReporteF2(r9)
    r10 = Registro(10,"Daniel", 21, True, 4750)
    ReporteF2(r10)
    ReporteF3()

def ReporteF1():
    file.write("<!DOCTYPE html>\n")
    file.write('<html lang="en">\n')
    file.write('<head>\n')
    file.write('<style type="text/css">\n')
    file.write(
        'table { border: black 5px solid; border-collapse: collapse;   table-layout: auto; width: 100%; border-collapse: collapse; }\n')
    file.write(
        'body { background-color: #ffdd90; background-image: url("https://lh3.googleusercontent.com/proxy/N8cSinoTJKagEAw7ZcXlkjitj31O0IlYCkVUg5-tLaxAkoU-7hl1dpENdRSBx2mh2dDw6Nt0IqLDaZOm8SY4lzw3FMyGZVOOgffThgKz5h2eVMjG"); }\n')
    file.write('html { font-family: "helvetica neue", helvetica, arial, sans-serif; }')
    file.write(
        'tbody tr:nth-child(odd) { background-color: #42DCF8; } tbody tr:nth-child(even) { background-color: #659BFA; } table { background-color: #05FD5B; }')
    file.write('</style>\n')
    file.write('<meta charset="UTF-8">\n')
    file.write('<title>Registros</title>\n')
    file.write('</head>\n')
    file.write('<body>\n')
    file.write('<font face="Brush Script MT"><marquee behavior=alternate><h1>Simpleql</h1></marquee></font>\n')
    file.write('<p>Estos son los primeros 10 registros</p>\n')
    file.write('<div style="text-align:center;">\n')
    file.write('<table class="table table-dark" border="">\n')
    file.write('<thead>\n')
    file.write('<tr>\n')
    file.write('<th scope="col"><h2>#</h2></th>\n')
    file.write('<th scope="col"><h2>Nombre</h2></th>\n')
    file.write('<th scope="col"><h2>Edad</h2></th>\n')
    file.write('<th scope="col"><h2>Activo</h2></th>\n')
    file.write('<th scope="col"><h2>Saldo</h2></th>\n')
    file.write('</tr>\n')
    file.write('</thead>\n')
    file.write('<tbody>\n')
    CrearObjetos()

def ReporteF2(registro):
    file.write('<tr>\n')
    file.write('<th scope="row">' + str(registro.numero) + '</th>\n')
    file.write('<td>' + str(registro.nombre) + '</td>\n')
    file.write('<td>' + str(registro.edad) + '</td>\n')
    file.write('<td>' + str(registro.activo) + '</td>\n')
    file.write('<td>' + str(registro.saldo) + '</td>\n')
    file.write('</tr>\n')

def ReporteF3():
    file.write('</tbody>\n')
    file.write('</table>\n')
    file.write('</div>')
    file.write('</body>\n')
    file.write('</html>\n')
    file.close()
    print("REPORTE GENERADO CON ÉXITO")
    webbrowser.open("Tarea4.html")

ReporteF1()