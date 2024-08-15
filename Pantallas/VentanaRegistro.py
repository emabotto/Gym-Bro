import tkinter as tk
import customtkinter as ctk
from Pantallas.Ventana import Miventana
from BaseDeDatos.Datos import *

class Registro(Miventana):
    def __init__(self):
        super().__init__('Registro')

    def Abrir_ventana(self):
        self.main_ventana.geometry("400x400")

        botones = ['Registrarse', 'Volver']

        entrada = ctk.CTkFrame(master=self.main_ventana,width=200,height=280,corner_radius=10)
        entrada.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.admin = ctk.StringVar()  
        check=ctk.CTkCheckBox(self.main_ventana, text='Administrador',variable=self.admin, onvalue="1", offvalue="0", command=self.Actualizar_Valor)            
        check.pack(pady=10, anchor=tk.CENTER) 

        self.usu_regis=ctk.CTkEntry(master=self.main_ventana, width=120,height=25,corner_radius=5) 
        self.usu_regis.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        
        self.cont_regis=ctk.CTkEntry(master=self.main_ventana, width=120,height=25,corner_radius=5) 
        self.cont_regis.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.nombre_regis=ctk.CTkEntry(master=self.main_ventana, width=120,height=25,corner_radius=5) 
        self.nombre_regis.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
        
        self.apellido_regis=ctk.CTkEntry(master=self.main_ventana, width=120,height=25,corner_radius=5) 
        self.apellido_regis.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
        
        contador = 0.0
        for  i in botones:  
            boton = ctk.CTkButton(self.main_ventana, text = i, command = lambda texto = i: self.Boton_Apretado(texto), width=60,height=5,anchor=tk.CENTER)
            boton.pack(pady=10, anchor=tk.CENTER)
            contador = contador + 0.1

    def Boton_Apretado(self,Apretado):
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
        
        if Verificar_Datos(self.usuario,self.contra) == True:
            print('YA EXISTE ESTE MAMA HUEVO')
        else:
            tipo = self.admin.get()
            nombre = self.nombre_regis.get() 
            apellido = self.apellido_regis.get()
            telefono = 'Telefono no ingresado'
            Agregar_Usuario(self.usuario,self.contra,tipo, nombre,apellido,telefono)
            print('Se registro correctamente')

