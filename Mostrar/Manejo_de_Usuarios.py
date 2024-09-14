import tkinter as tk
import customtkinter as ctk
from BaseDeDatos.Datos import *


class Gestion_Usuario():
    def __init__(self, contenedor):
        self.contenedor =  ctk.CTkFrame(contenedor, width=300, height=600)
        self.contenedor.grid(row=0, column=0, padx=50, pady=100, sticky="nsew")
        self.Mostrar_Usuarios_registrados()
        
    def Mostrar_Usuarios_registrados(self):
        etiquetas = ['Correo', 'Nombre', 'Apellido', 'Privilegios']
        col = 0
        linea = 1
        for i in range(len(etiquetas)):
            etiqueta = ctk.CTkLabel(self.contenedor,text=etiquetas[i])
            etiqueta.grid(row= 0, column=col, padx=30, pady=10)
            col +=1
        
        col = 0
        for i in range(3):
            lista = self.Limpiar_Lista(i)
            for j in range(len(lista)):
                mostrar_dato = ctk.CTkLabel(self.contenedor, text = lista[j])
                mostrar_dato.grid(row = linea, column=col, padx=30, pady=10)
                col += 1
            linea +=1
        
    def Limpiar_Lista(self,i):
           lista = Tomar_Datos(i)
           if lista[5] == '1':
               lista[5] = 'Administrador'
           else:
               lista[5] = 'Cliente'
           lista_para_usar = lista[0],lista[2],lista[3],lista[5]
           print(lista_para_usar)
           return lista_para_usar