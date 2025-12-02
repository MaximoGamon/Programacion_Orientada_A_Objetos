from tkinter import *
from view import interfaz


class App:
    def __init__(self,ventana):
        vista=interfaz.View(ventana)
    

if __name__ == "__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()