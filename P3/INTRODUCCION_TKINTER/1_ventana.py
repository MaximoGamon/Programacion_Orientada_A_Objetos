"""
Tkinter trabaja a traves de interfaces, es una biblioteca de python que
permite crear aplicaciones en python para escritorio
"""
#1er Forma
#from tkinter import *

#2da Forma
import tkinter as tk

ventana = tk.Tk()

ventana.title("Mi primera ventana grafica en Tkinter con python")
ventana.geometry("800x600")
ventana.resizable(True,True)#Metodo para redimensionar el tamaño de la ventana
ventana.mainloop() #metodo que permite tener la ventana abierta e interactuar con ella



