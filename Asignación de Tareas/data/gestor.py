from modelo.tarea import Tarea

class Gestor:
    def __init__(self):
        self.tareas = []
        self.siguiente_id = 1

    def agregar_tarea(self, nombre, tiempo):
        tarea = Tarea(self.siguiente_id, nombre=nombre, tiempo=tiempo)
        
        self.tareas.append(tarea)
        self.siguiente_id += 1
        return tarea

    def eliminar_tarea(self, id_tarea):
        self.tareas = [tarea for tarea in
                       self.tareas if tarea.id != id_tarea]
        
    def obtener_tareas(self):
        return self.tareas.copy()
    
    def limpiar_tareas(self):
        self.tareas.clear()
        self.siguiente_id = 1
    def vacio(self):
        return len(self.tareas) == 0
    
    