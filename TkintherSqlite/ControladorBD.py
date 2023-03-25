from tkinter import messagebox
import sqlite3 
import bcrypt

class controladorBD:
    def __init__(self):
        pass
#Preparamos la conexion a la BD para cuando sea necesario usarla
    def conexionBD(self):
        try:
            conexion=sqlite3.connect("C:/Users/Jessy/Desktop/Practica_9/TkintherSqlite/DBUsuarios.db")
            print("Conexion exitosa")
            return conexion

        except sqlite3.OperationalError:
            print("Conexion erronea")
#Metodo para insertar 
    def GuardarUsuario(self,nom,cor,con):
        conx=self.conexionBD()
        if(nom == "" or cor == "" or con == ""):
            messagebox.showwarning("Error!","Llena todos los registros")
            conx.close()
        else:
            cursor = conx.cursor()
            conH =self.encriptarCon(con)
            datos =(nom,cor,conH)
            qrInsert="insert into TBRegistrados(nombre,correo,contra) values(?,?,?)"
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito!!","Se guardo al usuario")
    def encriptarCon(self,con):
        conPlana=con
        conPlana=conPlana.encode()
        sal = bcrypt.gensalt()
        conHa= bcrypt.hashpw(conPlana,sal)
        return conHa
    
