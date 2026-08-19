from dataclasses import dataclass


@dataclass
class Tarea:
    id: int
    nombre: str
    tiempo: float