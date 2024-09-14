import tkinter as tk
import customtkinter as ctk
from datetime import date
import calendar 


class Clases:
    def __init__(self,ventana) -> None:
        self.ventana = ventana
        self.cupo_max = 15
        self.fecha = date.today()
        self.mes = int(format(self.fecha.month))
        self.basura, self.cant_dias = calendar.monthrange(2024,self.mes)
        
        self.crear_clase()
        
    def crear_clase(self):
    
        clases = ['Funcional', 'Crossfit', 'Zumba', 'Calistenia','Boxeo']
        meses = ['Enero','Febrero','Marzo','Abril','Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre','Diciembre']
        
        titulo = ctk.CTkLabel(self.ventana, text="Crear Clase", font=("Arial", 16))
        titulo.pack(pady=10)
        
        # Seleccionar el self.mes
        mes_var = ctk.StringVar(value=meses[self.mes-1])
        mes_etiqueta = ctk.CTkLabel(self.ventana, text="Selecciona el Mes:")
        mes_etiqueta.pack(pady=5)
        mes_menu = ctk.CTkOptionMenu(self.ventana, variable=mes_var, values=meses)
        mes_menu.pack(pady=5)
        
        # Seleccionar el dia
        dia = ctk.StringVar(value="1")
        dia_label = ctk.CTkLabel(self.ventana, text="Selecciona el Día:")
        dia_label.pack(pady=5)
        dia_menu = ctk.CTkOptionMenu(self.ventana, variable=dia, values=[str(i+1) for i in range(self.cant_dias)])
        dia_menu.pack(pady=5)
        
        # Seleccionar tipo de clase
        tipo = ctk.StringVar(value='Elegir clase')
        tipo_clase = ctk.CTkLabel(self.ventana, text="Tipo de la Clase:")
        tipo_clase.pack(pady=5)
        tipo_clase_menu = ctk.CTkOptionMenu(self.ventana, variable=tipo,values=[str(i) for i in clases])
        tipo_clase_menu.pack(pady=5)
        
        # Defenir cupo maximo
        cupo = ctk.StringVar(value='1')
        cupo_label = ctk.CTkLabel(self.ventana, text="Cupo Máximo:")
        cupo_label.pack(pady=5)
        cupo_max_menu = ctk.CTkOptionMenu(self.ventana, variable=cupo,values=[str(i+1) for i in range(self.cupo_max)])
        cupo_max_menu.pack(pady=5)
        
        guardar = ctk.CTkButton(self.ventana, text="Guardar Clase", command=self.guardar_clase)
        guardar.pack(pady=20)

    def guardar_clase(self):
        return