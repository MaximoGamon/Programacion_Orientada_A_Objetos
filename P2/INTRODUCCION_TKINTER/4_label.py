from tkinter import *

ventana=Tk()
ventana.geometry("800x600")
ventana.title("Etiquetas")

#Etiquetas o label

etiqueta1=Label(ventana,text="Nombre de la persona").pack()

marco1=Frame(ventana,bg="#0EC37A",width=300,height=100)
marco1.pack_propagate(False)
marco1.pack()

etiqueta2=Label(marco1,text="Soy una etiqueta dentro de un marco",bg="#0EC37A").pack()


ventana.mainloop()