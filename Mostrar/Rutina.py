import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

def mostrar_mensaje(ventana_secundaria):
    imagen_original = Image.open("Imagenes/Imagen 1.jpg")
    imagen_redimensionada = imagen_original.resize((200, 200))  
        
    background_image = ImageTk.PhotoImage(imagen_redimensionada)

    fondo_label = ctk.CTkLabel(ventana_secundaria, image=background_image, text='')
    fondo_label.place(relwidth=1, relheight=1)

    mensaje = ctk.CTkLabel(ventana_secundaria, text="Esta función se implementará en una versión futura.", font=("Arial", 25, "bold"), text_color="#00aaff")
    mensaje.pack(pady=(160, 220))
    
        
