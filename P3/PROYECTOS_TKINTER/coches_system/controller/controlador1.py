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
    
    #CAMIONETAS
    @staticmethod
    def insertar_camioneta(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada):
        resultado = messagebox.askquestion(icon="question",message=f"¿Deseas Guardar el auto con los siguientes datos?: "
                                           f"\n marca: {marca} \n color: {color} \n modelo: {modelo} \n velocidad: {velocidad} \n potencia: {potencia} \n plazas: {plazas} \n traccion: {traccion} \n cerrada: {cerrada}")
        if resultado:
            cochesBD.Camionetas.insertar(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
        else:
            pass 
    
    @staticmethod
    def consultar_camioneta():
        return cochesBD.Camionetas.consultar()
    
    @staticmethod
    def consultar_id_camioneta(id):
        try:
            cursor.execute("select * from camionetas where id_Camionetas=%s",(id,))
            return cursor.fetchone()
        except:    
            return []
        
    @staticmethod
    def cambiar_camioneta(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada,id):
        resultado = messagebox.askquestion(icon="question",message=f"¿Desea actualizar la camioneta con el ID: {id}")
        if resultado:
            cochesBD.Camionetas.actualizar(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada,id)
        else:
            pass

    @staticmethod
    def eliminar_camioneta(id):
        resultado = messagebox.askquestion(icon="warning",message=f"¿Eliminar definitivamente la camioneta con el ID: {id}")
        if resultado:
            cochesBD.Camionetas.eliminar(id)
        else:
            pass


    