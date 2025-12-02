from tkinter import *
from tkinter import messagebox
from controller import funciones

#Interfaz VIEW
def interfaz_principal():
    ventana = Tk()
    ventana.title("Calculadora")
    ventana.geometry("500x500")
    ventana.resizable(False,False)

    n1=IntVar()
    n2=IntVar()
    numero1=Entry(ventana,textvariable=n1,width=5,justify="right")
    numero1.pack(side="top",anchor="center")

    numero2=Entry(ventana,textvariable=n2,width=5,justify="right")
    numero2.pack(side="top",anchor="center")

    btn_suma=Button(ventana,text="+",command=lambda: funciones.resultado("suma",n1.get(),n2.get()))
    btn_suma.pack()

    btn_resta=Button(ventana,text="-",command=lambda:funciones.resultado("resta",n1.get(),n2.get()))
    btn_resta.pack()

    btn_multiplicacion=Button(ventana,text="x",command=lambda:funciones.resultado("multiplicacion",n1.get(),n2.get()))
    btn_multiplicacion.pack()

    btn_division=Button(ventana,text="/",command=lambda:funciones.resultado("division",n1.get(),n2.get()))
    btn_division.pack()

    btn_salir=Button(ventana,text="Salir",command=ventana.quit)
    btn_salir.pack()




    ventana.mainloop()