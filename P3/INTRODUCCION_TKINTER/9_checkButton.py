from tkinter import *


def mostrarEstado():
    if opcion.get() == 1:
        resultado.config(text=f"Notificaciones activadas...")
    else:
        resultado.config(text=f"Notificaciones desactivadas...")




ventana=Tk()
ventana.title("checkButton")
ventana.geometry("500x500")

opcion=IntVar()
checkBoton=Checkbutton(ventana,text="¿Deseas recibir notificaciones?",variable=opcion,
                       onvalue=1,
                       offvalue=0,
                       )
checkBoton.pack()



button_confirmar=Button(ventana,text="confirmar",command=mostrarEstado)
button_confirmar.pack(pady=5)


resultado=Label(ventana,text="")
resultado.pack()



ventana.mainloop()