from tkinter import messagebox
from model import cochesBD
from conexionBD import *

class funciones:
    
    @staticmethod
    def insertar_resultados_auto(marca,color,modelo,velocidad,potencia,plazas):
        resultado = messagebox.askquestion(icon="question",message=f"¿Deseas Guardar el auto con los siguientes datos?: "
                                           f"\n marca: {marca} \n color: {color} \n modelo: {modelo} \n velocidad: {velocidad} \n potencia: {potencia} \n plazas: {plazas}")
        if resultado:
            cochesBD.Autos.insertar(marca,color,modelo,velocidad,potencia,plazas)
        else:
            pass

    @staticmethod
    def consultar_id(id):
          try:
            cursor.execute("select * from coches where id=%s",(id,))
            return cursor.fetchone()
          except:    
            return []
          
    @staticmethod
    def cambiar_auto(marca,color,modelo,velocidad,potencia,plazas,id):
        resultado = messagebox.askquestion(icon="question",message=f"¿Desea actualizar el auto con el ID: {id}")
        if resultado:
            cochesBD.Autos.actualizar(marca,color,modelo,velocidad,potencia,plazas,id)
        else:
            pass
    
    @staticmethod
    def eliminar_auto(id):
        resultado = messagebox.askquestion(icon="warning",message=f"¿Eliminar definitivamente el auto con el ID: {id}")
        if resultado:
            cochesBD.Autos.eliminar(id)
        else:
            pass
            

    