class Usu():
    cantUsu=3
    def __init__(self,nomb,password) :
        self.nomb = nomb
        self.password = password
        self.conec = False
        self.intento=2
        Usu.cantUsu+=1
    def conexion (self,pass2=None,Usu2=None):
        if (pass2==None)and(Usu2==None):
            cont=input("Ingresa tu cotraseña: ")
            Usuar=input("Ingresa tu usuario: ")
        else:
            cont=pass2
            Usuar=Usu2
        if (cont==self.password)and(Usu2==self.nomb):
             print("Conexion Exitosa :)")
             self.conec=True
             return True
        else:
            self.intento-=1
            if self.intento < 0:
                print("Datos incorrectos, intente nuevamente, revise sus datos :( )")
                if (pass2!=None)and(Usu2!=None):
                    return False
                print("Tus intentos son: ", self.intento)
                self.conec()
            else:
                print("No se puede acceder :(")
    def __str__(self):
        if self.conec:
            conexion="Conectad@"
        else:
            conexion="Desconectad@"
        return f"El usuario es {self.nomb} y esta {conexion}"
    
#usu1=Usu(input("Ingrese un Nombre de usuario: "), input("Ingrese una contraseña: "))
#print(usu1)
#usu1.conexion()
#print(usu1)
