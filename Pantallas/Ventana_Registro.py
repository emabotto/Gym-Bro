import tkinter as tk 
import customtkinter as ctk
from tkinter import messagebox
from Pantallas.Ventana import Miventana
from BaseDeDatos.Datos import *


class Registro(Miventana):
    def __init__(self):
        super().__init__('Registro de Usuario',600,450)

    def Abrir_ventana(self):

        contenedor_registro = ctk.CTkFrame(master=self.main_ventana,corner_radius=10)
        contenedor_registro.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        titulo = ctk.CTkLabel(contenedor_registro, text="REGISTRO", font=("Arial", 20))
        titulo.pack(pady=20)

        # Campos de contenedor_registro
        self.usu_regis = ctk.CTkEntry(master=contenedor_registro, width=220, height=35, placeholder_text="Correo")
        self.usu_regis.pack(pady=(50,10))

        self.cont_regis = ctk.CTkEntry(master=contenedor_registro, width=220, height=35, placeholder_text="Contraseña", show="*")
        self.cont_regis.pack(pady=10)

        self.nombre_regis = ctk.CTkEntry(master=contenedor_registro, width=220, height=35, placeholder_text="Nombre")
        self.nombre_regis.pack(pady=10)

        self.apellido_regis = ctk.CTkEntry(master=contenedor_registro, width=220, height=35, placeholder_text="Apellido")
        self.apellido_regis.pack(pady=10)
        
        # Checkbox para administrador
        self.admin = ctk.StringVar()
        check = ctk.CTkCheckBox(contenedor_registro, text='Administrador', variable=self.admin, onvalue="1", offvalue="0", command=self.Actualizar_Valor)
        check.pack(pady=10)

        botones_frame = ctk.CTkFrame(contenedor_registro)
        botones_frame.pack(pady=20)

        registrarse_btn = ctk.CTkButton(botones_frame, text="Registrarse", command=lambda: self.Boton_Apretado("Registrarse"), width=100, height=40, fg_color='#1ABC9C', border_color= '#000000')
        registrarse_btn.grid(row=0, column=1, padx=10)

        volver_btn = ctk.CTkButton(botones_frame, text="Volver", command=lambda: self.Boton_Apretado("Volver"), width=100, height=40)
        volver_btn.grid(row=0, column=0, padx=10)

    def Boton_Apretado(self,Apretado):
        if Apretado == 'Registrarse':
            self.Verificar_Datos_Existentes()
        else:
            self.Cerrar_Ventana()

    def Actualizar_Valor(self):
        self.tipo = self.admin.get()

    def Cerrar_Ventana(self):
        from Pantallas.Inicio_Secicion import VentanaIniciarSecion
        self.main_ventana.destroy() 
        ventana_inicio_sesion = VentanaIniciarSecion()
        ventana_inicio_sesion.Abrir_ventana()
        ventana_inicio_sesion.mostrar()

    def Verificar_Datos_Existentes(self):
        self.usuario = self.usu_regis.get()
        self.contra = self.cont_regis.get()
        nombre = self.nombre_regis.get()
        apellido = self.apellido_regis.get()

        if nombre != '' and apellido != '' and self.usuario != ''and self.contra != '':
            if verificar_registro(self.usuario) != True:
                tipo = self.admin.get()
                telefono = 'Ingresar telefono'
                Agregar_Usuario(self.usuario,self.contra,tipo, nombre,apellido,telefono)
                messagebox.showinfo('Registro exitoso','El usuario se registro correctamente')
                self.Cerrar_Ventana()
            else:
                messagebox.showerror('Fallo en Registro','Ya existe este usuario')
        else:
            messagebox.showinfo('Fallo en Registro','Algunos campos no se comletaron')