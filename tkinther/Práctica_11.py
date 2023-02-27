from tkinter import Tk,Button,Frame,messagebox
def mostrarMensajes():
    messagebox.showinfo("showinfo", "Presionaste el boton Azul")
#1.Instanciamos el objeto ventana
ventana=Tk()
ventana.title("Ejemplo de 3 Frames ")
ventana.geometry("690x400")
#2.Agregamos los Frames
seccion1= Frame(ventana,bg="red")
seccion1.pack(expand=True,fill='both')
seccion2= Frame(ventana,bg="blue")
seccion2.pack(expand=True,fill='both')
seccion3= Frame(ventana,bg="pink")
seccion3.pack(expand=True,fill='both')
#3. Agregamos botones
botonAzul=Button(seccion1,text="Boton Azul",fg="blue",command=mostrarMensajes)
botonAzul.place(x=60 , y=60) 
botonAmarillo=Button(seccion2,text="Boton Amarillo",bg="#FFF933")
botonAmarillo.grid(row=1, column=1)
botonNegro=Button(seccion2,text="Boton Negro",fg="white",bg="#000000") 
botonNegro.grid(row=0, column=0)
botonVerde=Button(seccion3,text="Boton Verde", bg="#46C91F")
botonVerde.configure(height=2,width=10)
botonVerde.pack()
#llamamos al Main
ventana.mainloop()

