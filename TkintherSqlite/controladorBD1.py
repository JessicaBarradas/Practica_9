from tkinter import messagebox
import sqlite3

class controladorBD:
    
    def __init__(self):
        pass
    
    #preparamos la conexión a la BD para cuando sea necesario usarla
    def conexionBD(self):
        
        try:
            conexion = sqlite3.connect("C:/Users/Jessy/Desktop/Practica_9/TkintherSqlite/POO_PI.db")
            print("Conectado a la base de datos")
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar a la BD")
    
    #Metodo para insertar
    def guardarUsuario(self, nom, cor, con):
        
        #1. llamar a la conexion
        conx = self.conexionBD()
        
        #2. Revisar parametros vacios
        if(nom == "" or cor == "" or con == ""):
           messagebox.showwarning("Cuidado!", "Ningún campo puede estar vacio")
           conx.close() 
        else:
            #3. Preparar los datos y el querySQL
            cursor = conx.cursor()
            datos = (nom, cor, con)
            qrInsert = "insert into Usuarios(Username, Password, Email) values(?,?,?)"
            
            #4. Proceder a insertar y cerramos la conx
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito!!", "Se guardo el usuario")
    
