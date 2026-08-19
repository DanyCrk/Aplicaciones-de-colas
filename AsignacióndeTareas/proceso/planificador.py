from dataclasses import dataclass
@dataclass

class ResultadoTarea:
    tarea: object
    procesador: int
    inicio: float
    finalizacion: float
    
class Planificador:
    def __init__(self, num_procesadores):
        self.num_procesadores = num_procesadores
    def planificar(self, tareas):
        if not tareas:
            return []
        tareas_ordenadas = sorted(tareas, key=lambda t: t.tiempo)
        
        tiempos=[0.0
                  for _ in range(self.num_procesadores)]
        resultados=[]
        for tarea in tareas_ordenadas:
            indice= tiempos.index(min(tiempos))
            inicio= tiempos[indice]
            finalizacion= inicio + tarea.tiempo
            tiempos[indice]= finalizacion
            
            resultado= ResultadoTarea(tarea=tarea, procesador=indice +1 , inicio=inicio, finalizacion=finalizacion)
            resultados.append(resultado)
        return resultados
    def tiempo_medio_fin(self, resultados):
        if not resultados:
            return 0.0
        total_fin= sum(resultado.finalizacion for resultado in resultados)
        return total_fin / len(resultados)
    def tiempo_total(self, resultados):
        if not resultados:
            return 0.0
        return max(resultado.finalizacion for resultado in resultados)
    
    