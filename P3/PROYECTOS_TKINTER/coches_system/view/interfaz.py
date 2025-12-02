from tkinter import *
from tkinter import messagebox
from model import cochesBD
from controller import controlador1


class View:
    def __init__(self,ventana):
        self.ventana=ventana
        ventana.title("Notas System")
        ventana.geometry("700x500")
        self.menu_principal(ventana)

    @staticmethod  
    def borrar_pantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def menu_principal(ventana):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=" .:: Menu principal ::.",justify="center")
        lbl_titulo.pack(pady=5)

        lbl_opciones=Label(ventana,text="Elije una opcion: ")
        lbl_opciones.pack(pady=10)

        btn_autos=Button(ventana,text="1.- Autos",width=12,command=lambda:View.menu_acciones(ventana,"Autos"))
        btn_autos.pack(pady=10)

        btn_camionetas=Button(ventana,text="2.- Camionetas",width=12,command=lambda:View.menu_acciones(ventana,"Camionetas"))
        btn_camionetas.pack(pady=10)

        btn_camiones=Button(ventana,text="3.- Camiones",width=12,command=lambda:View.menu_acciones(ventana,"Camiones"))
        btn_camiones.pack(pady=10)

        btn_salir=Button(ventana,text="4.- Salir",width=12,command=ventana.quit)
        btn_salir.pack(pady=10)

    @staticmethod
    def menu_acciones(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=f" .:: Menu de {tipo} ::.",justify="center")
        lbl_titulo.pack(pady=5)

        lbl_opciones=Label(ventana,text="Elije una opcion: ")
        lbl_opciones.pack(pady=10)

        btn_insertar=Button(ventana,text="1.- Insertar",width=12,command=lambda:View.insertar_interfaz(ventana))
        btn_insertar.pack(pady=10)

        btn_consultar=Button(ventana,text="2.- Consultar",width=12,command=lambda:View.consultar_autos(ventana))
        btn_consultar.pack(pady=10)

        btn_actualizar=Button(ventana,text="3.- Actualizar",width=12,command=lambda:View.buscar_id(ventana,"cambiar"))
        btn_actualizar.pack(pady=10)

        btn_eliminar=Button(ventana,text="4.- Eliminar",width=12,command=lambda:View.buscar_id(ventana,"borrar"))
        btn_eliminar.pack(pady=10)

        btn_salir=Button(ventana,text="5.- Regresar",width=12,command=lambda:View.menu_principal(ventana))
        btn_salir.pack(pady=10)
    
    @staticmethod
    def insertar_interfaz(ventana):
        View.borrar_pantalla(ventana)

        lbl_titulo=Label(ventana,text=f" Ingresa los datos del vehiculo: ",justify="center")
        lbl_titulo.pack(pady=5)

        #Marca
        lbl_marca=Label(ventana,text=f" Ingrese la Marca: ",justify="center")
        lbl_marca.pack(pady=5)

        marca=StringVar()
        txt_marca=Entry(ventana,textvariable=marca)
        txt_marca.focus()
        txt_marca.pack(pady=10)

        #color
        lbl_color=Label(ventana,text=f" Ingrese el color: ",justify="center")
        lbl_color.pack(pady=5)

        color=StringVar()
        txt_color=Entry(ventana,textvariable=color)
        txt_color.pack(pady=10)

        #modelo
        lbl_modelo=Label(ventana,text=f" Ingrese el modelo: ",justify="center")
        lbl_modelo.pack(pady=5)

        modelo=StringVar()
        txt_modelo=Entry(ventana,textvariable=modelo)
        txt_modelo.pack(pady=10)

        #velocidad
        lbl_velocidad=Label(ventana,text=f" Ingrese la velocidad: ",justify="center")
        lbl_velocidad.pack(pady=5)

        velocidad=DoubleVar()
        txt_velocidad=Entry(ventana,textvariable=velocidad)
        txt_velocidad.pack(pady=10)

        #potencia
        lbl_potencia=Label(ventana,text=f" Ingrese la potencia: ",justify="center")
        lbl_potencia.pack(pady=5)

        potencia=DoubleVar()
        txt_potencia=Entry(ventana,textvariable=potencia)
        txt_potencia.pack(pady=10)

        #plazas
        lbl_plazas=Label(ventana,text=f" Ingrese el No. de plazas: ",justify="center")
        lbl_plazas.pack(pady=5)

        plazas=IntVar()
        txt_plazas=Entry(ventana,textvariable=plazas)
        txt_plazas.pack(pady=10)

        btn_salir=Button(ventana,text="5.- Regresar",width=12,command=lambda:View.menu_principal(ventana))
        btn_salir.pack(pady=10)

    @staticmethod
    def consultar_autos(ventana):
        View.borrar_pantalla(ventana)

        registros=cochesBD.Autos.consultar()
        if len(registros)>0:
            num_autos=1
            for fila in registros:
                lbl_reg=Label(ventana,text=f"Auto # {num_autos} con ID: {fila[0]}\n Marca {fila[1]} \n Color {fila[2]} \n Modelo {fila[3]} \n Velocidad {fila[3]}"
                f"\n Potencia {fila[4]} \n Plazas {fila[6]} ")
                lbl_reg.pack()
                num_autos+=1
        else:
            messagebox.showinfo(icon="info",message="No existen registros en la BD")

        
        btn_salir=Button(ventana,text="5.- Regresar",width=12,command=lambda:View.menu_principal(ventana))
        btn_salir.pack(pady=10)

    
    @staticmethod
    def buscar_id(ventana,tipo):
        View.borrar_pantalla(ventana)

        lbl_id=Label(ventana, text="ID de la operacion a buscar: ")
        lbl_id.pack(pady=5)

        id = IntVar()
        txt_id=Entry(ventana,textvariable=id,justify="right",width=5)
        txt_id.focus()
        txt_id.pack(pady=10)

        if tipo == "cambiar":
            Button(ventana,text="Buscar",command=lambda:View.cambiar_id(ventana,id.get())).pack(pady=5)
        elif tipo == "borrar":
             Button(ventana,text="Buscar",command=lambda:View.eliminar_id(ventana,id.get())).pack(pady=5)

    @staticmethod
    def cambiar_id(ventana,id_):
        registro=controlador1.funciones.consultar_id(id_)
        if registro is None:
            messagebox.showinfo(icon="info",message="No existen registros en la BD")
        else:
            View.borrar_pantalla(ventana)
            lbl_titulo=Label(ventana,text=f" .:: Cambiar un auto ::.")
            lbl_titulo.pack(pady=5)

            id=IntVar()
            txt_id=Entry(ventana,textvariable=id,justify="right",width=5,state="readonly")
            id.set(id_)
            txt_id.focus()
            txt_id.pack(pady=5)

            Label(ventana,text="color").pack(pady=5)
            color=StringVar()
            txt_color=Entry(ventana,textvariable=color,width=8)
            color.set(registro[1])
            txt_color.pack(pady=5)

            Label(ventana,text="marca").pack(pady=5)
            marca=StringVar()
            txt_marca=Entry(ventana,textvariable=marca,width=8)
            marca.set(registro[2])
            txt_marca.pack(pady=5)

            Label(ventana,text="modelo ").pack(pady=5)
            modelo=StringVar()
            txt_modelo=Entry(ventana,textvariable=modelo,width=8)
            modelo.set(registro[3])
            txt_modelo.pack(pady=5)

            Label(ventana,text="velocidad").pack(pady=5)
            velocidad=IntVar()
            txt_velocidad=Entry(ventana,textvariable=velocidad,width=8)
            velocidad.set(registro[4])
            txt_velocidad.pack(pady=5)

            Label(ventana,text="potencia").pack(pady=5)
            potencia=IntVar()
            txt_potencia=Entry(ventana,textvariable=potencia,width=8)
            potencia.set(registro[5])
            txt_potencia.pack(pady=5)

            Label(ventana,text="plazas").pack(pady=5)
            plazas=IntVar()
            txt_plazas=Entry(ventana,textvariable=plazas,width=8)
            plazas.set(registro[4])
            txt_plazas.pack(pady=5)

            Button(ventana,text="Guardar",command="").pack(pady=5)
            Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana)).pack(pady=5)


    @staticmethod
    def eliminar_id(ventana,id_):
        registro=controlador1.funciones.consultar_id(id_)
        if registro is None:
            messagebox.showinfo(icon="info",message="No existe esta operacion en la BD")
        else:
            View.borrar_pantalla(ventana)

            lbl_titulo=Label(ventana,text=f".:: Borrar una operación ::.")
            lbl_titulo.pack(pady=5)

            lbl_id=Label(ventana,text="ID de la operación:")
            lbl_id.pack(pady=5)

            id=IntVar()
            txt_id=Entry(ventana,textvariable=id,justify="right",width=5,state="readonly")
            id.set(id_)
            txt_id.focus()
            txt_id.pack(pady=5)

            btn_eliminar=Button(ventana,text="Eliminar",command="")
            btn_eliminar.pack(pady=5)
            Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana)).pack(pady=5)

    

        







        





