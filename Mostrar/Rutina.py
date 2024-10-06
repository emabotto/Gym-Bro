import tkinter as tk
import customtkinter as ctk

def mostrar_mensaje(ventana_secundaria):
    
    mensaje = ctk.CTkLabel(ventana_secundaria, text="Esta función se implementará en una versión futura.", font=("Arial", 25, "bold"), text_color="#00aaff")
    mensaje.pack(pady=(160, 220))
