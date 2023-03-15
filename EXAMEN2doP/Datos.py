class Datos():
    def __init__(self,nomb,AM,AP,AN,C,digitos):
        self.nomb = nomb
        self.AM = AM
        self.AP = AP
        self.AN = AN
        self.C = C
        self.digitos = digitos
        self.connect=False
    def conexion (self,nombre,apellidoP,apellidoM,carrera,añoNacimiento,digitos):
        if (nombre,apellidoP,apellidoM,carrera,añoNacimiento,digitos):
            nombre(input("Ingresa tu Nombre: "))
            apellidoP(input("Ingresa tu apellido Paterno: "))
            apellidoM(input("Ingresa tu apellido Materno: "))
            carrera(input("Ingresa tu Carrera: "))
            añoNacimiento(input("Ingresa tu año de Nacimiento: "))
            digitos(input("Ingresa 3 digitos: "))
        else:
            nombre=nombre
            apellidoP=apellidoP
            apellidoM=apellidoM
            carrera=carrera
            añoNacimiento=añoNacimiento
            digitos=digitos
        if (nombre==self.nomb)and(apellidoP==self.AP)and(apellidoM==self.AM)and(carrera==self.C)and(añoNacimiento==self.AN)and(digitos==self.digitos):
            print("Conexion Exitosa")
            self.connect=True
            return True
        else:
            print("No se puede acceder")
    def __str__(self):
        if self.connect:
            conexion="Conectad@"
        else:
            conexion="Desconectad@"
        return f"El usuario es {self.nomb} y esta {conexion}"
    def Ca (self):
        if (C):
            C=C(3)
        return C
    def AoNa (self):
        if(AN):
            AN=AN(2)
        return AN
    def nombr(self):
        if(nomb):
            nomb=nomb(1)
        return nomb
    def ApPa(self):
        if(AP):
            AP=AP(3)
        return AP
    def ApMa(self):
        if(AM):
            AM=AM(3)
        return AM
    def digi (self):
        return self.digitos
    
nom=Datos(input("Ingresa tu  nombre: "), input("Ingresa tu Apellido Paterno: "), input("Ingresa tu apellido Materno: "), input("Ingresa tu año de nacimiento: "), input("Ingresa tu carrera: "), input("Ingresa 3 digitos: "))
print(nom)
nom.conexion()
print(nom)
        

