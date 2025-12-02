from tkinter import messagebox
from model import operaciones
from conexionBD import *
#Control App o controller

class Funciones:
    @staticmethod
    def resultado(tipo,numero1,numero2):
        if tipo == "suma":
            ope=numero1+numero2
            signo="+"
            
        elif tipo == "resta":
            ope=numero1-numero2
            signo="-"
            
        elif tipo == "multiplicacion":
            ope=numero1*numero2
            signo="*"
        
        elif tipo == "division":
            ope=numero1/numero2
            signo="/"
            
        #messagebox.showinfo(title=f"{tipo}",message=f"{numero1} {signo} {numero2} = {ope}",icon="info")
        
        resultado=messagebox.askquestion(message=f"{numero1} {signo} {numero2} = {ope} \n\n Deseas guardar en la base de datos?",icon="question")
        if resultado == "yes":
            operaciones.Operaciones.insertar(numero1,numero2,signo,ope)
        else:
            pass

    #aqui va el metodo

    @staticmethod
    def consultar_id(id):
          try:
            cursor.execute("select * from operaciones where id=%s",(id,))
            return cursor.fetchone()
          except:    
            return []