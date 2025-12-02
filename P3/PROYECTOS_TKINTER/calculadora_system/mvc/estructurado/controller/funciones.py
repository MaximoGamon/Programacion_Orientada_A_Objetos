from tkinter import messagebox

#Control App o controller
def resultado(tipo,numero1,numero2):
    if tipo == "suma":
        ope=numero1+numero2
        signo="+"
        
    elif tipo == "resta":
        ope=numero1-numero2
        signo="-"
        
    elif tipo == "multiplicacion":
        ope=numero1*numero2
        signo="*"
       
    elif tipo == "division":
        ope=numero1/numero2
        signo="/"
        
    messagebox.showinfo(title=f"{tipo}",message=f"{numero1} {signo} {numero2} = {ope}",icon="info")

