import customtkinter as ctk
from tkinter import messagebox, Listbox, END
from datetime import date
import calendar

class Clases:
    def __init__(self, ventana) -> None:
        self.ventana = ventana
        self.cupo_max = 15
        self.fecha = date.today()
        self.mes = int(format(self.fecha.month))
        self.anio = int(format(self.fecha.year))
        basura, self.cant_dias = calendar.monthrange(self.anio, self.mes)
        
        self.crear_clase()

    def crear_clase(self):
        self.clases = ['Funcional', 'Crossfit', 'Zumba', 'Calistenia', 'Boxeo']
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

        # Contenedor principal
        contenedor = ctk.CTkFrame(self.ventana, corner_radius=10, fg_color="transparent")
        contenedor.pack(padx=20, pady=120)

        titulo = ctk.CTkLabel(contenedor, text="CREAR CLASE", font=("Arial", 20, "bold"), text_color="#00aaff")
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Seleccionar el mes
        self.mes_var = ctk.StringVar(value=meses[self.mes - 1])
        mes_etiqueta = ctk.CTkLabel(contenedor, text="Selecciona el Mes:", text_color="white")
        mes_etiqueta.grid(row=1, column=0, padx=20, pady=5, sticky="e")
        mes_menu = ctk.CTkOptionMenu(contenedor, variable=self.mes_var, values=meses, width=150)
        mes_menu.grid(row=1, column=1, padx=20, pady=5, sticky="w")

        # Seleccionar el día
        self.dia = ctk.StringVar(value="1")
        dia_label = ctk.CTkLabel(contenedor, text="Selecciona el Día:", text_color="white")
        dia_label.grid(row=2, column=0, padx=20, pady=5, sticky="e")
        dia_menu = ctk.CTkOptionMenu(contenedor, variable=self.dia, values=[str(i + 1) for i in range(self.cant_dias)], width=150)
        dia_menu.grid(row=2, column=1, padx=20, pady=5, sticky="w")

        # Seleccionar tipo de clase
        self.tipo = ctk.StringVar(value="Elegir clase")
        tipo_clase = ctk.CTkLabel(contenedor, text="Tipo de la Clase:", text_color="white")
        tipo_clase.grid(row=3, column=0, padx=20, pady=5, sticky="e")
        tipo_clase_menu = ctk.CTkOptionMenu(contenedor, variable=self.tipo, values=self.clases, width=150)
        tipo_clase_menu.grid(row=3, column=1, padx=20, pady=5, sticky="w")

        # Definir cupo máximo
        self.cupo = ctk.StringVar(value="1")
        cupo_label = ctk.CTkLabel(contenedor, text="Cupo Máximo:", text_color="white")
        cupo_label.grid(row=4, column=0, padx=20, pady=5, sticky="e")
        cupo_max_menu = ctk.CTkOptionMenu(contenedor, variable=self.cupo, values=[str(i + 1) for i in range(self.cupo_max)], width=150)
        cupo_max_menu.grid(row=4, column=1, padx=20, pady=5, sticky="w")

        # Botón de guardar
        guardar = ctk.CTkButton(contenedor, text="Guardar Clase", command=self.guardar_clase, width=150)
        guardar.grid(row=5, column=0, columnspan=2, pady=20)

        # Botón para mostrar inscritos
        mostrar_inscritos = ctk.CTkButton(contenedor, text="Mostrar Inscritos", command=self.mostrar_inscritos, width=150)
        mostrar_inscritos.grid(row=6, column=0, columnspan=2, pady=10)

        #Boton modificar clase
        modificar_clases = ctk.CTkButton(contenedor, text="Modificar Clases", command=self.modificar_clase, width=150)
        modificar_clases.grid(row=7, column=0, columnspan=2, pady=20)
    
    def modificar_clase(self):
        self.cargar_clases()

    def mostrar_clases(self):
        # Si ya hay una ventana abierta, la cerramos antes de abrir otra
        if hasattr(self, 'ventana_clases') and self.ventana_clases.winfo_exists():
            self.ventana_clases.destroy()

        self.ventana_clases = ctk.CTkToplevel(self.ventana)
        self.ventana_clases.geometry('550x500')
        self.ventana_clases.title("Gestión de Clases")

        row_num = 0
        col_num = 0

        for tipo, clases in self.clases_por_tipo.items():  # Cambiar 'self.clases' por 'clases'
            frame = ctk.CTkFrame(self.ventana_clases, width=180, height=200)
            frame.grid(row=row_num, column=col_num, padx=10, pady=10)

            label_tipo = ctk.CTkLabel(frame, text=tipo, font=("Arial", 14, "bold"))
            label_tipo.pack(pady=5)

            lista_clases = Listbox(frame, height=5)
            lista_clases.pack(padx=10, pady=5)

            for clase in clases:
                lista_clases.insert(END, clase)

            # Botón para eliminar clase
            eliminar_boton = ctk.CTkButton(frame, text="Eliminar Clase", command=lambda lista=lista_clases: self.eliminar_clase(lista))
            eliminar_boton.pack(pady=5)

            # Botón para cambiar cupo máximo
            cambiar_boton = ctk.CTkButton(frame, text="Cambiar Cupo", command=lambda lista=lista_clases: self.cambiar_cupo(lista))
            cambiar_boton.pack(pady=5)

            col_num += 1
            if col_num == 3:  # Máximo 3 columnas
                col_num = 0
                row_num += 1

    def eliminar_clase(self, lista_clases):
        seleccionada = lista_clases.curselection()
        if seleccionada:  # Solo proceder si hay una selección
            clase = lista_clases.get(seleccionada)
            confirmacion = messagebox.askyesno("Confirmar", f"¿Estás seguro de que quieres eliminar la clase '{clase}'?")
            if confirmacion:
                self.remover_clase_del_archivo(clase)  # Eliminar de archivo
                lista_clases.delete(seleccionada)  # Eliminar de la lista visual
                messagebox.showinfo("Éxito", "Clase eliminada correctamente.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una clase para eliminar.")

    def remover_clase_del_archivo(self, clase_a_eliminar):
        archivo_ruta = 'Archivos_admi/clases.txt'
        
        lineas_a_conservar = []
        
        with open(archivo_ruta, 'r') as archivo:
            for linea in archivo:
                if clase_a_eliminar not in linea:
                    lineas_a_conservar.append(linea)
        
        with open(archivo_ruta, 'w') as archivo:
            for linea in lineas_a_conservar:
                archivo.write(linea)
        
        self.cargar_clases()  # Recarga la lista de clases en la ventana activa

    def cargar_clases(self):
        self.clases_por_tipo = {tipo: [] for tipo in self.clases}

        archivo_ruta = 'Archivos_admi/clases.txt'
        with open(archivo_ruta, 'r') as archivo:
            for linea in archivo:
                partes = linea.strip().split(" - ")
                if len(partes) == 3:
                    tipo_clase = partes[0].replace("Clase: ", "")
                    dia = partes[1].replace("Dia: ", "")
                    cupo = partes[2].replace("Cupo Maximo: ", "")
                    if tipo_clase in self.clases_por_tipo:  # Verificar si el tipo de clase es válido
                        self.clases_por_tipo[tipo_clase].append(f"{dia} - {cupo}")
        self.mostrar_clases()  # Muestra las clases actualizadas


    def cambiar_cupo(self, lista_clases):
        seleccionada = lista_clases.curselection()
        if seleccionada:
            clase = lista_clases.get(seleccionada)
            nuevo_cupo = ctk.CTkEntry(self.ventana_clases)
            nuevo_cupo.pack(pady=10)

            def guardar_cupo():
                nuevo_cupo_valor = nuevo_cupo.get()
                self.actualizar_cupo(clase, nuevo_cupo_valor)
                nuevo_cupo.delete(0, END)

            guardar_boton = ctk.CTkButton(self.ventana_clases, text="Guardar Cupo", command=guardar_cupo)
            guardar_boton.pack(pady=5)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una clase para cambiar el cupo.")
        
    def guardar_clase(self):
        clase_seleccionada = self.tipo.get()
        dia_seleccionado = self.dia.get()
        mes_seleccionado = self.mes_var.get()

        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        mes_numero = meses.index(mes_seleccionado) + 1
        fecha_clase = f"{int(dia_seleccionado):02d}/{mes_numero:02d}/2024"  # El :02d -> Convierte el dia con dos digios, ejemplo 1/2/2024 -> 01/02/2024

        archivo_ruta = 'Archivos_admi/clases.txt'
        
        clase_existe = False
        with open(archivo_ruta, 'r') as archivo:
            for linea in archivo:
                if f"Clase: {clase_seleccionada}" in linea and f"Dia: {fecha_clase}" in linea:
                    clase_existe = True
                    break
        if clase_existe:
            messagebox.showerror("Error", f"Ya existe la clase en el día {fecha_clase}")
        else:
            with open(archivo_ruta, 'a') as archivo:
                archivo.write(f"Clase: {clase_seleccionada} - Dia: {fecha_clase} - Cupo Maximo: {self.cupo.get()}\n")
            messagebox.showinfo("Éxito", f"Se agregó la clase correctamente")

    def mostrar_inscritos(self):
        mes_seleccionado = self.mes_var.get()
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        mes_numero = meses.index(mes_seleccionado) + 1

        archivo_ruta = 'Archivos_admi/inscripciones.txt'

        inscritos_por_clase = {}
        with open(archivo_ruta, 'r') as archivo:
            for linea in archivo:
                partes = linea.strip().split(" - ")
                if len(partes) == 3:
                    nombre = partes[0].replace("Nombre: ", "")
                    clase = partes[1].replace("Clase: ", "")
                    dia = partes[2].replace("Dia: ", "")
                    mes_clase = int(dia.split('/')[1])
                    
                    if mes_clase == mes_numero:
                        if clase not in inscritos_por_clase:
                            inscritos_por_clase[clase] = []
                        inscritos_por_clase[clase].append((nombre, dia))

        if not inscritos_por_clase:
            messagebox.showinfo("Información", f"No hay inscritos para el mes de {mes_seleccionado}.")
            return
        
        self.ventana_inscritos = ctk.CTkToplevel(self.ventana)
        self.ventana_inscritos.geometry('600x400')
        self.ventana_inscritos.title(f"Inscritos para {mes_seleccionado}")

        self.inscritos_por_clase = inscritos_por_clase
        self.crear_columnas_inscritos()

    def crear_columnas_inscritos(self):
        # Mostrar inscritos en 3 columnas
        row_num = 0
        col_num = 0

        for clase, inscritos in self.inscritos_por_clase.items():
            label_clase = ctk.CTkLabel(self.ventana_inscritos, text=clase, font=("Arial", 14, "bold"))
            label_clase.grid(row=row_num, column=col_num, padx=10, pady=5)

            lista_inscritos = Listbox(self.ventana_inscritos, height=5, width=30)
            lista_inscritos.grid(row=row_num + 1, column=col_num, padx=10, pady=5)

            for inscrito in inscritos:
                lista_inscritos.insert(END, f"{inscrito[0]} - {inscrito[1]}")

            eliminar_boton = ctk.CTkButton(self.ventana_inscritos, text="Eliminar", command=lambda clase=clase, lista_inscritos=lista_inscritos: self.eliminar_inscrito(clase, lista_inscritos))
            eliminar_boton.grid(row=row_num + 2, column=col_num, padx=10, pady=5)

            col_num += 1
            if col_num == 3:  # Máximo 3 columnas
                col_num = 0
                row_num += 3

    def eliminar_inscrito(self, clase_seleccionada, lista_inscritos):
        seleccionado = lista_inscritos.get(lista_inscritos.curselection())
        nombre_inscrito = seleccionado.split(" - ")[0]
        fecha_inscripcion = seleccionado.split(" - ")[1]

        archivo_ruta = 'Archivos_admi/inscripciones.txt'

        with open(archivo_ruta, 'r') as archivo:
            lineas = archivo.readlines()

        with open(archivo_ruta, 'w') as archivo:
            for linea in lineas:
                if f"Nombre: {nombre_inscrito}" not in linea or f"Dia: {fecha_inscripcion}" not in linea or f"Clase: {clase_seleccionada}" not in linea:
                    archivo.write(linea)

        messagebox.showinfo("Éxito", f"Se eliminó a {nombre_inscrito} de la clase {clase_seleccionada}.")
        
        # Refrescar la ventana de inscritos
        lista_inscritos.delete(0, END)
        self.mostrar_inscritos()
