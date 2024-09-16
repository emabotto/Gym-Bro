import tkinter as tk
import customtkinter as ctk
from BaseDeDatos.Datos import Tomar_Datos
from Pantallas.Ventana import Miventana
from Mostrar.Calendario import Calendario
from Mostrar.Perfil import Perfil
from Mostrar.Manejo_de_Clases import *
from Mostrar.Manejo_de_Usuarios import *


class Inicio(Miventana):
    def __init__(self,ingreso):
        super().__init__('Gym-Bro - Menu Principal',625,975)
        self.ingreso = int(ingreso)
        self.info = Tomar_Datos(self.ingreso)
        
    def Abrir_ventana(self):
        
        self.main_ventana.grid_columnconfigure(1, weight=1)  # Permitir que la columna 1 (contenedor2) se expanda
        self.main_ventana.grid_rowconfigure(0, weight=1)     # Permitir que la fila 0 se expanda
        
        self.contenedor1 = ctk.CTkFrame(self.main_ventana, width=150, height=600)
        self.contenedor1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.Contenedores()
        self.Menu_Lateral()
        self.MostrarCalendario()
        
    def Contenedores(self):
        self.contenedor2 = ctk.CTkFrame(self.main_ventana)
        self.contenedor2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
    def botones(self,apretado):
        if apretado == 'Calendario':
            self.borrar_contenedor()
            self.MostrarCalendario()
        elif apretado == 'Perfil':
            self.borrar_contenedor()
            self.MostrarPerfil()
        elif apretado == 'Configuracion':
            self.borrar_contenedor()
            self.MostrarCalendario()
        elif apretado == 'Agregar Clases':
            self.borrar_contenedor()
            self.administrar_clases()
        elif apretado == 'Administrar Usuarios':
            self.borrar_contenedor()
            self.administrar_usuario()
        else: 
            self.borrar_contenedor()
    
    def administrar_clases(self):
        Clases(self.contenedor2)
        
    def administrar_usuario(self):
        Gestion_Usuario(self.contenedor2)
        
    def MostrarCalendario(self):
        Calendario(self.contenedor2)

    def MostrarPerfil(self):
        Perfil(self.contenedor2,self.ingreso)

    def Menu_Lateral(self):
        botones =  ['Calendario','Perfil','Configuracion','Rutina','Agregar Clases','Generar Reporte','Administrar Usuarios']
        alt = 10
        cont = 0 
        print(self.info)
        for i in botones:
            if cont < 3:
                self.generar_boton(i,alt)
            else: 
                if self.info[5] == '1':
                    self.generar_boton(i,alt)
            cont = cont + 1
            alt +=50
    
        boton = ctk.CTkButton(self.contenedor1, text='Salir', command =self.Cerrar_Ventana)
        boton.place(x=5,y=560)

    def generar_boton(self,i,alt):
        boton = ctk.CTkButton(self.contenedor1, text=i, command = lambda texto = i : self.botones(texto))
        boton.place(x=5, y=alt)     

    def Cerrar_Ventana(self):
        self.main_ventana.withdraw()
        self.main_ventana.destroy()

    def borrar_contenedor(self):
        self.contenedor2.destroy()
        self.Contenedores()
        