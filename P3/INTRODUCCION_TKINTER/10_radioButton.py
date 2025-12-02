from tkinter import *

def mostrarSeleccion():
    resultado.config(text=f"Opción seleccionada: {opcion.get()}")

ventana = Tk()
ventana.title("Radio Button")
ventana.geometry("500x500")

opcion = StringVar()

opcion1 = Radiobutton(ventana,text="Opción 1",variable=opcion,value="Opcion1")
opcion1.pack()

opcion2 = Radiobutton(ventana,text="Opción 2",variable=opcion,value="Opcion2")
opcion2.pack()

opcion3 = Radiobutton(ventana,text="Opción 3",variable=opcion,value="Opcion3")
opcion3.pack()


boton = Button(ventana , text="Mostrar selección" , command=mostrarSeleccion)
boton.pack()

resultado = Label(ventana , text="")
resultado.pack()

ventana.mainloop()