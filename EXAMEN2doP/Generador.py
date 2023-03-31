from tkinter import *
from DatosGenerador import *

Matricula=Tk()
Matricula.title("Matricula")
Matricula.geometry("400x200")

Nombre=Label(Matricula, text="Ingresa tu nombre")
Nombre.grid(row=2,column=1)
nomb=Entry(Matricula)
nomb.grid(row=2,column=2)
ApellidoPaterno=Label(Matricula, text="Ingresa tu Apellido Paterno")
ApellidoPaterno.grid(row=4,column=1)
AP=Entry(Matricula)
AP.grid(row=4,column=2)
ApellidoMaterno=Label(Matricula, text="Ingresa tu Apellido Materno")
ApellidoMaterno.grid(row=6,column=1)
AM=Entry(Matricula)
AM.grid(row=6,column=2)
AñoNacimiento=Label(Matricula, text="Ingresa tu año de nacimiento")
AñoNacimiento.grid(row=8,column=1)
AN=Entry(Matricula)
AN.grid(row=8,column=2)
Carrera=Label(Matricula, text="Ingresa tu carrera actualmente")
Carrera.grid(row=10,column=1)
C=Entry(Matricula)
C.grid(row=10,column=2)
AñoCursando=Label(Matricula, text="Ingresa el año que estas actualmente")
AñoCursando.grid(row=12,column=1)
AC=Entry(Matricula)
AC.grid(row=12,column=2)

def Generar():
    nombre=nomb.get()
    ApellidoP=AP.get()
    ApellidoM=AM.get()
    AñoNaci=AN.get()
    Car=C.get()
    AñoCursa=AC.get()
    Matricula=Datos(nombre,ApellidoP,ApellidoM,AñoNaci,Car,AñoCursa)
    Matricula.GenerarMatricula()
Generador=Button(Matricula, text="Generar Matricula",bg="#B1B9F1",command=Generar)
Generador.grid(row=14,column=1)
Matricula.mainloop()