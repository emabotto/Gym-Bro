import customtkinter as ctk
from tkinter import Tk
from datetime import date
import calendar

class Calendario:
    def __init__(self, contenedor):
        self.contenedor = contenedor
        
        today = date.today()
        self.anio = int(format(today.year))
        self.mes = int(format(today.month))
        
        self.cabecera_calendario()
        self.crear_calendario()
    
    def cabecera_calendario(self):
        meses = ['Enero','Febrero','Marzo','Abril','Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre','Diciembre']
        self.recuadro = ctk.CTkFrame(self.contenedor, width=500, height=600)
        self.recuadro.grid(row=0, column=0, columnspan=7, padx=30, pady=10, sticky="nsew")

        boton_mes_anterior = ctk.CTkButton(self.recuadro, text='<', command=self.mes_anterior, width=20, height=20)
        boton_mes_anterior.pack(side="left", padx=10)
        boton_mes_siguiente = ctk.CTkButton(self.recuadro, text='>', command=self.siguiente_mes, width=20, height=20)
        boton_mes_siguiente.pack(side="right", padx=10)

        self.mes_actual = meses[int(self.mes) - 1]
        self.label_medio = ctk.CTkLabel(self.recuadro, text=f"{self.mes_actual} {self.anio}", width=600)
        self.label_medio.pack(padx=20, pady=10)
    
    def crear_calendario(self):
        row = 2
        col = 0
        cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
        dias_mes = cal.itermonthdays(self.anio, self.mes)
        dias_semana = cal.monthdayscalendar(self.anio, self.mes)

        Dias = ["Dom", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb"]
        
        for i in range(len(Dias)):
            etiqueta_dias = ctk.CTkLabel(self.contenedor, text=Dias[i], font=("Arial", 12))
            etiqueta_dias.grid(row=1, column=i, padx=5, pady=5, sticky="nsew")
        
        for i in range(len(dias_semana)):
            for j in range(len(dias_semana[i])):
                dia = dias_semana[i][j]
                if dia == 0:
                    recuadro = ctk.CTkLabel(self.contenedor, text='', font=("Arial", 12), corner_radius=6)
                else:
                    if j == 3:  # Miércoles
                        boton_clase = ctk.CTkButton(self.contenedor, text=str(dia), font=("Arial", 12), height=80, command=lambda dia=dia: self.inscribir_clase(dia))
                        boton_clase.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                    else:
                        recuadro = ctk.CTkLabel(self.contenedor, text=str(dia), font=("Arial", 12), height=80)
                        recuadro.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                col += 1
                if col > 6:
                    col = 0
                    row += 1

    def inscribir_clase(self, dia):
        # Aquí puedes agregar la lógica para inscribirse en una clase.
        print(f"Te has inscrito en una clase el miércoles {dia}.")

    def mes_anterior(self):
        self.mes -= 1
        if self.mes == 0:
            self.mes = 12
            self.anio -= 1
        self.borrar_calendario()
        self.cabecera_calendario()
        self.crear_calendario()

    def siguiente_mes(self):
        self.mes += 1
        if self.mes == 13:
            self.mes = 1
            self.anio += 1
        self.borrar_calendario()
        self.cabecera_calendario()
        self.crear_calendario()

    def borrar_calendario(self):
        for i in self.contenedor.grid_slaves():
            if int(i.grid_info()["row"]) > 1:
                i.destroy()

def main():
    # Configuración de la ventana principal
    root = Tk()
    root.title("Calendario de Clases")

    # Estilo de customtkinter
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    # Crear un contenedor y añadir el calendario
    contenedor = ctk.CTkFrame(root)
    contenedor.pack(fill="both", expand=True)
    
    calendario = Calendario(contenedor)

    # Ejecutar la ventana
    root.mainloop()

if __name__ == "__main__":
    main()
