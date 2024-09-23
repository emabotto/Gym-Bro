import random
from datetime import datetime, timedelta

# Listas de clases y otros parámetros
tipos_de_clases = ['Funcional', 'Crossfit', 'Zumba', 'Calistenia', 'Boxeo']
cupos_maximos = list(range(1, 16))  # Cupos entre 1 y 15

def crear_clase_aleatoria():
    # Generar una fecha aleatoria
    hoy = datetime.now()
    fecha_clase = hoy + timedelta(days=random.randint(1, 30))  # Fecha dentro de los próximos 30 días
    dia = fecha_clase.day
    mes = fecha_clase.month
    anio = fecha_clase.year

    # Seleccionar aleatoriamente una clase y un cupo
    tipo_clase = random.choice(tipos_de_clases)
    cupo = random.choice(cupos_maximos)

    # Crear el texto de la clase
    clase_info = f"Clase: {tipo_clase} - Día: {dia}/{mes}/{anio} - Cupo Máximo: {cupo}\n"
    return clase_info

def guardar_clase_en_txt(clase_info, archivo="clases_aleatorias.txt"):
    with open(archivo, "a") as file:
        file.write(clase_info)

# Crear y guardar 10 clases aleatorias
for _ in range(10):
    clase = crear_clase_aleatoria()
    guardar_clase_en_txt(clase)
    print(f"Clase creada y guardada: {clase}")
