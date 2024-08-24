import tkinter as tk
import customtkinter as ctk
from Pantallas.Ventana import Miventana
from BaseDeDatos.Datos import *

class Registro(Miventana):
    def __init__(self):
        super().__init__('Registro')

    def Abrir_ventana(self):
        # Configurar la ventana principal
        self.main_ventana.geometry("400x500")
        self.main_ventana.title("Registro de Usuario")

        # Crear un frame centrado para contener los widgets
        entrada = ctk.CTkFrame(master=self.main_ventana, width=300, height=380, corner_radius=10)
        entrada.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Título
        titulo = ctk.CTkLabel(entrada, text="Registrar Usuario", font=("Arial", 18))
        titulo.pack(pady=20)

        # Campos de entrada
        self.usu_regis = ctk.CTkEntry(master=entrada, width=220, height=35, placeholder_text="Usuario")
        self.usu_regis.pack(pady=10)

        self.cont_regis = ctk.CTkEntry(master=entrada, width=220, height=35, placeholder_text="Contraseña", show="*")
        self.cont_regis.pack(pady=10)

        self.nombre_regis = ctk.CTkEntry(master=entrada, width=220, height=35, placeholder_text="Nombre")
        self.nombre_regis.pack(pady=10)

        self.apellido_regis = ctk.CTkEntry(master=entrada, width=220, height=35, placeholder_text="Apellido")
        self.apellido_regis.pack(pady=10)

        # Checkbox para administrador
        self.admin = ctk.StringVar()
        check = ctk.CTkCheckBox(entrada, text='Administrador', variable=self.admin, onvalue="1", offvalue="0", command=self.Actualizar_Valor)
        check.pack(pady=10)

        # Botones
        botones_frame = ctk.CTkFrame(entrada)
        botones_frame.pack(pady=20)

        registrarse_btn = ctk.CTkButton(botones_frame, text="Registrarse", command=lambda: self.Boton_Apretado("Registrarse"), width=100, height=40)
        registrarse_btn.grid(row=0, column=0, padx=10)

        volver_btn = ctk.CTkButton(botones_frame, text="Volver", command=lambda: self.Boton_Apretado("Volver"), width=100, height=40)
        volver_btn.grid(row=0, column=1, padx=10)

    def Boton_Apretado(self, Apretado):
        if Apretado == 'Registrarse':
            self.Verificar_Datos_Existentes()
        else:
            self.Cerrar_Ventana()

    def Actualizar_Valor(self):
        self.tipo = self.admin.get()

    def Cerrar_Ventana(self):
        from InicioSecicion import VentanaIniciarSecion
        self.main_ventana.destroy()
        atras = VentanaIniciarSecion()
        atras.Abrir_ventana()
        atras.mostrar()

    def Verificar_Datos_Existentes(self):
        self.usuario = self.usu_regis.get()
        self.contra = self.cont_regis.get()
        
        if Verificar_Datos(self.usuario, self.contra):
            print('El usuario ya existe')
        else:
            tipo = self.admin.get()
            nombre = self.nombre_regis.get()
            apellido = self.apellido_regis.get()
            telefono = 'Ingresar telefono'
            Agregar_Usuario(self.usuario, self.contra, tipo, nombre, apellido, telefono)
            print('Registro exitoso')

if __name__ == "__main__":
    app = Registro()
    app.Abrir_ventana()
    app.main_ventana.mainloop()
