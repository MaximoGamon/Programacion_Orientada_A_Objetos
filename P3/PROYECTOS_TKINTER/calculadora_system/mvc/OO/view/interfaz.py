from tkinter import *
from tkinter import messagebox
from model import operaciones
from controller import funciones


#Interfaz VIEW
class vista:
    def __init__(self,ventana):
        ventana.title("Calculadora")
        ventana.geometry("500x500")
        #ventana.resizable(False,False)
        vista.interfaz_principal(ventana)
        
    @staticmethod
    def interfaz_principal(ventana):   
        vista.borrarPantalla(ventana) 
        vista.menuPrincipal(ventana)
        n1=IntVar()
        n2=IntVar()
        numero1=Entry(ventana,textvariable=n1,width=5,justify="right")
        numero1.focus()
        numero1.pack(side="top",anchor="center")

        numero2=Entry(ventana,textvariable=n2,width=5,justify="right")
        numero2.pack(side="top",anchor="center")

        btn_suma=Button(ventana,text="+",command=lambda: funciones.Funciones.resultado("suma",n1.get(),n2.get()))
        btn_suma.pack()

        btn_resta=Button(ventana,text="-",command=lambda:funciones.Funciones.resultado("resta",n1.get(),n2.get()))
        btn_resta.pack()

        btn_multiplicacion=Button(ventana,text="x",command=lambda:funciones.Funciones.resultado("multiplicacion",n1.get(),n2.get()))
        btn_multiplicacion.pack()

        btn_division=Button(ventana,text="/",command=lambda:funciones.Funciones.resultado("division",n1.get(),n2.get()))
        btn_division.pack()

        btn_salir=Button(ventana,text="Salir",command=ventana.quit)
        btn_salir.pack()

    #Borrar pantalla
    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()


    @staticmethod
    def menuPrincipal(ventana):
        menuBar = Menu(ventana)
        ventana.config(menu=menuBar)

        operacionesMenu=Menu(menuBar,tearoff=False)
        menuBar.add_cascade(label="Operaciones",menu=operacionesMenu)
        operacionesMenu.add_command(label="Agregar",command=lambda: vista.interfaz_principal(ventana))
        operacionesMenu.add_command(label="consultar",command=lambda: vista.consultar(ventana))
        operacionesMenu.add_command(label="cambiar",command=lambda: vista.buscar_id(ventana,"cambiar"))
        operacionesMenu.add_command(label="borrar",command=lambda:vista.buscar_id(ventana,"borrar"))
        operacionesMenu.add_separator()

        operacionesMenu.add_command(label="Salir",command=ventana.quit)

    


    #Consultar  
    @staticmethod
    def consultar(ventana):
        vista.borrarPantalla(ventana)
        vista.menuPrincipal(ventana)
        label1=Label(ventana,text=".:: Listado de Operaciones ::.")
        label1.pack()

        
        oper=operaciones.Operaciones.consultar()
        if len(oper)>0:
            con=1
            for i in oper:
                label2=Label(ventana,text=f"\n Operacio: {con} ID: {i[0]} Fecha de creacion: {i[1]} \n Operacion: {i[2]}{i[4]}{i[3]} = {i[5]}")
                label2.pack()
                con+=1
        
        else:
            messagebox.showinfo(icon="info",message="No existen operaciones guardadas en la base de datos")

        btn_volver = Button(ventana,text="Volver",command=lambda:vista.interfaz_principal(ventana))
        btn_volver.pack(pady=5)



    @staticmethod
    def cambiar(ventana):
        vista.borrarPantalla(ventana)
        vista.menuPrincipal(ventana)

        label1=Label(ventana,text=".:: Cambiar una Operación ::.")
        label1.pack(pady=10)

        label2=Label(ventana,text="ID de la operación")
        label2.pack(pady=5)

        id=IntVar()
        # otra forma de hacerlo: new_n1=Entry(ventana)
        

        txt_id=Entry(ventana,textvariable=id,justify="right",width=5)
        txt_id.focus()
        txt_id.pack(pady=10)

        btn_buscar=Button(ventana,text="Buscar",command=lambda:vista.buscar(ventana,txt_id.get()))
        btn_buscar.pack(pady=10)

    @staticmethod
    def buscar_id(ventana,tipo):
        vista.borrarPantalla(ventana)
        vista.menuPrincipal(ventana)

        lbl_titulo=Label(ventana,text=f".:: Buscar una operación ::.")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana, text="ID de la operacion a buscar: ")
        lbl_id.pack(pady=5)

        id = IntVar()
        txt_id=Entry(ventana,textvariable=id,justify="right",width=5)
        txt_id.focus()
        txt_id.pack(pady=10)

        if tipo == "cambiar":
            Button(ventana,text="Buscar",command=lambda:vista.cambiar_id(ventana,id.get())).pack(pady=5)
        elif tipo == "borrar":
             Button(ventana,text="Buscar",command=lambda:vista.eliminar_id(ventana,id.get())).pack(pady=5)


    @staticmethod
    def cambiar_id(ventana,id_):
        registro=funciones.Funciones.consultar_id(id_)
        if registro is None:
            messagebox.showinfo(icon="info",message="No existen operaciones en la BD")
        else:
            vista.borrarPantalla(ventana)
            vista.menuPrincipal(ventana) 

            lbl_titulo=Label(ventana,text=f" .:: Cambiar una operación ::.")
            lbl_titulo.pack(pady=5)

            id=IntVar()
            txt_id=Entry(ventana,textvariable=id,justify="right",width=5,state="readonly")
            id.set(id_)
            txt_id.focus()
            txt_id.pack(pady=5)

            Label(ventana,text="Numero 1").pack(pady=5)
            n1=IntVar()
            numero1=Entry(ventana,textvariable=n1,justify="right",width=5)
            n1.set(registro[2])
            numero1.pack(pady=5)

            Label(ventana,text="Numero 2").pack(pady=5)
            n2=IntVar()
            numero2=Entry(ventana,textvariable=n2,justify="right",width=5)
            n2.set(registro[3])
            numero2.pack(pady=5)

            Label(ventana,text="Signo ").pack(pady=5)
            sig=StringVar()
            signo=Entry(ventana,textvariable=sig,justify="center",width=5)
            sig.set(registro[4])
            signo.pack(pady=5)

            Label(ventana,text="Resultado").pack(pady=5)
            resul=DoubleVar()
            resultado=Entry(ventana,textvariable=resul,justify="right",width=5)
            resul.set(registro[5])
            resultado.pack(pady=5)

            Button(ventana,text="Guardar",command=lambda:operaciones.Operaciones.actualizar(n1.get(),n2.get(),signo.get(),resultado.get(),id_)).pack(pady=5)
            Button(ventana,text="Volver",command=lambda:vista.interfaz_principal(ventana)).pack(pady=5)


    @staticmethod
    def eliminar_id(ventana,id_):
        registro=funciones.Funciones.consultar_id(id_)
        if registro is None:
            messagebox.showinfo(icon="info",message="No existe esta operacion en la BD")
        else:
            vista.borrarPantalla(ventana)
            vista.menuPrincipal(ventana)

            lbl_titulo=Label(ventana,text=f".:: Borrar una operación ::.")
            lbl_titulo.pack(pady=5)

            lbl_id=Label(ventana,text="ID de la operación:")
            lbl_id.pack(pady=5)

            id=IntVar()
            txt_id=Entry(ventana,textvariable=id,justify="right",width=5,state="readonly")
            id.set(id_)
            txt_id.focus()
            txt_id.pack(pady=5)

            btn_eliminar=Button(ventana,text="Eliminar",command=lambda:operaciones.Operaciones.eliminar(id_))
            btn_eliminar.pack(pady=5)
            Button(ventana,text="Volver",command=lambda:vista.interfaz_principal(ventana)).pack(pady=5)



    @staticmethod
    def cambiar2(ventana): 

        new_n1=IntVar()
        new_n2=IntVar()
        new_signo=StringVar()
        new_result=DoubleVar()

        label3=Label(ventana,text="Nuevo Numero 1")
        label3.pack(pady=10)

        txt_n1=Entry(ventana,textvariable=new_n1,justify="right",width=5)
        txt_n1.pack(pady=10)

        label4=Label(ventana,text="Nuevo Numero 2")
        label4.pack(pady=10)


        txt_n2=Entry(ventana,textvariable=new_n2,justify="right",width=5)
        txt_n2.pack(pady=10)

        label5=Label(ventana,text="Nuevo Signo")
        label5.pack()

        txt_signo=Entry(ventana,textvariable=new_signo,justify="center")
        txt_signo.pack(pady=10)

        label6=Label(ventana,text="Nuevo Resultado")
        label6.pack(pady=10)


        txt_result=Entry(ventana,textvariable=new_result)
        txt_result.pack()

        btn_guardar= Button(ventana,text="Guardar",command=lambda: operaciones.Operaciones.actualizar(new_n1.get(),new_n2.get(),new_signo.get(),new_result.get(),id.get()))
        btn_guardar.pack(pady=5)

        btn_volver = Button(ventana,text="Volver",command=lambda:vista.interfaz_principal(ventana))
        btn_volver.pack(pady=5)




    #Vista de eliminar operaciones
    @staticmethod
    def eliminar(ventana):
        vista.borrarPantalla(ventana)
        vista.menuPrincipal(ventana)
        Labe1=Label(ventana,text=".:: Borrar una operacion ::.",anchor="center")
        Labe1.pack()

        label2=Label(ventana,text="ID de la operacion:",anchor="center")
        label2.pack(pady=10)

        id=IntVar()
        label3 = Entry(ventana,textvariable=id)
        label3.focus()
        label3.pack(pady=5)

        btn_eliminar = Button(ventana,text="Eliminar",command=lambda:operaciones.Operaciones.eliminar(id.get()))
        btn_eliminar.pack(pady=5)

        
        btn_volver = Button(ventana,text="Volver",command=lambda:vista.interfaz_principal(ventana))
        btn_volver.pack(pady=5)

        

       

        