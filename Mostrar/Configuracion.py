import tkinter as tk
import customtkinter as ctk

def Ventana_Config(ventana):
    boton = ctk.CTkButton(ventana, text = 'Colo de Botones', command = Elegir_color(), width=60,height=5,anchor=tk.CENTER)
    boton.pack(pady=10, anchor=tk.CENTER)

    
def Elegir_color():
    dfds = 9