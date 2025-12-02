from tkinter import *
from tkinter import messagebox
from controller import controlador1

class View:
    def __init__(self,ventana):
        self.ventana=ventana
        ventana.title("Notas System")
        ventana.geometry("800x600")
        self.menu_principal(ventana)

    @staticmethod  
    def borrar_pantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    #@staticmethod  
    # def borrar_pantalla(ventana):
        #for widget in ventana.winfo_children():
            #widget.destroy()
    @staticmethod
    def menu_principal(ventana):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=".:: Menu Principal ::.",justify="center")
        lbl_titulo.pack(pady=10)

        btn_registro=Button(ventana,text="1.- Registro",justify="center",command=lambda:View.registro(ventana))
        btn_registro.pack(pady=15)

        btn_login=Button(ventana,text="2.- Login",justify="center",command=lambda:View.login(ventana))
        btn_login.pack(pady=15)

        btn_salir=Button(ventana,text="3.- Salir",justify="center",command=ventana.quit)
        btn_salir.pack(pady=15)

    @staticmethod
    def registro(ventana):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=".:: Registro ::.",justify="center")
        lbl_titulo.pack(pady=10)

        #Nombre
        lbl_nombre=Label(ventana,text="¿Cual es tu nombre?:",justify="center")
        lbl_nombre.pack(pady=15)

        nombre=StringVar()

        txt_nombre=Entry(ventana,textvariable=nombre,justify="center")
        txt_nombre.focus()
        txt_nombre.pack(pady=15)

        #Apellidos
        lbl_apellido=Label(ventana,text="¿Cual es tu apellido?:",justify="center")
        lbl_apellido.pack(pady=15)

        apellido=StringVar()

        txt_apellido=Entry(ventana,textvariable=apellido,justify="center")
        txt_apellido.pack(pady=15)

        #email
        lbl_email=Label(ventana,text="¿Cual es tu email?:",justify="center")
        lbl_email.pack(pady=15)

        email=StringVar()

        txt_email=Entry(ventana,textvariable=email,justify="center")
        txt_email.pack(pady=15)

        #contraseña
        lbl_contraseña=Label(ventana,text="¿Cual es tu contraseña?:",justify="center")
        lbl_contraseña.pack(pady=15)

        contraseña=StringVar()

        txt_contraseña=Entry(ventana,show="*",textvariable=contraseña,justify="center")
        txt_contraseña.pack(pady=15)

        #boton de registrar
        btn_registrar=Button(ventana,text="Registrar",
        command=lambda:     {
                            controlador1.Controlador.registro(txt_nombre.get(),txt_apellido.get(),txt_email.get(),txt_contraseña.get()),
                            View.login(ventana)
                            }
                            )

        btn_registrar.pack(pady=10)

        #boton de volver
        btn_volver=Button(ventana,text="volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def login(ventana):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=".:: Login ::.",justify="center")
        lbl_titulo.pack(pady=10)

        
        lbl_email=Label(ventana,text="Ingresa tu email:",justify="center")
        lbl_email.pack(pady=15)

        email=StringVar()

        txt_email=Entry(ventana,textvariable=email,justify="center")
        txt_email.pack(pady=15)

        #contraseña
        lbl_contraseña=Label(ventana,text="Ingresa tu contraseña?:",justify="center")
        lbl_contraseña.pack(pady=15)

        contraseña=StringVar()

        txt_contraseña=Entry(ventana,show="*",textvariable=contraseña,justify="center")
        txt_contraseña.pack(pady=15)

        #boton de Entrar
        btn_Entrar=Button(ventana,text="Entrar",
        command=lambda:controlador1.Controlador.inicio_sesion(ventana,txt_email.get(),txt_contraseña.get()))
        btn_Entrar.pack(pady=10)

        #boton de volver
        btn_volver=Button(ventana,text="volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def menu_Notas(ventana,usuario_id,nombre,apellidos):
        global id_user,nom_user,ape_user
        id_user=usuario_id
        nom_user=nombre
        ape_user=apellidos
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=f".:: Bienvenido {nombre} {apellidos}, has iniciado sesión ::.",justify="center")
        lbl_titulo.pack(pady=10)

        btn_crear=Button(ventana,text="Crear",justify="center",width=15,command=lambda:View.crear_Notas(ventana))
        btn_crear.pack(pady=15)

        btn_mostrar=Button(ventana,text="Mostrar",justify="center",width=15,command=lambda:View.mostrar_Notas(ventana))
        btn_mostrar.pack(pady=15)

        btn_cambiar=Button(ventana,text="Cambiar",justify="center",width=15,command=lambda:View.cambiar_notas(ventana))
        btn_cambiar.pack(pady=15)

        btn_eliminar=Button(ventana,text="Eliminar",justify="center",width=15,command=lambda:View.eliminar_nota(ventana))
        btn_eliminar.pack(pady=15)

        btn_volver=Button(ventana,text="Regresar",justify="center",width=15,command=lambda:View.login(ventana))
        btn_volver.pack(pady=15)

    @staticmethod
    def crear_Notas(ventana):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=".:: Crear Nota ::.",justify="center")
        lbl_titulo.pack(pady=10)

        #Titulo
        lbl_titulo=Label(ventana,text="Titulo:",justify="center")
        lbl_titulo.pack(pady=15)

        titulo=StringVar()

        txt_titulo=Entry(ventana,textvariable=titulo,justify="center")
        txt_titulo.focus()
        txt_titulo.pack(pady=15)

        #Descripcion
        lbl_descripcion=Label(ventana,text="Descripcion:",justify="center")
        lbl_descripcion.pack(pady=15)

        descripcion=StringVar()

        txt_descripcion=Entry(ventana,show="*",textvariable=descripcion,justify="center")
        txt_descripcion.pack(pady=15)

        #boton de Guardar
        btn_guardar=Button(ventana,text="Guardar",command="")
        btn_guardar.pack(pady=10)

        #boton de volver
        btn_volver=Button(ventana,text="volver",command=lambda:View.menu_Notas(ventana,id_user,nom_user,ape_user))
        btn_volver.pack(pady=10)

    @staticmethod
    def mostrar_Notas(ventana):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text=".:: {nombre} {apellido}, tus notas: ::.",justify="center")
        lbl_titulo.pack(pady=10)

        filas=""
        registros=[("1","100","Nota 1","Descripcion de la nota 1","2025-11-24")]
        num_nota=1

        if len(registros)>0:
            for fila in registros:
                filas=filas+f"Nota: {num_nota}\n ID {fila[0]}.- Titulo: {fila[2]} Fecha de creacion: {fila[4]} \n Descricion: {fila[3]}"
                num_nota+=1
        else:
            messagebox.showwarning(icon="warning",message="No existen Notas para este usuario")
        
        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)


        #boton de volver
        btn_volver=Button(ventana,text="volver",command=lambda:View.menu_Notas(ventana,id_user,nom_user,ape_user))
        btn_volver.pack(pady=10)

    @staticmethod
    def cambiar_notas(ventana):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text="{nombre} {apellido} vamos a modificar una nota: ",justify="center")
        lbl_titulo.pack(pady=10)

        #ID
        lbl_id=Label(ventana,text="ID de la nota a cambiar: ",justify="center")
        lbl_id.pack(pady=10)

        id=StringVar()

        txt_id=Entry(ventana,textvariable=id,justify="center")
        txt_id.focus()
        txt_id.pack(pady=10)

        #Nuevo Titulo
        lbl_nuevo_titulo=Label(ventana,text="Nuevo titulo: ",justify="center")
        lbl_nuevo_titulo.pack(pady=10)

        nuevo_titulo=StringVar()

        txt_nuevo_titulo=Entry(ventana,textvariable=nuevo_titulo,justify="center")
        txt_nuevo_titulo.pack(pady=10)

        #Nueva descripcion
        lbl_nueva_descripcion=Label(ventana,text="Nueva descripcion: ",justify="center")
        lbl_nueva_descripcion.pack(pady=10)

        nueva_descripcion=StringVar()

        txt_nueva_descripcion=Entry(ventana,textvariable=nueva_descripcion,justify="center")
        txt_nueva_descripcion.pack(pady=10)

        #boton de Guardar
        btn_guardar=Button(ventana,text="Guardar",command="")
        btn_guardar.pack(pady=10)

        #boton de volver
        btn_volver=Button(ventana,text="volver",command=lambda:View.menu_Notas(ventana,id_user,nom_user,ape_user))
        btn_volver.pack(pady=10)

    @staticmethod
    def eliminar_nota(ventana):
        View.borrar_pantalla(ventana)
        lbl_titulo=Label(ventana,text="{nombre} {apellido} vamos a eliminar una nota: ",justify="center")
        lbl_titulo.pack(pady=10)

        #Nota a eliminar
        lbl_id=Label(ventana,text="ID de la nota a eliminar: ",justify="center")
        lbl_id.pack(pady=10)

        id=StringVar()

        txt_id=Entry(ventana,textvariable=id,justify="center")
        txt_id.focus()
        txt_id.pack(pady=10)

        #boton de Eliminar
        btn_eliminar=Button(ventana,text="Eliminar",command="")
        btn_eliminar.pack(pady=10)

        #boton de volver
        btn_volver=Button(ventana,text="volver",command=lambda:View.menu_Notas(ventana,id_user,nom_user,ape_user))
        btn_volver.pack(pady=10)