import tkinter as tk
from tkinter import ttk


class Titulo:

    def __init__(self, parent):

        self.frame = ttk.Frame(parent)

        self.frame.pack(
            fill="x",
            pady=(20, 10)
        )

        self.crear_titulo()

    def crear_titulo(self):

        titulo = ttk.Label(
            self.frame,
            text="PLANIFICADOR DE TAREAS",
            font=("Arial", 22, "bold")
        )

        titulo.pack()

        subtitulo = ttk.Label(
            self.frame,
            text="Planificación de tareas en múltiples procesadores"
        )

        subtitulo.pack(
            pady=(5, 0)
        )