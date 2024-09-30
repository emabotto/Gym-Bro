from tkinter import  messagebox
import customtkinter as ctk
from datetime import date
import calendar
import os

class Clases:
    def __init__(self, ventana) -> None:
        self.ventana = ventana
        self.cupo_max = 15
        self.fecha = date.today()
        self.mes = int(format(self.fecha.month))
        self.basura, self.cant_dias = calendar.monthrange(2024, self.mes)
        
        self.crear_clase()

    def crear_clase(self):
        clases = ['Funcional', 'Crossfit', 'Zumba', 'Calistenia', 'Boxeo']
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

        titulo = ctk.CTkLabel(self.ventana, text="Crear Clase", font=("Arial", 16))
        titulo.pack(pady=10)

        # Seleccionar el mes
        self.mes_var = ctk.StringVar(value=meses[self.mes-1])
        mes_etiqueta = ctk.CTkLabel(self.ventana, text="Selecciona el Mes:")
        mes_etiqueta.pack(pady=5)
        mes_menu = ctk.CTkOptionMenu(self.ventana, variable=self.mes_var, values=meses)
        mes_menu.pack(pady=5)

        # Seleccionar el día
        self.dia = ctk.StringVar(value="1")
        dia_label = ctk.CTkLabel(self.ventana, text="Selecciona el Día:")
        dia_label.pack(pady=5)
        dia_menu = ctk.CTkOptionMenu(self.ventana, variable=self.dia, values=[str(i+1) for i in range(self.cant_dias)])
        dia_menu.pack(pady=5)

        # Seleccionar tipo de clase
        self.tipo = ctk.StringVar(value='Elegir clase')
        tipo_clase = ctk.CTkLabel(self.ventana, text="Tipo de la Clase:")
        tipo_clase.pack(pady=5)
        tipo_clase_menu = ctk.CTkOptionMenu(self.ventana, variable=self.tipo, values=[str(i) for i in clases])
        tipo_clase_menu.pack(pady=5)

        # Definir cupo máximo
        self.cupo = ctk.StringVar(value='1')
        cupo_label = ctk.CTkLabel(self.ventana, text="Cupo Máximo:")
        cupo_label.pack(pady=5)
        cupo_max_menu = ctk.CTkOptionMenu(self.ventana, variable=self.cupo, values=[str(i+1) for i in range(self.cupo_max)])
        cupo_max_menu.pack(pady=5)

        guardar = ctk.CTkButton(self.ventana, text="Guardar Clase", command=self.guardar_clase)
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
        archivo_ruta = 'C:/Users/Emanuel/OneDrive/Desktop/Gym-Bro/Archivos_admi/clases.txt'  # Cambia esta ruta si es necesario

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
            messagebox.showinfo("Exito", f"Se agrego la clase correctamente")
