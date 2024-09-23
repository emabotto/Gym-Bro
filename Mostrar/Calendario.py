import customtkinter as ctk
from datetime import date
import calendar
from Archivos_admi.Admin_Inscripciones import Inscripciones
class Calendario:
    def __init__(self,contenedor):
        self.contenedor = contenedor
        
        today = date.today()
        self.anio = int(format(today.year))
        self.mes = int(format(today.month))
        
        self.cabecera_calendario()
        self.crear_calendario()
    
    def cabecera_calendario(self): #Cabecera de calendario
        meses = ['Enero','Febrero','Marzo','Abril','Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre','Diciembre']
        self.recuadro = ctk.CTkFrame(self.contenedor,width=500, height=600)
        self.recuadro.grid(row=0, column=0, columnspan=7,padx=30, pady=10, sticky="nsew")

        boton_mes_anterior = ctk.CTkButton(self.recuadro, text='<',command=self.mes_anterior,width=20, height=20)
        boton_mes_anterior.pack(side="left", padx=10)
        boton_mes_siguiente = ctk.CTkButton(self.recuadro, text='>',command=self.siguiente_mes,width=20, height=20)
        boton_mes_siguiente.pack(side="right", padx=10)

        self.mes_actual = meses [int(self.mes)-1]
        self.label_medio = ctk.CTkLabel(self.recuadro,text=(self.mes_actual, self.anio),width= 600)
        self.label_medio.pack(padx = 20, pady=10)
    
    def crear_calendario(self): #Crea los dias con sus botones
        row = 2
        col = 0
        cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
        dias_mes = cal.itermonthdays(self.anio,self.mes)

        Dias = ["Dom", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb"]
        for i in range(len(Dias)):
            etiqueta_dias = ctk.CTkLabel(self.contenedor,text = Dias[i], font=("Arial", 12))
            etiqueta_dias.grid(row=1, column=0+i, padx=5, pady=5, sticky="nsew")
        
        for i in dias_mes:
            if i != 0: 
                contenedor1 = ctk.CTkFrame(self.contenedor, corner_radius=6)
                contenedor1.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")  
                if col == 0: #Los domingos esta cerrado asi que no se pueden inscribir 
                    etiqueta_domingo = ctk.CTkLabel(contenedor1,text = i,font=("Arial", 12), height=80, width= 20)
                    etiqueta_domingo.pack(side="top",fill="x",padx=5, pady=5) 
                else:
                    boton_inscripcion = ctk.CTkButton(contenedor1, text=i, font=("Arial", 12), height=80, width= 20, command=lambda dia=i: self.inscribirse_a_clase(dia))
                    boton_inscripcion.pack(side="top",fill="x",padx=5, pady=5) 
            col += 1
            if col > 6:
                col = 0
                row += 1

    def inscribirse_a_clase(self, dia):
        ventana_inscripciones = Inscripciones(dia,self.mes,self.anio,self.contenedor)
        
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
            if int(i.grid_info()["row"])> 1:
                i.destroy()



