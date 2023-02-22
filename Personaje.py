class Personaje:

    #Definimos el constructor de personaje
    def _init_(self,esp,nom,alt):
        self.especie= esp
        self.nombre= nom
        self.altura= alt

    #metodos del personaje
    def correr(self,status):
        if(status):
            print("el personaje " + self.nombre + " esta corriendo")
        else:
            print("el personaje " + self.nombre + " se detuvo")
    def lanzarGranadas(self):
            print("el personaje " + self.nombre + " lanzo una granada")
    def recargarArma(self, municiones):
        cargador= 10
        cargador= cargador + municiones
        print("el arma tiene " + str (cargador)+" balas")