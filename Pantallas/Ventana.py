import tkinter as tk
import customtkinter as ctk
from abc import ABC
from abc import abstractmethod

class Miventana(ABC):
    @abstractmethod
    def __init__(self, titulo):
        self.titulo = titulo
        self.main_ventana = ctk.CTk()
    
    @abstractmethod
    def Abrir_ventana(self):
        pass

    @abstractmethod
    def Cerrar_Ventana(self):
        pass
    
    def mostrar(self):
        self.main_ventana.title(self.titulo)
        self.main_ventana.mainloop()
