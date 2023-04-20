from tkinter import messagebox
import sqlite3 

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
            datos =(Mat, Cant)
            qrInsert="insert into MatConstruccion(Material,Cantidad) values(?,?)"
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito!!","Se guardo el material")      
    def actualizarMat(self,id,Mater,Canti):
        conx=self.conexionBD()
        if (id=="" or Mater=="" or Canti==""):
            messagebox.showwarning("Advertencia","Ningun campo puede estar vacio")
            conx.close()
        else:
            try:
                cursor=conx.cursor()
                Material=Mater
                Cantidad=Canti
                sqlActu="UPDATE MatConstruccion SET Material=?, Cantidad=? WHERE IDMat=?"
                cursor.execute(sqlActu,[Material,Cantidad,id])
                MatActu=cursor.fetchall()
                conx.commit()
                conx.close()
                messagebox.showinfo("ENHORABUENA","Datos actualizados correctamente")
                return MatActu
            except sqlite3.OperationalError:
                messagebox.showerror("ERROR","Error en la consulta")
    def consultaMaterial(self,id):
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
                sqlSelect="Select * from MatConstruccion where IDMat="+id
            #5.Ejecucuion y guardado de la consulta
                cursor.execute(sqlSelect)
                RSMaterial=cursor.fetchall()
                conx.close()
                return RSMaterial
            except sqlite3.OperationalError:
                print("Error consulta")
    def consultarMat(self):
        conx=self.conexionBD()
        cursor=conx.cursor()
        try:
            sqlConsu="Select * from MatConstruccion"
            cursor.execute(sqlConsu)
            Consulta=cursor.fetchall()
            conx.close()
            return Consulta
        except sqlite3.OperationalError:
            messagebox.showwarning("Advertencia","No se encontro ningún usuario")