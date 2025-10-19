from tkinter import ttk


class Botones:

    def __init__(
        self,
        parent,
        eliminar_callback,
        mostrar_callback,
        limpiar_callback,
        ejecutar_callback
    ):

        self.frame = ttk.Frame(parent)

        self.frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.crear_botones(
            eliminar_callback,
            mostrar_callback,
            limpiar_callback,
            ejecutar_callback
        )

    def crear_botones(
        self,
        eliminar_callback,
        mostrar_callback,
        limpiar_callback,
        ejecutar_callback
    ):

        ttk.Button(
            self.frame,
            text="Eliminar seleccionada",
            command=eliminar_callback
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            self.frame,
            text="Mostrar tareas",
            command=mostrar_callback
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            self.frame,
            text="Limpiar todas",
            command=limpiar_callback
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            self.frame,
            text="EJECUTAR PLANIFICACIÓN",
            command=ejecutar_callback
        ).pack(
            side="right",
            padx=5
        )