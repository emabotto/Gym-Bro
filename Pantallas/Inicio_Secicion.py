import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from Pantallas.Ventana import Miventana
from BaseDeDatos.Datos import Verificar_Datos
from Pantallas.Inicio import Inicio

class VentanaIniciarSecion(Miventana):
    
    def __init__(self):
        super().__init__('Iniciar Secion',600,450)
    
    def Abrir_ventana(self):
        botones = ['Ingresar', 'Registrarse', 'Salir']
        colorA = '#F43E17'
        colorB = '#000000'
        
        frame = ctk.CTkFrame(self.main_ventana,corner_radius=10)
        frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
    
        logo = Image.open("Imagenes/Imagen 1.jpg") 
        logo = logo.resize((200,200), Image.Resampling.LANCZOS) # 'Image.Resampling.LANCZOS' renderiza la imagen y le da una mejor calidad, es de la biblioteca PIL
        logo = ctk.CTkImage(light_image=logo, size=(200, 200))

        logo_label = ctk.CTkLabel(frame, image=logo,text='')
        logo_label.pack(pady=10)

        etiqueta_usuario = ctk.CTkLabel(frame, text='Usuario:')
        etiqueta_usuario.pack(pady=(0,10))

        self.usuario = ctk.CTkEntry(frame, width=200, height=30, corner_radius=5, placeholder_text='Usuario')
        self.usuario.pack(pady=(0,10))

        etiqueta_contrasenia = ctk.CTkLabel(frame, text='Contraseña:')
        etiqueta_contrasenia.pack(pady=(0,10))

        self.contrasenia = ctk.CTkEntry(frame, width=200, height=30, corner_radius=5,  placeholder_text='Contraseña', show='*')
        self.contrasenia.pack(pady=(0,10))

        for i in botones:
            boton = ctk.CTkButton(frame, text=i, command=lambda texto=i: self.Boton_Apretado(texto), width=120, height=35, fg_color=colorA, border_color=colorB)
            boton.pack(pady=(15,0))
 
    def Boton_Apretado(self,Apretado):
        if Apretado == 'Ingresar':
            entra = self.Ingresar()
            if entra == True:
                self.main_ventana.destroy()
                iniciar = Inicio(self.persona)
                iniciar.Abrir_ventana()
                iniciar.mostrar()
        elif Apretado == 'Registrarse':
            from Pantallas.Ventana_Registro import Registro # Se importa desde aca porque arriba genera una dependecia circular 
            self.main_ventana.destroy()
            registro = Registro()
            registro.Abrir_ventana()
            registro.mostrar()
        else:
            self.Cerrar_Ventana()

    def Ingresar(self):
        usuario = self.usuario.get()
        contra = self.contrasenia.get()
        self.entrada, self.persona = Verificar_Datos(usuario,contra)
        return self.entrada
 
    def Cerrar_Ventana(self):
        self.main_ventana.withdraw()
        self.main_ventana.quit()

