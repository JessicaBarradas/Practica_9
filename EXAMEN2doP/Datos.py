class Datos():
    def __init__(self,nomb,AM,AP,AN,C,digitos):
        self.nomb=nomb
        self.AM=AM
        self.AP=AP
        self.AN=AN
        self.C=C
        self.digitos=digitos
        self.connect=False
    def conexion (self,nombre,apellidoM,apellidoP,carrera,añoNacimiento):
        if (nombre,apellidoM,apellidoP,carrera,añoNacimiento):
            nombre(input("Ingresa tu Nombre: "))
            apellidoP(input("Ingresa tu apellido Paterno: "))
            apellidoM(input("Ingresa tu apellido Materno: "))
            carrera(input("Ingresa tu Carrera: "))
            añoNacimiento(input("Ingresa tu año de Nacimiento: "))
        else:
            nombre=nombre
            apellidoP=apellidoP
            apellidoM=apellidoM
            carrera=carrera
            añoNacimiento=añoNacimiento
        if (nombre==self.nomb)and(apellidoP==self.AP)and(apellidoM==self.AM)and(carrera==self.C)and(añoNacimiento==self.AN):
            print("Conexion Exitosa")
            self.connect=True
            return True
        else:
            print("No se puede acceder")
    def digitos (self):
        return self.digitos
nom=Datos(input("Ingresa tu  nombre: "), input("Ingresa tu Apellido Paterno: "), input("Ingresa tu apellido Materno: "), input("Ingresa tu año de nacimiento: "), input("Ingresa tu carrera: "), input("Ingresa 3 digitos: "))
print(nom)
nom.conexion()
print(nom)
        

