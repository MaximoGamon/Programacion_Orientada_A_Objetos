"""
Crear una calculadora:
1.- Dos campos de texto
2.- 4 botones para las Operaciones
3.- Mostrar el resultado en una alerta
4.- Porgramado de forma Orientada a Objetos
5.- Considerar el MVC
"""

from tkinter import *

from view import interfaz

class App:
    #Constructor
    # def __init__(self,ventana):
        #ejecutar la ventana
        @staticmethod
        def main(ventana):
            view=interfaz.vista(ventana)



if __name__ == "__main__":
    ventana=Tk()
    #3constructor
    #app=App(ventana) 
    App.main(ventana)
    ventana.mainloop()