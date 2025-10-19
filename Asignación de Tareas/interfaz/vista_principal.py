import tkinter as tk
from tkinter import messagebox

from interfaz.titulo import Titulo
from interfaz.formulario import Formulario
from interfaz.tabla_tareas import TablaTareas
from interfaz.botones import Botones
from interfaz.resultados import TablaResultados
from data.gestor import Gestor

from proceso.planificador import Planificador


class vistaPrincipal:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Planificador de Tareas"
        )

        self.root.geometry(
            "900x600"
        )

        self.gestor = Gestor()

        self.crear_interfaz()

    def crear_interfaz(self):

        self.titulo = Titulo(
            self.root
        )

        self.formulario = Formulario(
            self.root,
            self.agregar_tarea
        )

        self.tabla_tareas = TablaTareas(
            self.root
        )

        self.botones = Botones(
            self.root,
            self.eliminar_tarea,
            self.mostrar_tareas,
            self.limpiar_tareas,
            self.ejecutar_planificacion
        )

        self.resultados = TablaResultados(
            self.root
        )

    def agregar_tarea(self):

        nombre, tiempo_texto = (
            self.formulario.obtener_datos()
        )

        if not nombre:

            messagebox.showwarning(
                "Dato faltante",
                "Ingrese el nombre de la tarea."
            )

            return

        try:

            tiempo = float(tiempo_texto)

        except ValueError:

            messagebox.showerror(
                "Error",
                "El tiempo debe ser un número."
            )

            return

        if tiempo <= 0:

            messagebox.showerror(
                "Error",
                "El tiempo debe ser mayor que cero."
            )

            return

        tarea = self.gestor.agregar_tarea(
            nombre,
            tiempo
        )

        self.tabla_tareas.agregar(
            tarea
        )

        self.formulario.limpiar()

    def eliminar_tarea(self):

        id_tarea = (
            self.tabla_tareas.eliminar_seleccionada()
        )

        if id_tarea is None:

            messagebox.showwarning(
                "Seleccionar tarea",
                "Seleccione una tarea para eliminar."
            )

            return

        self.gestor.eliminar_tarea(
            id_tarea
        )

    def mostrar_tareas(self):

        tareas = self.gestor.obtener_tareas()

        if not tareas:

            messagebox.showinfo(
                "Tareas",
                "No hay tareas registradas."
            )

            return

        texto = "TAREAS REGISTRADAS\n\n"

        for tarea in tareas:

            texto += (
                f"ID: {tarea.id} | "
                f"{tarea.nombre} | "
                f"Tiempo: {tarea.tiempo}\n"
            )

        messagebox.showinfo(
            "Tareas",
            texto
        )

    def limpiar_tareas(self):

        if self.gestor.vacio():
            return

        confirmar = messagebox.askyesno(
            "Confirmar",
            "¿Desea eliminar todas las tareas?"
        )

        if not confirmar:
            return

        self.gestor.limpiar_tareas()

        self.tabla_tareas.limpiar()

        self.resultados.limpiar()

    def ejecutar_planificacion(self):

        tareas = self.gestor.obtener_tareas()

        if not tareas:

            messagebox.showwarning(
                "Sin tareas",
                "Debe registrar al menos una tarea."
            )

            return

        numero_procesadores = (
            self.formulario.obtener_procesadores()
        )

        plan = Planificador(
            numero_procesadores
        )

        resultados = plan.planificar(
            tareas 
        )

        promedio = (
            plan.tiempo_medio_fin(
                resultados
            )
        )

        total = (
            plan.tiempo_total(
                resultados
            )
        )

        self.resultados.mostrar(
            resultados
        )

        self.resultados.mostrar_metricas(
            promedio,
            total
        )