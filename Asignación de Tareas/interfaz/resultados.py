from tkinter import ttk


class TablaResultados:

    def __init__(self, parent):

        self.frame = ttk.LabelFrame(
            parent,
            text="Resultados de la planificación",
            padding=10
        )

        self.frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.crear_tabla()

    def crear_tabla(self):

        columnas = (
            "tarea",
            "procesador",
            "inicio",
            "finalizacion"
        )

        self.tabla = ttk.Treeview(
            self.frame,
            columns=columnas,
            show="headings",
            height=7
        )

        self.tabla.heading(
            "tarea",
            text="Tarea"
        )

        self.tabla.heading(
            "procesador",
            text="Procesador"
        )

        self.tabla.heading(
            "inicio",
            text="Inicio"
        )

        self.tabla.heading(
            "finalizacion",
            text="Finalización"
        )

        for columna in columnas:

            self.tabla.column(
                columna,
                anchor="center",
                width=150
            )

        self.tabla.pack(
            fill="both",
            expand=True
        )

        self.label_promedio = ttk.Label(
            self.frame,
            text="Tiempo medio de finalización: --",
            font=("Arial", 11, "bold")
        )

        self.label_promedio.pack(
            pady=(10, 2)
        )

        self.label_total = ttk.Label(
            self.frame,
            text="Tiempo total de ejecución: --",
            font=("Arial", 11, "bold")
        )

        self.label_total.pack(
            pady=2
        )

    def mostrar(self, resultados):

        self.limpiar()

        for resultado in resultados:

            self.tabla.insert(
                "",
                "end",
                values=(
                    resultado.tarea.nombre,
                    f"P{resultado.procesador}",
                    f"{resultado.inicio:.2f}",
                    f"{resultado.finalizacion:.2f}"
                )
            )

    def mostrar_metricas(self, promedio, total):

        self.label_promedio.config(
            text=(
                f"Tiempo medio de finalización: "
                f"{promedio:.2f}"
            )
        )

        self.label_total.config(
            text=(
                f"Tiempo total de ejecución: "
                f"{total:.2f}"
            )
        )

    def limpiar(self):

        for elemento in self.tabla.get_children():

            self.tabla.delete(elemento)

        self.label_promedio.config(
            text="Tiempo medio de finalización: --"
        )

        self.label_total.config(
            text="Tiempo total de ejecución: --"
        )