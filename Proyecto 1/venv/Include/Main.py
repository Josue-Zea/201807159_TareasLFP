BD=[]
BaseActual = 0
class BaseDatos:
    def __init__(self,nombre,vacio,columnas):
        self.nombre=nombre
        self.vacio = vacio
        self.columnas = columnas
        self.BDEncabezados=[]
        self.BDNRegistros=[]

    def getNombre(self):
        return self.nombre

    def setColumnas(self, columnas):
        self.columnas = columnas

    def getColumnas(self):
        return self.columnas

    def setVacio(self, vacio):
        self.vacio = vacio

    def getVacio(self):
        return self.vacio

    def setBDEncabezados(self,BDEncabezados):
        self.BDEncabezados = BDEncabezados

    def getDBEncabezados(self):
        return self.BDEncabezados

    def setBDNRegistros(self, base):
        self.BDNRegistros.append(base.split(","))

    def getBDNRegistros(self):
        return self.BDNRegistros

class Automata:
    def __init__(self,cadena):
        self.cadena = cadena

    def VerificarCadena(self):
        comando = ""
        variable1 = ""
        variable2 = ""
        self.estado=0
        for i in range(0,len(self.cadena)):
            self.transicion = self.cadena[i]
            if self.estado == 0:
                if self.transicion!=" ":
                    comando+=self.transicion
                elif comando.lower() == "create":
                    self.estado = 1
                    comando=""
                elif comando.lower() == "load":
                    self.estado = 3
                    comando=""
                elif comando.lower() == "use":
                    self.estado = 7
                    comando=""
            elif self.estado == 1:
                if self.transicion!=" ":
                    comando+=self.transicion
                elif comando.lower() == "set":
                    self.estado = 2
                    comando=""
            elif self.estado == 2:
                if i == (len(self.cadena) - 1):
                    comando += self.transicion
                    self.estado = 10
                    AgregarBaseDatos(comando)
                else:
                    comando += self.transicion
            elif self.estado == 3:
                if self.transicion!=" ":
                    comando+=self.transicion
                elif comando.lower() == "into":
                    self.estado = 4
                    comando=""
            elif self.estado == 4:
                if self.transicion!=" ":
                    variable1+=self.transicion
                else:
                    self.estado = 5
            elif self.estado == 5:
                if self.transicion!=" ":
                    comando+=self.transicion
                elif comando.lower() == "files":
                    self.estado = 6
                    comando=""
            elif self.estado == 6:
                if i == (len(self.cadena) - 1):
                    Resultado = True
                    variable2 += self.transicion
                    variable2= variable2.replace(" ","")
                    var3 = ""
                    for j in range(0,len(variable2)):
                        trans = variable2[j]
                        if j == (len(variable2)-1):
                            var3+=trans
                            Resultado = CargaraBaseDatos(variable1, var3)
                        elif trans!=",":
                            var3+=trans
                        elif trans==",":
                            Resultado = CargaraBaseDatos(variable1, var3)
                            var3=""
                    if Resultado == True:
                        self.estado=10
                    else:
                        return False
                    print("Base de datos cargada con éxito")
                else:
                    variable2+=self.transicion
            elif self.estado == 7:
                if self.transicion!=" ":
                    comando+=self.transicion
                elif comando.lower() == "set":
                    self.estado = 8
                    comando=""
            elif self.estado == 8:
                Resultado = True
                if i == (len(self.cadena)-1):
                    variable1+=self.transicion
                    Resultado = BaseEnUso(variable1)
                    if Resultado == True:
                        self.estado = 10
                    else:
                        return False
                else:
                    variable1+=self.transicion
        if self.estado == 10:
            return True
        else:
            return False

##Método para buscar una base de datos y establecerla como base en uso
def BaseEnUso(NombreBase):
    global BaseActual
    ValorSumado = 0
    Encontrado = 0
    for i in range(len(BD)):
        if  NombreBase == BD[i].getNombre():
            BaseActual = BD[i]
            print("Se estableció la base de datos '" + BD[i].getNombre() + "' en uso")
            Encontrado = 1
    if Encontrado == 0:
        return False
    elif Encontrado == 1:
        return True

##Método para hacer la función de seleccionar
def ComandoSel(Atributos,Condiciones):
    Atributos = Atributos.split(",")
    NoEncabezado=""
    BaseFragmentada = []
    if BaseActual==0:
        print("Primero debe establecer una base de datos a usar")
    else:
        BaseTotalTempotal = BaseActual.getBDNRegistros()
        EncabezadosDeBase = BaseActual.getDBEncabezados()
        for i in range(len(Atributos)):
            for j in range(len(EncabezadosDeBase)):
                if Atributos[i].lower() == EncabezadosDeBase[j].lower():
                    NoEncabezado += str(j) + ","
                    continue
        NoEncabezado = NoEncabezado.split(",")
        NoEncabezado.pop(len(NoEncabezado) - 1)
        BaseTotalTempotal = BuscarCondiciones(BaseTotalTempotal, Condiciones, EncabezadosDeBase)
        print("Base total temporal")
        print(BaseTotalTempotal)
        if Atributos[0] == "*":
            print("Continuamos")
        elif len(NoEncabezado) != len(Atributos):
            print("Uno o más atributos no existen")
        else:
            valor = ""
            for i in range(len(BaseTotalTempotal)):
                for j in range(len(BaseTotalTempotal)):
                    for k in range(len(NoEncabezado)):
                        if int(NoEncabezado[k]) == j:
                            valor += str(BaseTotalTempotal[i][j]) + ","
                            if k == len(NoEncabezado) - 1:
                                valor = valor.split(",")
                                valor.pop(len(valor) - 1)
                                BaseFragmentada.append(valor)
                                valor = ""
        print("Base fragmentada")
        print(BaseFragmentada)
        ImprimirBase(BaseFragmentada, len(NoEncabezado))
        try:
            print("Pruebas")
        except:
            print("Los atributos solo pueden listarse siguiendo el orden en el que fueron ingresados")

def BuscarCondiciones(Base,Condiciones,Encabezados):
    estado = 0
    condicionAUsar=0
    atributo1=""
    comparacion1=""
    valor1=""
    atributo2=""
    comparacion2=""
    valor2=""
    Buscados=""
    for i in range(0, len(Condiciones)):
        transicion = Condiciones[i]
        if estado == 0:
            if transicion == "=":
                comparacion1+="="
                estado = 1
            elif transicion == "<":
                comparacion1+="<"
                estado = 1
            elif transicion ==">":
                comparacion1=">"
                estado = 1
            elif transicion=="!":
                comparacion1="!"
                estado = 1
            else:
                atributo1+=transicion
        elif estado == 1:
            if transicion == '"':
                estado = 2
            elif transicion == "=":
                comparacion1+="="
                estado=1
            else:
                valor1+=transicion
            if i == len(Condiciones)-1:
                estado=10
            if len(valor1)>=3:
                if valor1[len(valor1)-3:len(valor1)]=="and":
                    estado = 11
                    valor1=valor1[0:len(valor1)-3]
                    condicionAUsar=1
                if valor1[len(valor1)-3:len(valor1)]=="xor":
                    estado = 11
                    valor1=valor1[0:len(valor1)-3]
                    condicionAUsar = 3
            if len(valor1)>=2:
                if valor1[len(valor1)-2:len(valor1)]=="or":
                    estado = 11
                    valor1=valor1[0:len(valor1)-2]
                    condicionAUsar = 2
        elif estado == 2:
            if transicion=='"' and i == len(Condiciones)-1:
                estado = 10
            elif transicion=='"':
                estado =3
            else:
                valor1 += transicion
        elif estado == 3:
            if transicion=="a":
                estado=4
            elif transicion=="o":
                estado=6
            elif transicion=="x":
                estado=7
        elif estado == 4:
            if transicion =="n":
                estado=5
        elif estado==5:
            if transicion=="d":
                estado=11
                condicionAUsar=1
        elif estado==6:
            if transicion=="r":
                estado=11
        elif estado == 7:
            if transicion=="o":
                estado = 8
        elif estado == 8:
            if transicion=="r":
                estado=11
        elif estado == 11:
            if transicion == "=":
                comparacion2+="="
                estado = 12
            elif transicion == ">":
                comparacion2+=">"
                estado = 12
            elif transicion == "<":
                comparacion2+="<"
                estado = 12
            elif transicion == "!":
                comparacion2+="!"
                estado = 12
            else:
                atributo2+=transicion
        elif estado == 12:
            if transicion == '"':
                estado = 13
            elif transicion == "=":
                comparacion2+="="
                estado=12
            else:
                valor2+=transicion
                if i == len(Condiciones)-1:
                    estado=10
        elif estado == 13:
            if transicion=='"' and i == len(Condiciones)-1:
                estado = 10
            else:
                valor2 += transicion
    if estado==10:
        print("Funciona")
        print(atributo1)
        print(comparacion1)
        print(valor1)
        print(atributo2)
        print(comparacion2)
        print(valor2)
    else:
        print("Errores")
        print(atributo1)
        print(comparacion1)
        print(valor1)
        print(atributo2)
        print(comparacion2)
        print(valor2)
    for i in range(len(Encabezados)):
        if atributo1 == Encabezados[i]:
            Buscados+=str(i)+","
    for i in range(len(Encabezados)):
        if atributo2==Encabezados[i]:
            Buscados+=str(i)+""
    Buscados=Buscados.split(",")
    Buscados.pop(len(Buscados) - 1)
    if condicionAUsar==0:
        Temp=[]
        vals=""
        SeToma=0
        if comparacion1=="=":
            for i in range(len(Base)):
                for j in range(len(Encabezados)):
                    vals+=Base[i][j]+","
                    if int(Buscados[0])==j:
                        if valor1==Base[i][j].lower():
                            SeToma=1
                if SeToma==1:
                    vals = vals.split(",")
                    vals.pop(len(vals) - 1)
                    Temp.append(vals)
                    vals = ""
                    SeToma=0
            Base = Temp
        elif comparacion1=="<":
            print("Mientras")
        elif comparacion1==">":
            print("Mientras")
        elif comparacion1=="<=":
            print("Mientras")
        elif comparacion1==">=":
            print("Mientras")
        elif comparacion1=="!=":
            print("Mientras")
    return Base

##Método para ingresar los registros en la base de datos
def LlenarBase(cadena,Base):
    CadenaEncabezados = ""
    CadenaDatos = ""
    estado = 0
    for i in range(0, len(cadena)):
        transicion = cadena[i]
        if estado == 0:
            if transicion == "(":
                estado = 1
            else:
                return False
        elif estado == 1:
            if transicion == "<":
                estado = 2
                CadenaDatos=""
                CadenaEncabezados = ""
            elif transicion == ",":
                estado = 1
            elif transicion == ")":
                estado = 7
            else:
                return False
        elif estado == 2:
            if transicion == "[":
                estado = 3
            else:
                return False
        elif estado == 3:
            if transicion == "]":
                estado = 4
            else:
                CadenaEncabezados += transicion
        elif estado == 4:
            if transicion == "=":
                estado = 5
            else:
                return False
        elif estado == 5:
            if transicion == '"':
                estado = 6
            elif str.isalnum(transicion) or str.isnumeric(transicion) or transicion == "." or transicion == "-":
                CadenaDatos += transicion
            elif transicion == ",":
                estado = 2
                CadenaDatos += ","
                CadenaEncabezados += ","
            elif transicion == ">":
                estado = 1
                if Base.getVacio() == 0:
                    Base.setBDEncabezados(CadenaEncabezados.split(","))
                    Base.setColumnas(len(CadenaEncabezados.split(",")))
                    Base.setVacio(1)
                    Base.setBDNRegistros(CadenaDatos)
                    CadenaDatos=""
                else:
                    if Base.getDBEncabezados()==CadenaEncabezados.split(","):
                        Base.setBDNRegistros(CadenaDatos)
                        CadenaDatos=""
                    else:
                        print("El archivo no tiene la estructura de la base de datos")
                        return False
            else:
                return False
        elif estado == 6:
            if transicion != '"':
                CadenaDatos += transicion
            else:
                estado = 5
    if estado == 7:
        return Base
    else:
        return False

##Método para buscar base de datos y llenarla
def CargaraBaseDatos(NombreBase,Archivo):
    Registros = ""
    valor = 0
    for i in range(len(BD)):
        if NombreBase==BD[i].getNombre():
            Registros = ObtenerTexto(Archivo)
            BD[i] = LlenarBase(Registros, BD[i])
            print(BD[i].getBDNRegistros())
            valor=1
    if valor == 1:
        return True
    elif valor == 0:
        return False

##Método de pruega impresion temporal
def ImprimirBase(Base,Columnas):
    for i in range(0, len(Base)):
        for j in range(0, Columnas):
                print("[ ", Base[i][j], " ]", end="")
        print()

##Función para agregar el contenido del archivo aon a una variable
def ObtenerTexto(NombreArchivo):
    Registros = ""
    archivo = open(NombreArchivo,"r")
    for linea in archivo.readlines():
        Registros+=linea
    archivo.close()
    Registros = Registros.replace('\n', ' ').replace('\r', '').replace('         ', '').replace('     ', '').replace(" ","").replace("	","")
    return Registros

##Método para agregar sets
def AgregarBaseDatos(nombre):
    BaseN = BaseDatos(nombre,0,0)
    BD.append(BaseN)
    print("Set '"+nombre+"' creado con éxito")

while True:
    comando = input("Ingrese un comando: ")
    if comando !="salir":
        AFD = Automata(comando)
        if AFD.VerificarCadena() == True:
            continue
        else:
            print('El comando ' + comando + " NO es valido")
    else:
        break