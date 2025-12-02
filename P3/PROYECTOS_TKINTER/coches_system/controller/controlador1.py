from tkinter import messagebox
from model import cochesBD
from conexionBD import *

class funciones:
    @staticmethod
    def consultar_id(id):
          try:
            cursor.execute("select * from coches where id=%s",(id,))
            return cursor.fetchone()
          except:    
            return []
    