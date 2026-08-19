import tkinter as tk
from tkinter import ttk


class Formulario:

    def __init__(self, parent, agregar_callback):

        self.agregar_callback = agregar_callback

        self.frame = ttk.LabelFrame(
            parent,
            text="Registrar tarea",
            padding=15
        )

        self.frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.crear_formulario()

    def crear_formulario(self):
        ttk.Label(
            self.frame,
            text="Nombre de la tarea:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        self.entry_nombre = ttk.Entry(
            self.frame,
            width=25
        )

        self.entry_nombre.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            self.frame,
            text="Tiempo de ejecución:"
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=5
        )

        self.entry_tiempo = ttk.Entry(
            self.frame,
            width=15
        )

        self.entry_tiempo.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )

        ttk.Button(
            self.frame,
            text="Agregar tarea",
            command=self.agregar_callback
        ).grid(
            row=0,
            column=4,
            padx=15
        )

        ttk.Label(
            self.frame,
            text="Número de procesadores:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=(15, 5)
        )

        self.spin_procesadores = ttk.Spinbox(
            self.frame,
            from_=1,
            to=100,
            width=10
        )

        self.spin_procesadores.set(2)

        self.spin_procesadores.grid(
            row=1,
            column=1,
            padx=5,
            pady=(15, 5),
            sticky="w"
        )

    def obtener_datos(self):

        return (
            self.entry_nombre.get().strip(),
            self.entry_tiempo.get().strip()
        )

    def obtener_procesadores(self):

        return int(
            self.spin_procesadores.get()
        )

    def limpiar(self):

        self.entry_nombre.delete(
            0,
            tk.END
        )

        self.entry_tiempo.delete(
            0,
            tk.END
        )

        self.entry_nombre.focus()