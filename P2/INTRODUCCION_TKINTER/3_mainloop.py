from  tkinter import *

ventana=Tk()
ventana.title("Main-loop")
ventana.geometry("800x600")

marco=Frame(ventana)
marco.config(
    bg="#00B9FC",
    bd=10,
    height=400,
    width=600,
    relief=RAISED
)
marco.pack(
    padx=50,
    pady=100
)

ventana.mainloop()