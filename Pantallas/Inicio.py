import tkinter as tk
import customtkinter as ctk
from Pantallas.Ventana import Miventana
from Mostrar.Mi_Calendario import Calendario
from Mostrar.Perfil import Perfil


class Inicio(Miventana):
    def __init__(self,ingreso):
        super().__init__('Mneu Principal')
        self.ingreso = ingreso

    def Abrir_ventana(self):
        self.main_ventana.geometry('975x625')
        self.contenedor1 = ctk.CTkFrame(self.main_ventana, width=150, height=600)
        self.contenedor1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.Contenedores()
        self.Menu_Lateral()
    
    def Contenedores(self):
        self.contenedor2 = ctk.CTkFrame(self.main_ventana, width=500, height=600)
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
        else: 
            self.borrar_contenedor()
    
    def MostrarCalendario(self):
        Calendario(self.contenedor2)

    def MostrarPerfil(self):
        Perfil(self.contenedor2,self.ingreso)

    def Menu_Lateral(self):
        botones =  ['Calendario','Perfil','Configuracion','Rutina']
        alt = 10
        for i in botones:
            boton = ctk.CTkButton(self.contenedor1, text=i, command = lambda texto = i : self.botones(texto))
            boton.place(x=5, y=alt)
            alt +=50

        boton = ctk.CTkButton(self.contenedor1, text='Salir', command =self.Cerrar_Ventana)
        boton.place(x=5,y=560)

    def Cerrar_Ventana(self):
        self.main_ventana.withdraw()
        self.main_ventana.destroy()

    def borrar_contenedor(self):
        self.contenedor2.destroy()
        self.Contenedores()
        