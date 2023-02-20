class Personaje:
    #atributos del personaje por default
    especie= "humano"
    nombre= "Master Chief"
    altura= "2.70"
    #metodos del personaje
    def correr(self,status):
        if(status):
            print("el personaje " + self.nombre + "esta corriendo")
        else:
            print("el personaje " + self.nombre + "se detuvo")
    def lanzarGranadas(self):
            print("el personaje " + self.nombre + "lanzo una granada")
    def recargarArma(self, municiones):
        cargador= 10
        cargador= cargador + municiones
        print("el arma tiene " + str (cargador)+" balas")