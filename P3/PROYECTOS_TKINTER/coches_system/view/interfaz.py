from tkinter import *
from tkinter import messagebox,ttk
from model import cochesBD
from controller import controlador1
import customtkinter as ctk

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

        if tipo=="Autos":
            insertar=lambda:View.insertar_autos(ventana)
            consultar=lambda:View.consultar_autos(ventana)
            actualizar=lambda:View.buscar_id_auto(ventana,"cambiar")
            eliminar=lambda:View.buscar_id_auto(ventana,"borrar")
        elif tipo=="Camionetas":
            insertar=lambda:View.insertar_camionetas(ventana)
            consultar=lambda:View.consultar_camionetas(ventana)
            actualizar=lambda:View.buscar_id_camionetas(ventana,"actualizar")
            eliminar=lambda:View.buscar_id_camionetas(ventana,"eliminar")
        elif tipo=="Camiones":
            insertar=lambda:View.insertar_camiones(ventana)
            consultar=lambda:View.consultar_camiones(ventana)
            actualizar=lambda:View.buscar_id_camiones(ventana,"actualizar")
            eliminar=lambda:View.buscar_id_camiones(ventana,"eliminar")

        lbl_opciones=Label(ventana,text="Elije una opcion: ")
        lbl_opciones.pack(pady=10)

        btn_insertar=Button(ventana,text="1.- Insertar",width=12,command=insertar)
        btn_insertar.pack(pady=10)

        btn_consultar=Button(ventana,text="2.- Consultar",width=12,command=consultar)
        btn_consultar.pack(pady=10)

        btn_actualizar=Button(ventana,text="3.- Actualizar",width=12,command=actualizar)
        btn_actualizar.pack(pady=10)

        btn_eliminar=Button(ventana,text="4.- Eliminar",width=12,command=eliminar)
        btn_eliminar.pack(pady=10)

        btn_salir=Button(ventana,text="5.- Regresar",width=12,command=lambda:View.menu_principal(ventana))
        btn_salir.pack(pady=10)
    
    @staticmethod
    def insertar_autos(ventana):
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

        btn_salir=Button(ventana,text=" Regresar",width=10,command=lambda:View.menu_acciones(ventana,"Autos"))
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

        
        btn_salir=Button(ventana,text=" Regresar",width=10,command=lambda:View.menu_acciones(ventana,"Autos"))
        btn_salir.pack(pady=10)

    
    @staticmethod
    def buscar_id_auto(ventana,tipo):
        View.borrar_pantalla(ventana)

        lbl_id=Label(ventana, text="ID de la operacion a buscar: ")
        lbl_id.pack(pady=5)

        id = IntVar()
        txt_id=Entry(ventana,textvariable=id,justify="right",width=5)
        txt_id.focus()
        txt_id.pack(pady=10)

        btn_salir=Button(ventana,text=" Regresar",width=10,command=lambda:View.menu_acciones(ventana,"Autos"))
        btn_salir.pack(pady=10)

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
            Button(ventana,text=" Regresar",width=10,command=lambda:View.menu_acciones(ventana,"Autos")).pack(pady=5)


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
            Button(ventana,text=" Regresar",width=10,command=lambda:View.menu_acciones(ventana,"Autos")).pack(pady=5)

    #Camionetas
    @staticmethod
    def insertar_camionetas(ventana):
        View.borrar_pantalla(ventana)
        scrollbar = ctk.CTkScrollableFrame(ventana, fg_color="transparent")
        scrollbar.pack(fill=BOTH,expand=True)

        Label(scrollbar,text=".:: Datos del vehiculo ::.\n",justify=CENTER).pack(pady=10)

        lbl_marca=Label(scrollbar,text="Marca:",justify=CENTER)
        lbl_marca.pack(pady=10)
        marca=StringVar()
        txt_marca=Entry(scrollbar,textvariable=marca,justify=RIGHT)
        txt_marca.focus()
        txt_marca.pack(pady=5)

        lbl_color=Label(scrollbar,text="Color:",justify=CENTER)
        lbl_color.pack(pady=10)
        color=StringVar()
        txt_color=Entry(scrollbar,textvariable=color,justify=RIGHT)
        txt_color.pack(pady=5)

        lbl_modelo=Label(scrollbar,text="Modelo:",justify=CENTER)
        lbl_modelo.pack(pady=10)
        modelo=StringVar()
        txt_modelo=Entry(scrollbar,textvariable=modelo,justify=RIGHT)
        txt_modelo.pack(pady=5)

        lbl_velocidad=Label(scrollbar,text="Velocidad:",justify=CENTER)
        lbl_velocidad.pack(pady=10)
        velocidad=StringVar()
        txt_velocidad=Entry(scrollbar,textvariable=velocidad,justify=RIGHT)
        txt_velocidad.pack(pady=5)

        lbl_caballaje=Label(scrollbar,text="Caballaje:",justify=CENTER)
        lbl_caballaje.pack(pady=10)
        caballaje=StringVar()
        txt_caballaje=Entry(scrollbar,textvariable=caballaje,justify=RIGHT)
        txt_caballaje.pack(pady=5)

        lbl_plazas=Label(scrollbar,text="Plazas:",justify=CENTER)
        lbl_plazas.pack(pady=10)
        plazas=StringVar()
        txt_plazas=Entry(scrollbar,textvariable=plazas,justify=RIGHT)
        txt_plazas.pack(pady=5)

        lbl_traccion=Label(scrollbar,text="Traccion:",justify=CENTER)
        lbl_traccion.pack(pady=10)
        traccion=StringVar()
        txt_traccion=Entry(scrollbar,textvariable=traccion,justify=RIGHT)
        txt_traccion.pack(pady=5)

        lbl_cerrada=Label(scrollbar,text="¿Cerrada?:",justify=CENTER)
        lbl_cerrada.pack(pady=10)
        cerrada=StringVar()
        txt_cerrada=Entry(scrollbar,textvariable=cerrada,justify=RIGHT)
        txt_cerrada.pack(pady=5)
        
        btn_guardar=Button(scrollbar,text="Guardar",command=lambda:"",justify=CENTER)
        btn_guardar.pack(pady=5)
        btn_volver=Button(scrollbar,text="Volver",command=lambda:View.menu_acciones(ventana,"Camionetas"),justify=CENTER)
        btn_volver.pack(pady=5)

    @staticmethod
    def consultar_camionetas(ventana):
        View.borrar_pantalla(ventana)
        Label(ventana,text=".:: Consulta de Camionetas ::.\n",justify=CENTER).pack(pady=10)
        registros=[
            ["1","1","1","1","1","1","1","1","1"],
            ["2","2","2","2","2","2","2","2","2"]
        ]
        if len(registros)>0:
            columnas=("ID","Marca","Color","Modelo","Velocidad","Potencia","Plazas","Traccion","Cerrada")
            tree_frame = ctk.CTkFrame(ventana, fg_color="transparent")
            tree_frame.pack(fill=BOTH, expand=True, padx=10, pady=(0, 10))
            camionetas_tree=ttk.Treeview(tree_frame, columns=columnas, show="headings", height=10)
            
            scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=camionetas_tree.yview)
            scrollbarx= ttk.Scrollbar(tree_frame, orient=HORIZONTAL, command=camionetas_tree.xview)
            camionetas_tree.configure(yscroll=scrollbar.set,xscroll=scrollbarx.set)
            scrollbar.pack(side="right", fill="y")
            scrollbarx.pack(side=BOTTOM, fill="x")
            camionetas_tree.pack(side="left", fill=BOTH, expand=True)

            style = ttk.Style()
            style.theme_use("default")
            style.configure("Treeview", background="#F0F0F0", foreground="black", rowheight=18, fieldbackground="#F0F0F0")
            style.configure("Treeview.Heading", background="#D1D5DB", foreground="black", font=("Arial", 12, "bold"))

            for col in columnas:
                camionetas_tree.heading(col, text=col)
                camionetas_tree.column(col, width=120, anchor="center")

            for item in registros:
                fila = (item[0], item[1], item[2], item[3], item[4], item[5], item[6],item[7],item[8])
                camionetas_tree.insert("", END, values=fila)
        else:
            ctk.CTkLabel(ventana, text="No hay datos para mostrar", font=ctk.CTkFont(size=16)).pack(pady=20)
        
        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_acciones(ventana,"Camionetas"),justify=CENTER)
        btn_volver.pack(pady=1)
    
    @staticmethod
    def buscar_id_camionetas(ventana,tipo):
        View.borrar_pantalla(ventana)

        lbl_titulo=Label(ventana,text=f".::Buscar una Camioneta::.")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text=f"ID de la camioneta a buscar: ")
        lbl_id.pack(pady=5)

        id=IntVar()
        txt_id=Entry(ventana,textvariable=id,justify=RIGHT,width=5)
        txt_id.focus()
        txt_id.pack(pady=5)

        if tipo=="actualizar":
            Button(ventana,text="Buscar",command=lambda:View.cambiar_camionetas(ventana,id.get())).pack(pady=5)
        elif tipo=="eliminar":
            Button(ventana,text="Buscar",command=lambda:View.eliminar_camionetas(ventana,id.get())).pack(pady=5)
        Button(ventana,text="Volver",command=lambda:View.menu_acciones(ventana,"Camionetas")).pack(pady=5)
    @staticmethod
    def cambiar_camionetas(ventana,id_):
        registro=[
            ["1","1","1","1","1","1","1","1","1"],
            ["2","2","2","2","2","2","2","2","2"]
        ]
        if registro is None:
            messagebox.showinfo(icon="info",message="No existen esta camioneta en la BD ...")
        else:
            View.borrar_pantalla(ventana)
            
            scrollbar = ctk.CTkScrollableFrame(ventana, fg_color="transparent")
            scrollbar.pack(fill=BOTH,expand=True)

            lbl_titulo=Label(scrollbar,text=f".::Cambiar una Camioneta::.")
            lbl_titulo.pack(pady=10)

            id=IntVar()
            txt_id=Entry(scrollbar,textvariable=id,justify=RIGHT,width=5,state="readonly")
            id.set(registro[1][0])
            txt_id.focus()
            txt_id.pack(pady=5)

            Label(scrollbar,text="Marca: ").pack(pady=5)
            marca=StringVar()
            txt_marca=Entry(scrollbar,textvariable=marca,justify=RIGHT)
            marca.set("Pendiente")
            txt_marca.pack(pady=5)

            Label(scrollbar,text="Color: ").pack(pady=5)
            color=StringVar()
            lbl_color=Entry(scrollbar,textvariable=color,justify=RIGHT)
            color.set("Pendiente")
            lbl_color.pack(pady=5)
            
            Label(scrollbar,text="Modelo: ").pack(pady=5)
            modelo=StringVar()
            lbl_modelo=Entry(scrollbar,textvariable=modelo,justify=RIGHT)
            modelo.set("Pendiente")
            lbl_modelo.pack(pady=5)

            Label(scrollbar,text="Velocidad: ").pack(pady=5)
            velocidad=StringVar()
            lbl_velocidad=Entry(scrollbar,textvariable=velocidad,justify=RIGHT)
            velocidad.set("Pendiente")
            lbl_velocidad.pack(pady=5)

            Label(scrollbar,text="Potencia: ").pack(pady=5)
            potencia=StringVar()
            lbl_potencia=Entry(scrollbar,textvariable=potencia,justify=RIGHT)
            potencia.set("Pendiente")
            lbl_potencia.pack(pady=5)

            Label(scrollbar,text="Plazas: ").pack(pady=5)
            plazas=StringVar()
            lbl_plazas=Entry(scrollbar,textvariable=plazas,justify=RIGHT)
            plazas.set("Pendiente")
            lbl_plazas.pack(pady=5)

            Label(scrollbar,text="Traccion: ").pack(pady=5)
            traccion=StringVar()
            lbl_traccion=Entry(scrollbar,textvariable=traccion,justify=RIGHT)
            traccion.set("Pendiente")
            lbl_traccion.pack(pady=5)

            Label(scrollbar,text="Cerrada: ").pack(pady=5)
            cerrada=StringVar()
            lbl_cerrada=Entry(scrollbar,textvariable=cerrada,justify=RIGHT)
            cerrada.set("Pendiente")
            lbl_cerrada.pack(pady=5)
                
            Button(scrollbar,text="Guardar",command=lambda:"").pack(pady=5)
            Button(scrollbar,text="Volver",command=lambda:View.menu_acciones(ventana,"Camionetas")).pack(pady=5)

    #Vista de eliminar pantalla
    @staticmethod
    def eliminar_camionetas(ventana,id_):
        registro=[
            ["1","1","1","1","1","1","1"],
            ["2","2","2","2","2","2","2"]
        ]
        if registro is None:
            messagebox.showinfo(icon="info",message="No existen esta camioneta en la BD ...")
        else:
            View.borrar_pantalla(ventana)

            lbl_titulo=Label(ventana,text=".::Borrar una Camioneta::.")
            lbl_titulo.pack(pady=10)
            lbl_id=Label(ventana,text=f"\nID de la Camioneta:\n")
            lbl_id.pack(pady=5)
            
            id=IntVar()
            txt_id=Entry(ventana,textvariable=id,width=5,justify=RIGHT,state="readonly")
            id.set(registro[1][0])
            txt_id.focus()
            txt_id.pack(pady=5)

            btn_eliminar=Button(ventana,text="Eliminar",command=lambda:"")
            btn_eliminar.pack(pady=5)
            btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_acciones(ventana,"Camionetas"))
            btn_volver.pack(pady=5)
    
    #Camionetas
    @staticmethod
    def insertar_camiones(ventana):
        View.borrar_pantalla(ventana)
        scrollbar = ctk.CTkScrollableFrame(ventana, fg_color="transparent")
        scrollbar.pack(fill=BOTH,expand=True)

        Label(scrollbar,text=".:: Datos del vehiculo ::.\n",justify=CENTER).pack(pady=10)

        lbl_marca=Label(scrollbar,text="Marca:",justify=CENTER)
        lbl_marca.pack(pady=10)
        marca=StringVar()
        txt_marca=Entry(scrollbar,textvariable=marca,justify=RIGHT)
        txt_marca.focus()
        txt_marca.pack(pady=5)

        lbl_color=Label(scrollbar,text="Color:",justify=CENTER)
        lbl_color.pack(pady=10)
        color=StringVar()
        txt_color=Entry(scrollbar,textvariable=color,justify=RIGHT)
        txt_color.pack(pady=5)

        lbl_modelo=Label(scrollbar,text="Modelo:",justify=CENTER)
        lbl_modelo.pack(pady=10)
        modelo=StringVar()
        txt_modelo=Entry(scrollbar,textvariable=modelo,justify=RIGHT)
        txt_modelo.pack(pady=5)

        lbl_velocidad=Label(scrollbar,text="Velocidad:",justify=CENTER)
        lbl_velocidad.pack(pady=10)
        velocidad=StringVar()
        txt_velocidad=Entry(scrollbar,textvariable=velocidad,justify=RIGHT)
        txt_velocidad.pack(pady=5)

        lbl_caballaje=Label(scrollbar,text="Caballaje:",justify=CENTER)
        lbl_caballaje.pack(pady=10)
        caballaje=StringVar()
        txt_caballaje=Entry(scrollbar,textvariable=caballaje,justify=RIGHT)
        txt_caballaje.pack(pady=5)

        lbl_plazas=Label(scrollbar,text="Plazas:",justify=CENTER)
        lbl_plazas.pack(pady=10)
        plazas=StringVar()
        txt_plazas=Entry(scrollbar,textvariable=plazas,justify=RIGHT)
        txt_plazas.pack(pady=5)

        lbl_ejes=Label(scrollbar,text="Ejes:",justify=CENTER)
        lbl_ejes.pack(pady=10)
        ejes=StringVar()
        txt_ejes=Entry(scrollbar,textvariable=ejes,justify=RIGHT)
        txt_ejes.pack(pady=5)

        lbl_capacidad=Label(scrollbar,text="Capacidad de Carga:",justify=CENTER)
        lbl_capacidad.pack(pady=10)
        capacidad=StringVar()
        txt_capacidad=Entry(scrollbar,textvariable=capacidad,justify=RIGHT)
        txt_capacidad.pack(pady=5)
        
        btn_guardar=Button(scrollbar,text="Guardar",command=lambda:"",justify=CENTER)
        btn_guardar.pack(pady=5)
        btn_volver=Button(scrollbar,text="Volver",command=lambda:View.menu_acciones(ventana,"Camiones"),justify=CENTER)
        btn_volver.pack(pady=5)

    @staticmethod
    def consultar_camiones(ventana):
        View.borrar_pantalla(ventana)
        Label(ventana,text=".:: Consulta de Camiones ::.\n",justify=CENTER).pack(pady=10)
        registros=[
            ["1","1","1","1","1","1","1","1","1"],
            ["2","2","2","2","2","2","2","2","2"]
        ]
        if len(registros)>0:
            columnas=("ID","Marca","Color","Modelo","Velocidad","Potencia","Plazas","Ejes","Capacidad de Carga")
            tree_frame = ctk.CTkFrame(ventana, fg_color="transparent")
            tree_frame.pack(fill=BOTH, expand=True, padx=10, pady=(0, 10))
            camiones_tree=ttk.Treeview(tree_frame, columns=columnas, show="headings", height=10)
            
            scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=camiones_tree.yview)
            scrollbarx= ttk.Scrollbar(tree_frame, orient=HORIZONTAL, command=camiones_tree.xview)
            camiones_tree.configure(yscroll=scrollbar.set,xscroll=scrollbarx.set)
            scrollbar.pack(side="right", fill="y")
            scrollbarx.pack(side=BOTTOM, fill="x")
            camiones_tree.pack(side="left", fill=BOTH, expand=True)

            style = ttk.Style()
            style.theme_use("default")
            style.configure("Treeview", background="#F0F0F0", foreground="black", rowheight=18, fieldbackground="#F0F0F0")
            style.configure("Treeview.Heading", background="#D1D5DB", foreground="black", font=("Arial", 12, "bold"))

            for col in columnas:
                camiones_tree.heading(col, text=col)
                camiones_tree.column(col, width=120, anchor="center")

            for item in registros:
                fila = (item[0], item[1], item[2], item[3], item[4], item[5], item[6],item[7],item[8])
                camiones_tree.insert("", END, values=fila)
        else:
            ctk.CTkLabel(ventana, text="No hay datos para mostrar", font=ctk.CTkFont(size=16)).pack(pady=20)
        
        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_acciones(ventana,"Camiones"),justify=CENTER)
        btn_volver.pack(pady=1)
    
    @staticmethod
    def buscar_id_camiones(ventana,tipo):
        View.borrar_pantalla(ventana)

        lbl_titulo=Label(ventana,text=f".::Buscar un Camion::.")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text=f"ID del camion a buscar: ")
        lbl_id.pack(pady=5)

        id=IntVar()
        txt_id=Entry(ventana,textvariable=id,justify=RIGHT,width=5)
        txt_id.focus()
        txt_id.pack(pady=5)

        if tipo=="actualizar":
            Button(ventana,text="Buscar",command=lambda:View.cambiar_camiones(ventana,id.get())).pack(pady=5)
        elif tipo=="eliminar":
            Button(ventana,text="Buscar",command=lambda:View.eliminar_camiones(ventana,id.get())).pack(pady=5)
        Button(ventana,text="Volver",command=lambda:View.menu_acciones(ventana,"Camiones")).pack(pady=5)

    @staticmethod
    def cambiar_camiones(ventana,id_):
        registro=[
            ["1","1","1","1","1","1","1","1","1"],
            ["2","2","2","2","2","2","2","2","2"]
        ]
        if registro is None:
            messagebox.showinfo(icon="info",message="No existen est camion en la BD ...")
        else:
            View.borrar_pantalla(ventana)

            scrollbar = ctk.CTkScrollableFrame(ventana, fg_color="transparent")
            scrollbar.pack(fill=BOTH,expand=True)

            lbl_titulo=Label(scrollbar,text=f".::Cambiar un Camion::.")
            lbl_titulo.pack(pady=10)

            id=IntVar()
            txt_id=Entry(scrollbar,textvariable=id,justify=RIGHT,width=5,state="readonly")
            id.set(registro[1][0])
            txt_id.focus()
            txt_id.pack(pady=5)

            Label(scrollbar,text="Marca: ").pack(pady=5)
            marca=StringVar()
            txt_marca=Entry(scrollbar,textvariable=marca,justify=RIGHT)
            marca.set("Pendiente")
            txt_marca.pack(pady=5)

            Label(scrollbar,text="Color: ").pack(pady=5)
            color=StringVar()
            lbl_color=Entry(scrollbar,textvariable=color,justify=RIGHT)
            color.set("Pendiente")
            lbl_color.pack(pady=5)
            
            Label(scrollbar,text="Modelo: ").pack(pady=5)
            modelo=StringVar()
            lbl_modelo=Entry(scrollbar,textvariable=modelo,justify=RIGHT)
            modelo.set("Pendiente")
            lbl_modelo.pack(pady=5)

            Label(scrollbar,text="Velocidad: ").pack(pady=5)
            velocidad=StringVar()
            lbl_velocidad=Entry(scrollbar,textvariable=velocidad,justify=RIGHT)
            velocidad.set("Pendiente")
            lbl_velocidad.pack(pady=5)

            Label(scrollbar,text="Potencia: ").pack(pady=5)
            potencia=StringVar()
            lbl_potencia=Entry(scrollbar,textvariable=potencia,justify=RIGHT)
            potencia.set("Pendiente")
            lbl_potencia.pack(pady=5)

            Label(scrollbar,text="Plazas: ").pack(pady=5)
            plazas=StringVar()
            lbl_plazas=Entry(scrollbar,textvariable=plazas,justify=RIGHT)
            plazas.set("Pendiente")
            lbl_plazas.pack(pady=5)

            Label(scrollbar,text="Ejes: ").pack(pady=5)
            traccion=StringVar()
            lbl_traccion=Entry(scrollbar,textvariable=traccion,justify=RIGHT)
            traccion.set("Pendiente")
            lbl_traccion.pack(pady=5)

            Label(scrollbar,text="Capcidad de carga: ").pack(pady=5)
            cerrada=StringVar()
            lbl_cerrada=Entry(scrollbar,textvariable=cerrada,justify=RIGHT)
            cerrada.set("Pendiente")
            lbl_cerrada.pack(pady=5)
                
            Button(scrollbar,text="Guardar",command=lambda:"").pack(pady=5)
            Button(scrollbar,text="Volver",command=lambda:View.menu_acciones(ventana,"Camiones")).pack(pady=5)

    #Vista de eliminar pantalla
    @staticmethod
    def eliminar_camiones(ventana,id_):
        registro=[
            ["1","1","1","1","1","1","1"],
            ["2","2","2","2","2","2","2"]
        ]
        if registro is None:
            messagebox.showinfo(icon="info",message="No existen este camion en la BD ...")
        else:
            View.borrar_pantalla(ventana)

            lbl_titulo=Label(ventana,text=".::Borrar un Camion::.")
            lbl_titulo.pack(pady=10)
            lbl_id=Label(ventana,text=f"\nID del Camion:\n")
            lbl_id.pack(pady=5)
            
            id=IntVar()
            txt_id=Entry(ventana,textvariable=id,width=5,justify=RIGHT,state="readonly")
            id.set(registro[1][0])
            txt_id.focus()
            txt_id.pack(pady=5)

            btn_eliminar=Button(ventana,text="Eliminar",command=lambda:"")
            btn_eliminar.pack(pady=5)
            btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_acciones(ventana,"Camiones"))
            btn_volver.pack(pady=5)

        







        





