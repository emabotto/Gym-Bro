import customtkinter as ctk
from tkinter import messagebox
from datetime import date
import calendar
import os

class Clases:
    def __init__(self, ventana) -> None:
        self.ventana = ventana
        self.cupo_max = 15
        self.fecha = date.today()
        self.mes = int(format(self.fecha.month))
        self.anio = int(format(self.fecha.year))
        self.basura, self.cant_dias = calendar.monthrange(self.anio, self.mes)
        
        self.crear_clase()

    def crear_clase(self):
        # Listas para las opciones
        clases = ['Funcional', 'Crossfit', 'Zumba', 'Calistenia', 'Boxeo']
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

        # Contenedor principal
        contenedor = ctk.CTkFrame(self.ventana, corner_radius=10, fg_color="transparent", width=450, height=600)
        contenedor.pack(padx=300, pady=80)
        
        # Título
        titulo = ctk.CTkLabel(contenedor, text="CREAR CLASE", font=("Arial", 20, "bold"), text_color="#00aaff")
        titulo.pack(padx = 20, pady=10)

        # Seleccionar el mes
        self.mes_var = ctk.StringVar(value=meses[self.mes - 1])
        mes_etiqueta = ctk.CTkLabel(contenedor, text="Selecciona el Mes:", text_color="white")
        mes_etiqueta.pack(padx = 20, pady=5)
        mes_menu = ctk.CTkOptionMenu(contenedor, variable=self.mes_var, values=meses, width=150)
        mes_menu.pack(padx = 20, pady=5)

        # Seleccionar el día
        self.dia = ctk.StringVar(value="1")
        dia_label = ctk.CTkLabel(contenedor, text="Selecciona el Día:", text_color="white")
        dia_label.pack(pady=5)
        dia_menu = ctk.CTkOptionMenu(contenedor, variable=self.dia, values=[str(i + 1) for i in range(self.cant_dias)], width=150)
        dia_menu.pack(pady=5)

        # Seleccionar tipo de clase
        self.tipo = ctk.StringVar(value="Elegir clase")
        tipo_clase = ctk.CTkLabel(contenedor, text="Tipo de la Clase:", text_color="white")
        tipo_clase.pack(pady=5)
        tipo_clase_menu = ctk.CTkOptionMenu(contenedor, variable=self.tipo, values=clases, width=150)
        tipo_clase_menu.pack(pady=5)

        # Definir cupo máximo
        self.cupo = ctk.StringVar(value="1")
        cupo_label = ctk.CTkLabel(contenedor, text="Cupo Máximo:", text_color="white")
        cupo_label.pack(pady=5)
        cupo_max_menu = ctk.CTkOptionMenu(contenedor, variable=self.cupo, values=[str(i + 1) for i in range(self.cupo_max)], width=150)
        cupo_max_menu.pack(pady=5)

        # Botón de guardar
        guardar = ctk.CTkButton(contenedor, text="Guardar Clase", command=self.guardar_clase, width=150)
        guardar.pack(pady=20)

    def guardar_clase(self):
        clase_seleccionada = self.tipo.get()
        dia_seleccionado = self.dia.get()
        mes_seleccionado = self.mes_var.get()

        # Convertir mes a formato numérico
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        mes_numero = meses.index(mes_seleccionado) + 1
        fecha_clase = f"{int(dia_seleccionado):02d}/{mes_numero:02d}/2024"

        # Ruta del archivo
        archivo_ruta = 'C:/Users/Emanuel/OneDrive/Desktop/Gym-Bro/Archivos_admi/clases.txt'

        if not os.path.exists(archivo_ruta):
            ctk.CTkLabel(self.ventana, text="Error: No se encontró el archivo clases.txt", text_color="red").pack(pady=10)
            return

        # Verificar si ya existe una clase en ese día
        clase_existe = False
        with open(archivo_ruta, 'r') as archivo:
            for linea in archivo:
                if f"Clase: {clase_seleccionada}" in linea and f"Dia: {fecha_clase}" in linea:
                    clase_existe = True
                    break

        if clase_existe:
            messagebox.showerror("Error", f"Ya existe la clase en el dia {fecha_clase}")
        else:
            with open(archivo_ruta, 'a') as archivo:
                archivo.write(f"Clase: {clase_seleccionada} - Dia: {fecha_clase} - Cupo Maximo: {self.cupo.get()}\n")
            messagebox.showinfo("Exito", f"Se agregó la clase correctamente")
