from tkinter import messagebox
import customtkinter as ctk
from PIL import Image, ImageTk
from BaseDeDatos.Datos import *  
from BaseDeDatos.Usuario import Usuario

class Gestion_Usuario:
    def __init__(self, contenedor):
        
        self.scroll_frame = ctk.CTkScrollableFrame(contenedor, width=750, height=580)
        self.scroll_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        self.scroll_frame.grid_columnconfigure(0, weight=2)  # Columna de correos más ancha
        self.scroll_frame.grid_columnconfigure(1, weight=1)  # Columna de privilegios
        self.scroll_frame.grid_columnconfigure(2, weight=1)  # Columna de botones
        
        self.privilegios_seleccionables = ['Cliente', 'Administrador']
        
        # Cargar íconos
        self.trash_icon = self.cargar_icono("Imagenes/Inconos/Basurero.png")
        self.act_icon = self.cargar_icono("Imagenes/Inconos/Actualizar.png")
        
        # Mostrar los usuarios al cargar
        self.Mostrar_Usuarios_registrados()

    def cargar_icono(self, ruta):
        # Función para cargar y redimensionar íconos
        icono = Image.open(ruta)
        icono = icono.resize((20, 20), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(icono)

    def Mostrar_Usuarios_registrados(self):
        # Limpiar la interfaz antes de volver a mostrar los datos
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()
            
        etiquetas = ['Correo', 'Privilegios', 'Acción']
        for col, etiqueta in enumerate(etiquetas):
            ctk.CTkLabel(self.scroll_frame, text=etiqueta, font=("Arial", 14, "bold")).grid(row=0, column=col, padx=20, pady=10, sticky="ew")

        # Mostrar usuarios
        usuarios = self.Limpiar_Lista()
        for i, usuario in enumerate(usuarios):
            ctk.CTkLabel(self.scroll_frame, text=usuario[0], anchor="w").grid(row=i+1, column=0, padx=20, pady=10, sticky="ew")
            
            # ComboBox para seleccionar nuevos privilegios
            nuevo_privilegio = ctk.CTkOptionMenu(self.scroll_frame, values=self.privilegios_seleccionables)
            nuevo_privilegio.set(usuario[-1])
            nuevo_privilegio.grid(row=i+1, column=1, padx=20, pady=10, sticky="ew")
            
            # Botones de acción
            self.crear_botones_accion(i, nuevo_privilegio, 2)

    def crear_botones_accion(self, i, nuevo_privilegio, col):
        # Botón para actualizar privilegios
        ctk.CTkButton(self.scroll_frame, text='', image=self.act_icon, 
                      command=lambda: self.Actualizar_Privilegio(i, nuevo_privilegio), width=20, height=20).grid(row=i+1, column=col, padx=20, pady=10)
        
        # Botón para eliminar usuario
        ctk.CTkButton(self.scroll_frame, text='', image=self.trash_icon, 
                      command=lambda: self.Eliminar_Usuario(i), width=20, height=20).grid(row=i+1, column=col+1, padx=5, pady=10)

    def Limpiar_Lista(self):
        # Cargar datos de la base de datos y transformar los privilegios
        lista = []
        for i in range(len(usu.correo)):
            datos = Tomar_Datos(i)
            datos[5] = 'Administrador' if datos[5] == '1' else 'Cliente'
            lista.append(tuple(datos[:1] + [datos[5]]))
        return lista

    def Actualizar_Privilegio(self, i, nuevo_privilegio_widget):
        # Actualizar privilegios en la base de datos
        nuevo_privilegio = nuevo_privilegio_widget.get()
        usuario_id = self.Limpiar_Lista()[i][0]  
        privilegio_valor = '1' if nuevo_privilegio == 'Administrador' else '0'
        self.Actualizar_Privilegio_Usuario(usuario_id, privilegio_valor)
        self.Mostrar_Usuarios_registrados()  # Recargar usuarios actualizados

    def Eliminar_Usuario(self, i):
        # Eliminar usuario tras confirmación
        usuario_id = self.Limpiar_Lista()[i][0] 
        confirmacion = messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres eliminar este usuario?")
        if confirmacion:
            self.Eliminar_Usuario_BD(usuario_id)
            self.Mostrar_Usuarios_registrados()
        
    def Actualizar_Privilegio_Usuario(self, usuario_id, privilegio_valor):
        usuarios = []
        
        with open('BaseDeDatos/Cuentas.txt', 'r') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:  
                    datos = linea.split(',')
                    if datos[0] == usuario_id:
                        datos[5] = privilegio_valor  # Actualizar privilegio
                    usuarios.append(','.join(datos))
        
        # Escribir de nuevo en el archivo
        with open('BaseDeDatos/Cuentas.txt', 'w') as archivo:
            for usuario in usuarios:
                archivo.write(usuario + '\n')

        messagebox.showinfo("Éxito", f"Privilegio actualizado para {usuario_id}.")
        Leer_Datos_Guardados()
        
    def Eliminar_Usuario_BD(self, usuario_id):
        # Lógica para eliminar usuario de la base de datos
        usuarios = []
        
        with open('BaseDeDatos/Cuentas.txt', 'r') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:  # Verificar que la línea no esté vacía
                    datos = linea.split(',')
                    if datos[0] != usuario_id:  # No agregar al listado si coincide el ID
                        usuarios.append(linea)
        
        # Escribir de nuevo en el archivo
        with open('BaseDeDatos/Cuentas.txt', 'w') as archivo:
            for usuario in usuarios:
                archivo.write(usuario + '\n')

        messagebox.showinfo("Éxito", f"Usuario {usuario_id} eliminado correctamente.")
        Leer_Datos_Guardados()
