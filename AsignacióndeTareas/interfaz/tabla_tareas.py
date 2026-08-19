from tkinter import ttk


class TablaTareas:

    def __init__(self, parent):

        self.frame = ttk.LabelFrame(
            parent,
            text="Tareas registradas",
            padding=10
        )

        self.frame.pack(
            fill="x",
            expand=True,
            padx=20,
            pady=7
        )

        self.crear_tabla()

    def crear_tabla(self):

        columnas = (
            "id",
            "nombre",
            "tiempo"
        )

        self.tabla = ttk.Treeview(
            self.frame,
            columns=columnas,
            show="headings",
            height=4
        )

        self.tabla.heading(
            "id",
            text="ID"
        )

        self.tabla.heading(
            "nombre",
            text="Tarea"
        )

        self.tabla.heading(
            "tiempo",
            text="Tiempo"
        )

        self.tabla.column(
            "id",
            width=80,
            anchor="center"
        )

        self.tabla.column(
            "nombre",
            width=300,
            anchor="center"
        )

        self.tabla.column(
            "tiempo",
            width=150,
            anchor="center"
        )

        self.tabla.pack(
            fill="both",
            expand=True
        )

    def agregar(self, tarea):

        self.tabla.insert(
            "",
            "end",
            iid=str(tarea.id),
            values=(
                tarea.id,
                tarea.nombre,
                tarea.tiempo
            )
        )

    def eliminar_seleccionada(self):

        seleccion = self.tabla.selection()

        if not seleccion:
            return None

        id_tarea = int(
            seleccion[0]
        )

        self.tabla.delete(
            seleccion[0]
        )

        return id_tarea

    def limpiar(self):

        for elemento in self.tabla.get_children():

            self.tabla.delete(elemento)