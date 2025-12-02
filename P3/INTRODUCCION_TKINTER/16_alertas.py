from tkinter import *
from tkinter import messagebox

ventana=Tk()
ventana.geometry("500x500")
ventana.title("Alertas")

def alerta1():
    nombreObtenido=cadena.get()
    etiqueta.config(text=f"{nombreObtenido}")
    resultado=messagebox.showinfo(message=f"{nombreObtenido}",icon="info")

def alerta2():
    resultado=messagebox.askquestion(message="Quieres continuar ejecutando la aplicacion?",icon="question")
    if resultado != "yes":
        ventana.destroy()

cadena=StringVar()
caja1=Entry(ventana,textvariable=cadena)
caja1.pack()

boton1=Button(ventana,text="Alerta",command=alerta1)
boton1.pack()

boton2=Button(ventana,text="Otra alerta",command=alerta2)
boton2.pack()

etiqueta=Label(ventana,text="")
etiqueta.pack()


ventana.mainloop()