import tkinter as tk
import customtkinter as ctk
from datetime import date
import calendar 

def crear_clase(ventana):
    cupo_max = 15
    fecha = date.today()
    mes = int(format(fecha.month))
    basura, cant_dias = calendar.monthrange(2024,mes)
    clases = ['Funcional', 'Crossfit', 'Zumba', 'Calistenia','Boxeo']
    meses = ['Enero','Febrero','Marzo','Abril','Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre','Diciembre']
    
    titulo = ctk.CTkLabel(ventana, text="Crear Clase", font=("Arial", 16))
    titulo.pack(pady=10)
    
    # Seleccionar el mes
    mes_var = ctk.StringVar(value=meses[mes-1])
    mes_etiqueta = ctk.CTkLabel(ventana, text="Selecciona el Mes:")
    mes_etiqueta.pack(pady=5)
    mes_menu = ctk.CTkOptionMenu(ventana, variable=mes_var, values=meses)
    mes_menu.pack(pady=5)
    
    # Seleccionar el dia
    dia = ctk.StringVar(value="1")
    dia_label = ctk.CTkLabel(ventana, text="Selecciona el Día:")
    dia_label.pack(pady=5)
    dia_menu = ctk.CTkOptionMenu(ventana, variable=dia, values=[str(i+1) for i in range(cant_dias)])
    dia_menu.pack(pady=5)
    
    # Seleccionar tipo de clase
    tipo = ctk.StringVar(value='Elegir clase')
    tipo_clase = ctk.CTkLabel(ventana, text="Tipo de la Clase:")
    tipo_clase.pack(pady=5)
    tipo_clase_menu = ctk.CTkOptionMenu(ventana, variable=tipo,values=[str(i) for i in clases])
    tipo_clase_menu.pack(pady=5)
    
    # Defenir cupo maximo
    cupo = ctk.StringVar(value='1')
    cupo_label = ctk.CTkLabel(ventana, text="Cupo Máximo:")
    cupo_label.pack(pady=5)
    cupo_max_menu = ctk.CTkOptionMenu(ventana, variable=cupo,values=[str(i+1) for i in range(cupo_max)])
    cupo_max_menu.pack(pady=5)
    
    guardar = ctk.CTkButton(ventana, text="Guardar Clase", command=guardar_clase)
    guardar.pack(pady=20)

def guardar_clase():
    return