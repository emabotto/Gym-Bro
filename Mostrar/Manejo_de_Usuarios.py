import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from BaseDeDatos.Datos import *


class Gestion_Usuario:
    def __init__(self, contenedor):
        self.contenedor = ctk.CTkFrame(contenedor, width=800, height=600)
        self.contenedor.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.privilegios_seleccionables = ['Cliente', 'Administrador']
        
        self.trash_icon = Image.open("Imagenes/Inconos/Basurero.png")
        self.trash_icon = self.trash_icon.resize((20, 20), Image.Resampling.LANCZOS)
        self.trash_icon = ImageTk.PhotoImage(self.trash_icon)
        
        self.act_icon = Image.open("Imagenes/Inconos/Actualizar.png")
        self.act_icon = self.act_icon.resize((20, 20), Image.Resampling.LANCZOS)
        self.act_icon = ImageTk.PhotoImage(self.act_icon)
        
        self.Mostrar_Usuarios_registrados()

    def Mostrar_Usuarios_registrados(self):
        # Limpiar la interfaz antes de volver a mostrar los datos
        for widget in self.contenedor.winfo_children():
            widget.destroy()

        etiquetas = ['Correo', 'Privilegios', 'Acción']
        col = 0
        for etiqueta in etiquetas:
            ctk.CTkLabel(self.contenedor, text=etiqueta, font=("Arial", 14, "bold")).grid(row=0, column=col, padx=20, pady=10)
            col += 1

        usuarios = self.Limpiar_Lista()
        for i, usuario in enumerate(usuarios):
            col = 0
            for dato in usuario[:-1]:
                ctk.CTkLabel(self.contenedor, text=dato).grid(row=i+1, column=col, padx=20, pady=10)
                col += 1
            
            # ComboBox para seleccionar nuevos privilegios
            nuevo_privilegio = ctk.CTkOptionMenu(self.contenedor, values=self.privilegios_seleccionables)
            nuevo_privilegio.set(usuario[-1])
            nuevo_privilegio.grid(row=i+1, column=col, padx=20, pady=10)
            
            # Botón para actualizar privilegios
            btn_actualizar = ctk.CTkButton(self.contenedor, text='',image=self.act_icon, command=lambda i=i, nuevo_priv=nuevo_privilegio: self.Actualizar_Privilegio(i, nuevo_priv),width=20,height=20)
            btn_actualizar.grid(row=i+1, column=col+1, padx=20, pady=10)
            
            # Botón para eliminar usuario
            btn_eliminar = ctk.CTkButton(self.contenedor,text='', image=self.trash_icon, command=lambda i=i: self.Eliminar_Usuario(i),width=20,height=20)
            btn_eliminar.grid(row=i+1, column=col+2, padx=5, pady=10)
            
    
    def Limpiar_Lista(self):
        lista = []
        for i in range(len(usu.correo)):
            datos = Tomar_Datos(i)
            if datos[5] == '1':
                datos[5] = 'Administrador'
            else:
                datos[5] = 'Cliente'
            lista.append(tuple(datos[:1] + [datos[5]]))
        return lista
    
    def Actualizar_Privilegio(self, index, nuevo_privilegio_widget):
        nuevo_privilegio = nuevo_privilegio_widget.get()
        usuario_id = self.Limpiar_Lista()[index][0]  # Suponiendo que el correo es el ID
        if nuevo_privilegio == 'Administrador':
            privilegio_valor = '1'
        else:
            privilegio_valor = '0'
        self.Actualizar_Privilegio_Usuario(usuario_id, privilegio_valor)
        self.Mostrar_Usuarios_registrados()
    
    def Eliminar_Usuario(self, index):
        usuario_id = self.Limpiar_Lista()[index][0]  # Suponiendo que el correo es el ID
        confirmacion = tk.messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres eliminar este usuario?")
        if confirmacion:
            self.Eliminar_Usuario(usuario_id)
            self.Mostrar_Usuarios_registrados()
    
    def  Actualizar_Privilegio_Usuario(usuario_id, privilegio_valor):
        return
    def Eliminar_Usuario(usuario_id):
        return