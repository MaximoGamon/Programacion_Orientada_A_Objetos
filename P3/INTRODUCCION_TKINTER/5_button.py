from cProfile import label
from tkinter import *

# def cambiarTexto():
    #mensajeCambiante.config(text="Soy el texto cambiado")

def ventana_nueva():
    nueva=Toplevel(ventana)
    nueva.title("Login")
    nueva.geometry("600x400")
    label3=Label(nueva,text="Inicio de sesion Exitoso ")
    label3.config(
        bg="green",
        width=20
    )
    label3.pack(pady=10)
    Boton_regresar=Button(nueva,text="Salir",command=nueva.destroy)
    Boton_regresar.pack(pady=10)    


ventana=Tk()
ventana.title("uso de botones")
ventana.geometry("600x400")

frame_principal=Frame(ventana)
frame_principal.config(
    bg="blue",
    width=800,
    height=120,
    border=2,
    relief=GROOVE
)
frame_principal.pack_propagate(False)
frame_principal.pack(pady=20)

label_titulo=Label(frame_principal,text="LOGIN")
label_titulo.config(
    bg="silver",
    width=20,
)

label_titulo.pack(pady=10)


label1=Label(frame_principal,text="Nombre: ",anchor=W)
label1.config(
    bg="silver",
    width=20
)

label1.pack(pady=10)


label2=Label(frame_principal,text="E-mail: ",anchor=W)
label2.config(
    bg="silver",
    width=20
)

label2.pack(pady=10)

#mensajeCambiante=Label(ventana,text="Texto original")
#mensajeCambiante.pack()

boton_cambiar=Button(ventana,text="Iniciar sesion",command=ventana_nueva)
boton_cambiar.pack()

ventana.mainloop()