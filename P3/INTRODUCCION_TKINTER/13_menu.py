from tkinter import *

def mensaje(tipo):
    resultado.config(text=f"{tipo}")
    



ventana=Tk()
ventana.geometry("500x500")
ventana.title("Menu")

menuBar = Menu(ventana)
ventana.config(menu=menuBar)

archivoMenu=Menu(menuBar,tearoff=1)

archivoMenu2=Menu(menuBar,tearoff=1)

menuBar.add_cascade(label="Archivo",menu=archivoMenu)
archivoMenu.add_command(label="Nuevo Archivo",command=lambda: mensaje("Nuevo archivo"))

archivoMenu.add_command(label="Guardar Archivo",command=lambda: mensaje("Guardar Archivo"))

archivoMenu.add_separator()

archivoMenu.add_command(label="Salir",command=ventana.quit)

#Edicion
menuBar.add_cascade(label="Edicion",menu=archivoMenu2)
archivoMenu2.add_command(label="copiar",command=lambda:mensaje("Archivo copiado"))
archivoMenu2.add_command(label="Recortar",command=lambda: mensaje("Archivo Recortado"))

archivoMenu2.add_separator()

archivoMenu2.add_command(label="Salir",command=ventana.quit)

resultado=Label(ventana,text="")
resultado.pack()

ventana.mainloop()