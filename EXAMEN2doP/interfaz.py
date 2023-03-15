from tkinter import Tk,Label,Frame,Entry,Button,StringVar,messagebox,IntVar
from Datos import  *

Matricula=Tk()
Nombre=StringVar()
ApellidoP=StringVar()
ApellidoM=StringVar()
Carrera=StringVar()
Año=IntVar()
Digitos=IntVar()
def CreateMatricula():
    Matricula.title("Matricula")
    Matricula.geometry("300x200")
    seccion1=Frame(Matricula,bg="#652379")
    seccion1.pack(expand=True,fill="both")
