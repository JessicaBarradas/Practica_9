from tkinter import messagebox
import sqlite3 
import bcrypt

class controladorMat:
    def __init__(self):
        pass
#Preparamos la conexion a la BD 
    def conexionBD(self):
        try:
            conexion=sqlite3.connect("C:/Users/Jessy/Desktop/Practica_9/EXAMEN3erP/Ferreteria.db")
            print("Conexion exitosa")
            return conexion

        except sqlite3.OperationalError:
            print("Conexion erronea")
#Metodo de Insertar
    def InsertarM(self,Mat,Cant):
        conx=self.conexionBD()
        if(Mat == "" or Cant == ""):
            messagebox.showwarning("Error!","Llena todos los registros")
            conx.close()
        else:
            cursor = conx.cursor()
            datos =(Mat,Cant)
            qrInsert="insert into MatConstruccion(Material, Cantidad) values(?,?)"
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito!!","Se guardo el material")        
