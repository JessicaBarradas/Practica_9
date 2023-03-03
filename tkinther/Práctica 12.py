from tkinter import Tk,Label,Frame,StringVar,Entry,Button,messagebox
from usu import *

login=Tk()
Usuario=StringVar()
Contraseña=StringVar()
def CreateLogin():
    login.title("Login")
    login.geometry("300x200")
    seccion1=Frame(login,bg="#EC9090")
    seccion1.pack(expand=True, fill="both")
    PedirUsu=Label(seccion1, bg="#C1A6EC", text="Acceder a cuenta")
    PedirUsu.grid(column=1, row=0, padx=20, pady=20,columnspan=2)
    Usua=Label(seccion1, bg="#A6B3EC", text="Usuario")
    Usua.grid(column=0,row=1)
    Pass=Label(seccion1,bg="#A6ECB7",text="Contraseña")
    Pass.grid(column=0,row=2)
    Usuario.set("")
    InsertarUsua=Entry(seccion1,textvariable=Usuario,bg="#C5CBEA")
    InsertarUsua.grid(column=1,row=1)
    Contraseña.set("")
    InsertarPass=Entry(seccion1,textvariable=Contraseña,show="*", bg="#CDECC2")
    InsertarPass.grid(column=1,row=2)
    Acceder=Button(seccion1,text="Acceder",bg="#39CA30",command=acceder)
    Acceder.grid(column=2,row=3)
    login.mainloop()
def acceder():
    test=usu1.conexion(Contraseña.get(),Usuario.get())
    if test:
        messagebox.showinfo("ENHORABUENA","Accedio correctamente")
    else:
        messagebox.showerror("ERROR","Acceso denegado")
if __name__=="__main__":
    #usu1=Usu(input("Ingrese un Nombre de usuario: "), input("Ingrese una contraseña: "))
    usu1=Usu("Jessica","JessicaA")
    CreateLogin()