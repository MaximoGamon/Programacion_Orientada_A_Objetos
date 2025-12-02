from tkinter import *

def Entrar():
    lbl_titulo.config(
        text="POO con Python",
        bg="green",
        fg="red",
        width=50,
        height=4,
        font=("Arial",30,"bold"),
        border=2,
        relief=GROOVE
    )

def Borrar():
    lbl_titulo.config(
        text="Bienvenido a Tkinter",
        bg="lightblue",
        fg="darkblue",
        width=50,
        height=4,
        font=("Helvetica",30,"italic"),
        border=2,
        relief= GROOVE
    )

ventana=Tk()
ventana.title("Entry")
ventana.geometry("500x500")

lbl_titulo=Label(ventana,text="Bienvenido a Tkinter")
lbl_titulo.config(
    bg="lightblue",
    fg="darkblue",
    width=50,
    height=4,
    font=("Helvetica",30,"italic"),
    relief=GROOVE
)

lbl_titulo.pack(pady=50)

lbl_nombre=Entry(ventana,text="Ingrese el nombre ")
lbl_nombre.pack(pady=5)



txt_nombre=Entry(ventana)
txt_nombre.pack()

lbl_password=Entry(ventana,text="Ingrese la contraseña")
lbl_password.pack(pady=5)

txt_paswword=Entry(ventana,show="*")
txt_paswword.pack()

btn_entrar=Button(ventana,text="Entrar",command=Entrar)
btn_entrar.pack(pady=5)


btn_borrar=Button(ventana,text="Borrar",command=Borrar)
btn_borrar.config(
    fg="black",
    activeforeground="red",
    width=15,
    font=("Arial",20,"bold")
)

btn_borrar.pack(pady=5)

lbl_resultado=Label(ventana,text="")
lbl_resultado.pack(pady=5)

ventana.mainloop()
