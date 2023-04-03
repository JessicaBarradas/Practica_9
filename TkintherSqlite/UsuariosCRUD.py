from tkinter import *
from tkinter import ttk
import tkinter as tk
from ControladorBD import *


#Creamos un objeto de tipo controlador
controlador = controladorBD()
#Procedemos a guardar usuarios usando el metodo GuardarUsuarios() del objeto controlador
def ejecutaInsert():
    controlador.GuardarUsuario(varNom.get(),varCor.get(),varCon.get())
#Funcion para buscar un usuario
def ejecutaSelectU():
    rsUsuario= controlador.consultaUsuario(varBus.get())
    for usu in rsUsuario:
        cadena=str(usu[0])+" "+usu[1]+" "+usu[2]+" "+str(usu[3])
    if(rsUsuario):
        textBus.insert("0.0",cadena)
    else:
        messagebox.showinfo("No encontrado", "Usuario no registrado en la BD")
#Función para mostrar a todos los usuarios 
def ejecutaConsultaUsu():
    consulta=controlador.consultarUsu()
    tabUsu.delete(*tabUsu.get_children())
    for user in consulta:
        tabUsu.insert("",tk.END,text="",values=user)



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
btnGuardar=Button(pestana1,text="Guardar Usuario",command=ejecutaInsert).pack()

#pestaña 2:Buscar Usuario
titulo2= Label(pestana2,text="Buscar Usuario",fg="green",font=("Modern",18)).pack()
varBus=tk.StringVar()
lblid=Label(pestana2,text="Identificador de Usuario: ").pack()
txtid=Entry(pestana2,textvariable=varBus).pack()
btnBusqueda=Button(pestana2,text="Buscar",command=ejecutaSelectU).pack()
subBus=Label(pestana2,text="Registrado: ",fg="blue",font=("Modern",15)).pack()
textBus=tk.Text(pestana2,height=5,width=52)
textBus.pack()

#Pestaña 3: Consultar usuario
titulo3=Label(pestana3,text="Consultar Usuarios",fg="red",font=("Modern",18)).pack()
btnConsulta=Button(pestana3,text="Consultar",command=ejecutaConsultaUsu).pack()
#Tabla
columns=("id","nombre","correo","contra")
tabUsu=ttk.Treeview(pestana3,columns=columns,show="headings")
tabUsu.column("id",anchor=tk.W,width=30)
tabUsu.column("nombre",anchor=tk.W,width=150)
tabUsu.column("correo",anchor=tk.W,width=150)
tabUsu.column("contra",anchor=tk.W,width=150)
tabUsu.heading("id",text="ID")
tabUsu.heading("nombre",text="NOMBRE")
tabUsu.heading("correo",text="CORREO")
tabUsu.heading("contra",text="CONTRASEÑA")
tabUsu.pack()

panel.add(pestana1,text="Formulario de Usuarios")
panel.add(pestana2,text="Buscar Usuario")
panel.add(pestana3,text="Consultar Usuarios")
panel.add(pestana4,text="Actualizar Usuarios")


ventana.mainloop()