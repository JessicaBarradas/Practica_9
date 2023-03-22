from tkinter import *
from tkinter import ttk
import tkinter as tk

ventana=Tk()
ventana.title("CRUD Usuarios")
ventana.geometry("500x300")

panel=ttk.Notebook(ventana)
panel.pack(fill="both",expand="yes")

pestana1=ttk.Frame(panel)
pestana2=ttk.Frame(panel)
pestana3=ttk.Frame(panel)
pestana4=ttk.Frame(panel)

#Comienza la pestaña 1: Formulario de Usuarios
titulo=Label(pestana1,text="Registro de Usuarios",fg="Blue",font=("Modern",18)).pack()
#Nombre
varNom=tk.StringVar()
lblNom=Label(pestana1,text="Nombre: ").pack()
txtNom=Entry(pestana1,textvariable=varNom).pack()
#Correo
varCor=tk.StringVar()
lblCor=Label(pestana1,text="Correo: ").pack()
txtCor=Entry(pestana1,textvariable=varCor).pack()
#Contraseña
varCon=tk.StringVar()
lblCon=Label(pestana1,text="Contraseña: ").pack()
txtCon=Entry(pestana1,textvariable=varCon).pack()
#Boton
btnGuardar=Button(pestana1,text="Guardar Usuario").pack()

panel.add(pestana1,text="Formulario de Usuarios")
panel.add(pestana2,text="Buscar Usuario")
panel.add(pestana3,text="Consultar Usuarios")
panel.add(pestana4,text="Actualizar Usuarios")


ventana.mainloop()