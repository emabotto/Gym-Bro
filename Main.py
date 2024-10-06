from Pantallas.Inicio_Secicion import VentanaIniciarSecion
from BaseDeDatos.Usuario import Usuario
from BaseDeDatos.Datos import Leer_Datos_Guardados

if __name__ == "__main__":
    Leer_Datos_Guardados()
    
    inicio = VentanaIniciarSecion()
    inicio.Abrir_ventana()
    inicio.mostrar()
    