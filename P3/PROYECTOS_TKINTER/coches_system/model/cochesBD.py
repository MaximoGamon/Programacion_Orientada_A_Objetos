from conexionBD import *

class Autos:
    def __init__(self,marca,color,modelo,velocidad,potencia,plazas):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._potenica=potencia
        self._plazas=plazas

    @staticmethod
    def insertar(marca,color,modelo,velocidad,potencia,plazas):
        try:
            cursor.execute(
                "insert into coches values(null,%s,%s,%s,%s,%s,%s)",
                (color,marca,modelo,velocidad,potencia,plazas)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute("select * from coches")
            return cursor.fetchall()
        except:
            return []

    @staticmethod
    def actualizar(marca,color,modelo,velocidad,potencia,plazas,id):
        try:
            cursor.execute(
                "update coches set color=%s, marca=%s, modelo=%s, velocidad=%s, potencia=%s ,plazas =%s where id =%s"
                ,(color,marca,modelo,velocidad,potencia,plazas,id))
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute(
                "delete from coches where id=%s",(id,))
            conexion.commit()
            return True
        except:
            return False
        
    


class Camionetas:
    
    @staticmethod
    def insertar(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada):
        try:
           cursor.execute(
               "insert into camionetas values(null,%s,%s,%s,%s,%s,%s,%s,%s)",
               (marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
           )
           conexion.commit()
           return True
        except:
            return False  
        

    @staticmethod
    def consultar():
        try:
            cursor.execute("select * from camionetas")
            return cursor.fetchall()
        except:
            return []  
        
    @staticmethod    
    def actualizar(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada,id):
        try:
            cursor.execute(
                "update camionetas set marca=%s, color=%s, modelo=%s, velocidad=%s, potencia=%s,plazas =%s, traccion=%s,cerrada=%s where id_Camionetas =%s"
                ,(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada,id)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute(
                "delete from camionetas where id_Camionetas=%s",(id,))
            conexion.commit()
            return True
        except:
            return False


class Camiones:
    
    @staticmethod
    def insertar(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga):
        try:
           cursor.execute(
               "insert into camiones values(null,%s,%s,%s,%s,%s,%s,%s,%s)",
               (color,marca,modelo,velocidad,potencia,plazas,eje,capacidadCarga)
           )
           conexion.commit()
           return True
        except:
            return False   

    @staticmethod    
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id):
        try:
            cursor.execute(
                "update camiones set color=%s, marca=%s,  modelo=%s, velocidad=%s, potencia=%s ,plazas =%s, eje=%s,capacidad_Carga=%s where id_camiones =%s"
                ,(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id)
            )
            conexion.commit()
            return True
        except:
            return False
 
        
    @staticmethod
    def consultar():
        try:
            cursor.execute("select * from camiones")
            return cursor.fetchall()
        except:
            return []
        
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute(
                "delete from camiones where id_camiones=%s",(id,))
            conexion.commit()
            return True
        except:
            return False
        
