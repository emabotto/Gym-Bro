import tkinter as tk
import customtkinter as ctk
from abc import ABC
from abc import abstractmethod

class Miventana(ABC):
    @abstractmethod
    def __init__(self, titulo):
        self.titulo = titulo
        self.main_ventana = ctk.CTk()
        width = 450
        height = 600
        screen_width = self.main_ventana.winfo_screenwidth()
        screen_height = self.main_ventana.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        self.main_ventana.geometry(f'{width}x{height}+{x}+{y}')
        self.main_ventana.resizable(False, False)
    
    @abstractmethod
    def Abrir_ventana(self):
        pass

    @abstractmethod
    def Cerrar_Ventana(self):
        pass
    
    def mostrar(self):
        self.main_ventana.title(self.titulo)
        self.main_ventana.mainloop()
