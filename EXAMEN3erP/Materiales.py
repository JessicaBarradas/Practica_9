from tkinter import *
from tkinter import ttk
import tkinter as tk
from ControladorM import *
#Creamos un objeto de tipo controlador
controlador = controladorMat()
#Procedemos a insertar material usando el metodo InsertarM() del objeto controlador
def ejecutaInsertM():
    controlador.InsertarM(varMat.get(),IntCant.get())



ventana=Tk()
ventana.title("Ferreteria")
ventana.geometry("500x300")
panel=ttk.Notebook(ventana)
panel.pack(fill="both",expand="yes")

pestana1=ttk.Frame(panel)
pestana2=ttk.Frame(panel)
pestana3=ttk.Frame(panel)
#Pestana 1: Insertar Material
titulo=Label(pestana1,text="Insertar Material",fg="#8BD174",font=("Dongle",18)).pack()
#Material
varMat=tk.StringVar()
lblMat=Label(pestana1,text="Material: ").pack()
txtMat=Entry(pestana1,textvariable=varMat).pack()
#Cantidad
IntCant=tk.StringVar()
lbCant=Label(pestana1,text="Cantidad de material: ").pack()
txtCant=Entry(pestana1,textvariable=IntCant).pack()
#Boton
btnInsert=Button(pestana1,text="Insertar Material",command=ejecutaInsertM).pack()


panel.add(pestana1,text="Insertar Material")
panel.add(pestana2,text="Actualizar Material")
panel.add(pestana3,text="Consultar Materiales")


ventana.mainloop()