import random
from tkinter import messagebox

class Datos():
    def __init__(self,nomb,AP,AM,AN,C,AC):
        self.nombre=nomb
        self.ApePa=AP
        self.ApeMa=AM
        self.AñoNa=AN
        self.Carre=C
        self.AñoCur=AC
        #nomb=str(nomb)
        #ApePa=str(ApePa)
        #ApeMa=str(ApeMa)
        #AñoNa=str(AñoNa)
        #Carre=str(Carre)
        #AñoCur=str(AñoCur)
    def GenerarMatricula(self):
        nomb=self.nombre[0]
        AP=self.ApePa[:3]
        AM=self.ApeMa[:3]
        AN=self.AñoNa[2:4]
        C=self.Carre[:3]
        AC=self.AñoCur[2:4]
        Numero=str(random.randint(100,999))
        Matricula=str(C)+str(AC)+str(AN)+str(nomb)+str(AP)+str(AM)+Numero
        Matri=Matricula.upper()
        messagebox.showinfo("Tu matricula es ",str(Matri))