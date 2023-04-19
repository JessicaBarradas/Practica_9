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
titulo=Label(pestana1,text="Insertar Material",fg="#8BD172",font=("Dongle",18)).pack()
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
#Pestaña 2: Actualiza material
titulo2 = Label(pestana2, text = "Actualizar Material", fg ="#82A7E5", font = ("Modern", 18)).pack()
variID = tk.StringVar()
variMat = tk.StringVar()
variCant = tk.StringVar()
lablid = Label(pestana2, text = "ID del Material: ").pack()
textid = Entry(pestana2, textvariable = variID).pack()
lablMat = Label(pestana2, text = "Escribe el nuevo nombre del Material: ").pack()
textMat = Entry(pestana2, textvariable = variMat).pack()
lablCant = Label(pestana2, text = "Escribe la nueva cantidad del Material: ").pack()
textCant = Entry(pestana2, textvariable = variCant).pack()
btnActualizar=Button(pestana2,text="Actualizar").pack()
#Pestaña 3: Consultar todos
titulo3=Label(pestana3,text="Consultar Materiales",fg="red",font=("Modern",18)).pack()
btnConsulta=Button(pestana3,text="Consultar").pack()
#Tabla
columns=("IDMat","Material","Cantidad")
tabMat=ttk.Treeview(pestana3,columns=columns,show="headings")
tabMat.column("IDMat",anchor=tk.W,width=30)
tabMat.column("Material",anchor=tk.W,width=150)
tabMat.column("Cantidad",anchor=tk.W,width=150)
tabMat.heading("IDMat",text="ID")
tabMat.heading("Material",text="MATERIAL")
tabMat.heading("Cantidad",text="CANTIDAD")
tabMat.pack()


panel.add(pestana1,text="Insertar Material")
panel.add(pestana2,text="Actualizar Material")
panel.add(pestana3,text="Consultar Materiales")


ventana.mainloop()