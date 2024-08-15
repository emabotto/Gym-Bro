import tkinter as tk
import customtkinter as ctk

def Cargar_Rutina():
    with open('Rutina.txt', 'r') as archivo:
        for linea in archivo:
            linea = linea.strip().replace("\\r", "").replace("\n", "").replace("'", "")
            rutina = linea.split(',')
            