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
    def consultarUsu(self):
        conx=self.conexionBD()
        cursor=conx.cursor()
        try:
            sqlConsu="Select * from TBRegistrados"
            cursor.execute(sqlConsu)
            Consulta=cursor.fetchall()
            conx.close()
            return Consulta
        except sqlite3.OperationalError:
            messagebox.showwarning("Advertencia","No se encontro ningún usuario")
    def actualizarUsu(self,id,nomact,coract,conact):
        conx=self.conexionBD()
        if (id=="" or nomact=="" or coract=="" or conact==""):
            messagebox.showwarning("Advertencia","Ningun campo puede estar vacio")
            conx.close()
        else:
            try:
                cursor=conx.cursor()
                nomb=nomact
                correo=coract
                conH=self.encriptarCon(conact)
                sqlActu="UPDATE TBRegistrados SET nombre=?, correo=?, contra=? WHERE id=?"
                cursor.execute(sqlActu,[nomb,correo,conH,id])
                usuActu=cursor.fetchall()
                conx.commit()
                conx.close()
                messagebox.showinfo("ENHORABUENA","Datos actualizados correctamente")
                return usuActu
            except sqlite3.OperationalError:
                messagebox.showerror("ERROR","Error en la consulta")
    def EliminarUsu(self,ID):
        conx=self.conexionBD()
        if(ID==""):
            messagebox.showwarning("CUIDADO","No puede estar ningun campo vacio")
            conx.close()
        else:
            try:
                cursor=conx.cursor()
                sqlEliminar="DELETE FROM TBRegistrados WHERE id=?"
                cursor.execute(sqlEliminar,[ID])
                EliminarU=cursor.fetchall()
                conx.commit()
                conx.close()
                messagebox.showinfo("ENHORABUENA","El usuario se ha eliminado correctamente")
                return EliminarU
            except sqlite3.OperationalError:
                messagebox.showerror("ERROR","Error en la consulta")