import customtkinter as ctk
from tkinter import Tk, messagebox, Listbox, END, ttk

class Inscripciones:
    def __init__(self, dia, mes, anio, contenedor, usuario) -> None:
        self.ventana_secundaria = ctk.CTkToplevel(contenedor)
        self.ventana_secundaria.geometry('600x400')
        self.ventana_secundaria.title(f'Inscripción para el Día {dia}/{mes}')
        self.ventana_secundaria.configure(bg="#2C3E50")  # Fondo de ventana
        self.ventana_secundaria.grab_set()
        
        self.usuario = usuario
        self.dia = dia
        self.mes = mes
        self.anio = anio

        self.clases_disponibles = self.cargar_clases_disponibles()
        self.crear_titulo()
        if not self.clases_disponibles:
            messagebox.showerror("Error", "No se encontraron clases para este dia")
        else:
            self.inscripciones = self.cargar_inscripciones()
            self.tab_labels = {}  # Almacena las etiquetas de cupos
            self.lista_inscritos_widgets = {}  # Almacena las listas de inscritos
            self.crear_pestanias()

    def cargar_clases_disponibles(self):
        clases_filtradas = {}
        seleccion = f'{str(self.dia).zfill(2)}/{str(self.mes).zfill(2)}/{self.anio}'
        try:
            with open("Archivos_admi/clases.txt", "r") as archivo:
                lineas = archivo.readlines()
                fecha_buscada = seleccion
                for linea in lineas:
                    partes = linea.strip().split(" - ")
                    clase = partes[0].replace("Clase: ", "")
                    fecha = partes[1].replace("Dia: ", "")
                    cupo_maximo = int(partes[2].replace("Cupo Maximo: ", "").strip())
                    if fecha == fecha_buscada:
                        clases_filtradas[clase] = cupo_maximo
        except FileNotFoundError:
            messagebox.showwarning("Error", "No se encontró el archivo de clases.")
        
        return clases_filtradas

    def cargar_inscripciones(self):
        inscripciones = {}
        seleccion = f'{str(self.dia).zfill(2)}/{str(self.mes).zfill(2)}/{self.anio}'
        try:
            with open("Archivos_admi/inscripciones.txt", "r") as archivo:
                lineas = archivo.readlines()
                for linea in lineas:
                    datos = linea.strip().split(" - ")
                    if len(datos) == 3:
                        clase = datos[1].replace("Clase: ", "")
                        nombre = datos[0].replace("Nombre: ", "")
                        fecha = datos[2].replace("Dia: ", "")
                        if fecha == seleccion:
                            if clase not in inscripciones:
                                inscripciones[clase] = []
                            inscripciones[clase].append(nombre)
        except FileNotFoundError:
            messagebox.showwarning("Error", "No se encontró el archivo de inscripciones.")
        
        return inscripciones

    def crear_titulo(self):
        titulo = ctk.CTkLabel(self.ventana_secundaria, text="Inscripción a Clases", font=("Arial", 15, "bold"), text_color="#ECF0F1")
        titulo.pack(pady=(20, 10))

    def crear_pestanias(self):
        self.tab_control = ttk.Notebook(self.ventana_secundaria, style='TNotebook')
        self.tab_control.pack(expand=1, fill='both')

        # Estilo de las pestañas
        style = ttk.Style()
        style.configure('TNotebook', background="#2C3E50", bordercolor="black", borderwidth=2, relief='solid')
        style.configure('TNotebook.Tab', background="#34495E", foreground="white", padding=[10, 5])
        style.map('TNotebook.Tab', background=[('active', '#1ABC9C'), ('!active', '#34495E')],
                  foreground=[('active', 'blue'), ('!active', 'black')])

        for clase in self.clases_disponibles.keys():
            tab = ctk.CTkFrame(self.tab_control, fg_color="#2C3E50")  # Cambiado bg a fg_color
            self.tab_control.add(tab, text=clase)

            # Mostrar información en la pestaña
            cupo_maximo = self.clases_disponibles[clase]
            inscritos = self.inscripciones.get(clase, [])
            cupos_restantes = cupo_maximo - len(inscritos)

            label_cupos = ctk.CTkLabel(tab, text=f"Cupos disponibles: {cupos_restantes}", font=("Arial", 12), text_color="#ECF0F1")
            label_cupos.pack(pady=5)

            label_inscritos = ctk.CTkLabel(tab, text="Personas inscritas:", font=("Arial", 12), text_color="#ECF0F1")
            label_inscritos.pack(pady=5)

            lista_inscritos = Listbox(tab, height=5, width=40, bg="#34495E", fg="white", selectbackground="#1ABC9C")
            lista_inscritos.pack(pady=5)

            for inscrito in inscritos:
                lista_inscritos.insert(END, inscrito)
            
            self.tab_labels[clase] = label_cupos
            self.lista_inscritos_widgets[clase] = lista_inscritos
            
            # Botón para inscribirse
            boton_inscribirse = ctk.CTkButton(tab, text="Inscribirse", command=lambda c=clase: self.guardar_inscripcion(c))
            boton_inscribirse.pack(pady=10)

    def guardar_inscripcion(self, clase_seleccionada):
        
        if clase_seleccionada and (clase_seleccionada not in self.inscripciones or len(self.inscripciones[clase_seleccionada]) < self.clases_disponibles[clase_seleccionada]) and self.usuario not in self.inscripciones[clase_seleccionada]:
            with open("Archivos_admi/inscripciones.txt", "a") as archivo:
                archivo.write(f"Nombre: {self.usuario} - Clase: {clase_seleccionada} - Dia: {self.dia}/{self.mes}/{self.anio}\n")
            messagebox.showinfo("Éxito", f"Inscripción guardada para {clase_seleccionada}.")
           
            if clase_seleccionada not in self.inscripciones:
                self.inscripciones[clase_seleccionada] = []
            self.inscripciones[clase_seleccionada].append(self.usuario)
            
            self.actualizar_pestania(clase_seleccionada)  
        else:
            if self.usuario in self.inscripciones[clase_seleccionada]:
                messagebox.showwarning("Error", "Ya te encuentras registrado")
            else:
                messagebox.showwarning("Error", "No hay cupos disponibles o la clase no está seleccionada.")
    
    def actualizar_pestania(self, clase_seleccionada):
        cupo_maximo = self.clases_disponibles[clase_seleccionada]
        inscritos = self.inscripciones.get(clase_seleccionada, [])
        cupos_restantes = cupo_maximo - len(inscritos)

        # Actualiza la etiqueta de cupos
        self.tab_labels[clase_seleccionada].configure(text=f"Cupos disponibles: {cupos_restantes}")

        # Limpia y actualiza la lista de inscritos
        lista_inscritos = self.lista_inscritos_widgets[clase_seleccionada]
        lista_inscritos.delete(0, END)  # Limpia la lista
        for inscrito in inscritos:
            lista_inscritos.insert(END, inscrito)