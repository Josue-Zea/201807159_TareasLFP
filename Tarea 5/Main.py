cadena1 = "__servidor1"
cadena2 = "3servidor"

class Automata:
    def __init__(self,cadena):
        self.cadena = cadena

    def VerificarCadena(self):
        self.estado=0
        for i in range(0,len(self.cadena)):
            self.transicion = self.cadena[i]
            if self.estado == 0:
                if str.isalnum(self.transicion) or self.transicion == "_":
                    if str.isalnum(self.transicion):
                        self.estado = 2
                    elif self.transicion == "_":
                        self.estado = 1
                else:
                    return False
            elif self.estado == 1:
                if str.isalnum(self.transicion) or self.transicion == "_":
                    if str.isalnum(self.transicion):
                        self.estado = 3
                    elif self.transicion == "_":
                        self.estado = 1
                else:
                    return False
            elif self.estado == 2:
                if str.isalnum(self.transicion) or str.isnumeric(self.transicion):
                    if str.isalnum(self.transicion):
                        self.estado = 2
                    elif str.isnumeric(self.transicion):
                        self.estado = 4
                else:
                    return False
            elif self.estado == 3:
                if str.isnumeric(self.transicion) or str.isalnum(self.transicion):
                    if str.isnumeric(self.transicion):
                        self.estado = 4
                    elif str.isalnum(self.transicion):
                        self.estado = 3
                else:
                    return False
        if self.estado == 4:
            return True
        else:
            return False

def LlamarCadenas(cadena):
    AFD = Automata(cadena)
    if AFD.VerificarCadena() == True:
        print('La cadena '+cadena+" es valida")
    else:
        print('La cadena ' + cadena + " NO es valida")

def main():
    LlamarCadenas(cadena1)
    LlamarCadenas(cadena2)

if __name__ == "__main__":
    main()
