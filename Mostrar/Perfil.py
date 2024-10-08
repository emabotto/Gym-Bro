from BaseDeDatos.Datos import *
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image

class Perfil:
    def __init__(self,contenedor,i):

        self.contenedor =  ctk.CTkFrame(contenedor, width=300, height=600)
        self.contenedor.grid(row=0, column=0, padx=50, pady=120, sticky="nsew")#El sticky hace que se ocupe el espacio de todo el contenedor
        self.contenedor2 =  ctk.CTkFrame(contenedor, width=200, height=600)
        self.contenedor2.grid(row=0, column=1, padx=0, pady=140, sticky="nsew")

        self.i = int(i)
        self.lista = Tomar_Datos(self.i)
        self.imagen = self.lista[6]
        self.Mostrar_en_Pantalla()
        
    def Mostrar_en_Pantalla(self):
        self.entradas = []
        fila = 0
        
        etiquetas = ['Correo','Contraseña','Nombre','Apellido','Telefono']

        for i in range(len(etiquetas)):
            etiqueta = ctk.CTkLabel(self.contenedor,text=etiquetas[i])
            etiqueta.grid(row= i, column=0, padx=30, pady=10)

        for i in range(len(self.lista)-2):
            entrada = ctk.CTkEntry(self.contenedor, width=150, placeholder_text= self.lista[i])
            if i == 4 and self.lista[i] == 'Ingresar telefono':
                pass
            else:
                entrada.insert(0, self.lista[i])
            entrada.configure(state='disabled')
            entrada.grid(row=i, column=1, padx=5, pady=10)
            self.entradas.append(entrada)
        
        for i in self.entradas:
            boton = ctk.CTkButton(self.contenedor, text='Editar', command=lambda texto = i: self.EditarCampo(texto),width=40, height=30)
            boton.grid(row=fila, column=2, padx=25, pady=5)
            fila += 1
        
        boton = ctk.CTkButton(self.contenedor, text='Guardar Cambios', command=self.GuardarCambios)
        boton.grid(row=5, column=1, padx=30, pady=10)
        self.Mostrar_Imagen(self.imagen)
        boton = ctk.CTkButton(self.contenedor2, text= 'Cargar Imagen', command = self.Cargar_Imagen)
        boton.grid(row = 2, column = 1,padx = 30, pady = 10)

    def EditarCampo(self,i):
        i.configure(state='normal')
        i.focus()
        
    def GuardarCambios(self):
        self.mod = []
        cont = 0
        for i in self.entradas:
            if i.get() == '':
                self.mod.append(self.lista[cont])
            else:
                self.mod.append(i.get())
            cont = cont + 1
        self.mod.append(self.imagen)
        print(self.mod)
        Modificar_Datos(self.mod, self.i)

        self.Mostrar_en_Pantalla()
   
    def Mostrar_Imagen(self,imagen):
        tamanio = (175,175)
        imagen_elejida = Image.open(imagen) 
        foto = ctk.CTkImage(dark_image=imagen_elejida, size= tamanio)  
        label = ctk.CTkLabel(self.contenedor2, text='',image= foto, anchor=('center'))
        label.grid(row=0, column=1, padx=15, pady=10)

    def Cargar_Imagen(self): # Carga fotos de perfil que esten en la carpeta 'Imagenes'
        archivo = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")]) #Solo archivos con este formato
        if not archivo:  # este IF esta solo para que no tire error cuando no selecciono nada 
            return
        direccion = archivo.split('/')
        archivo = str(direccion[len(direccion)-2]+'/'+direccion[len(direccion)-1])
        
        self.imagen = archivo

        self.GuardarCambios()
        self.Mostrar_Imagen(archivo)
    
