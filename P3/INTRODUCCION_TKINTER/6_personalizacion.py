from tkinter import *

def hazclikc():
    lbl_titulo.config(
        text="POO con python",
        bg="green",
        fg="red",
        width=50,
        height=4,
        font=("Arial",30,"bold"),
        border=2,
        relief=GROOVE
    )

def regresarclick():
    lbl_titulo.config(
        text="Bienvenidos a Tkinter",
        bg="lightblue",
        fg="darkblue",
        width=50,
        height=4,
        font=("Helvetica",30,"italic"),
        border=2,
        relief=GROOVE  
        )

ventana=Tk()
ventana.title("Personalizacion de widgets u objetos")
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

btn_hazclick=Button(ventana,text="haz click aqui",command=hazclikc)
btn_hazclick.config(
    fg="grey",
    activebackground="blue",
    width=15,
    font=("Arial",20,"bold")
)
btn_hazclick.pack(pady=5)

btn_regresar=Button(ventana,text="Regresar click aqui",command=regresarclick)
btn_regresar.config(
    fg="black",
    activeforeground="red",
    width=15,
    font=("Arial",20,"bold")
)
btn_regresar.pack(pady=5)

ventana.mainloop()