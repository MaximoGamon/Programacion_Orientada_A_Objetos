from tkinter import *
from tkinter import messagebox

"""
Crear una calculadora:
1.- Dos campos de texto
2.- 4 botones para las Operaciones
3.- Mostrar el resultado en una alerta
4.- Porgramado de forma Estructurado
5.- Considerar el MVC
"""

def resultado(tipo,numero1,numero2):
    if tipo == "suma":
        sumar=numero1+numero2
        messagebox.showinfo(title="Suma",message=f"{numero1} + {numero2} = {sumar}",icon="info")
    elif tipo == "resta":
        restar=numero1-numero2
        messagebox.showinfo(title="Resta",message=f"{numero1} - {numero2} = {restar}",icon="info")
    elif tipo == "multiplicacion":
        multiplicar=numero1*numero2
        messagebox.showinfo(title="Multiplicacion",message=f"{numero1} x {numero2} = {multiplicar}",icon="info")
    elif tipo == "division":
        division=numero1/numero2
        messagebox.showinfo(title="Division",message=f"{numero1} / {numero2} = {division}",icon="info")




#Control App o controller
def suma(numero1,numero2):
    resultado("suma",numero1,numero2)

def resta(numero1,numero2):
    resultado("resta",numero1,numero2)

def multiplicacion(numero1,numero2):
    resultado("multiplicacion",numero1,numero2)

def division(numero1,numero2):
    resultado("division",numero1,numero2)


#Interfaz VIEW
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

btn_suma=Button(ventana,text="+",command=lambda:(n1.get(),n2.get()))
btn_suma.pack()

btn_resta=Button(ventana,text="-",command=lambda:resta(n1.get(),n2.get()))
btn_resta.pack()

btn_multiplicacion=Button(ventana,text="x",command=lambda:multiplicacion(n1.get(),n2.get()))
btn_multiplicacion.pack()

btn_division=Button(ventana,text="/",command=lambda:division(n1.get(),n2.get()))
btn_division.pack()

btn_salir=Button(ventana,text="Salir",command=ventana.quit)
btn_salir.pack()




ventana.mainloop()