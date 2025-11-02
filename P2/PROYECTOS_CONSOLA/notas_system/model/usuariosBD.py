from conexionBD import *
import hashlib
import datetime

class Usuario:
    def __init__(self,nombre,apellido,email,password,fecha):
        self._nombre=nombre
        self._apellido=apellido
        self._email=email
        self._password=password
        self._fecha=fecha

    @staticmethod  
    def registrar (nombre,apellido,email,password):
        try:
            password=hashlib.sha256(password.encode()).hexdigest()
            fecha=datetime.datetime.now()
            cursor.execute(
                "insert into usuarios values(null,%s,%s,%s,%s,%s)",
                (nombre,apellido,email,password,fecha)
            )
            conexion.commit()
            return True
        except:
            return False
    @staticmethod
    def iniciar_sesion(email,password):
        try:
            password=hashlib.sha256(password.encode()).hexdigest()
            cursor.execute(
                "select * from usuarios where email=%s and password=%s",
                (email,password)
            )
            usuario=cursor.fetchone()
            if usuario:
                return usuario
            else:
                return None 
                 
        except:
            return None

        