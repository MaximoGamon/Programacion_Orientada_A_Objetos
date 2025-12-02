from tkinter import *

ventana=Tk()
ventana.geometry("500x500")
ventana.title("listBox")

def seleccion ():
    valor=lista.get(lista.curselection())
    resultado.config(text=f"Seleccionaste: {valor}")



lista = Listbox(ventana,width=50,height=5,selectmode="single")
lista.pack()

opciones = ["azul","rojo","negro","amarillo"]
for i in opciones:
    lista.insert(END,i)

boton = Button(ventana,text="Mostrar seleccion del usuario",command=seleccion)
boton.pack()

resultado = Label(ventana,text="")
resultado.pack()

ventana.mainloop()