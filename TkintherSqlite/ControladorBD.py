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
    def consultaUsuario(self,id):
        #1. Preparar la conexión
        conx=self.conexionBD()
        #2. Veificar que el ID no este vacio
        if(id==""):
            messagebox.showwarning("Cuidado","ID vacio escribe uno valido")
            conx.close()
        else:
            #proceder a buscar
            try:
                #4. Preparar lo necesario para el select
                cursor=conx.cursor()
                sqlSelect="Select * from TBRegistrados where id="+id
            #5.Ejecucuion y guardado de la consulta
                cursor.execute(sqlSelect)
                RSusuario=cursor.fetchall()
                conx.close()
                return RSusuario
            except sqlite3.OperationalError:
                print("Error consulta")
    
