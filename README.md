# Aplicaciones-de-colas
Planificador de Tareas  Aplicación de escritorio desarrollada en Python que permite registrar y planificar un conjunto de tareas en múltiples procesadores.  El sistema busca distribuir las tareas entre los procesadores disponibles y calcular el tiempo de finalización y el tiempo medio de finalización de las tareas. 


##  Características

-  Registrar tareas.
-  Asignar un tiempo de ejecución a cada tarea.
-  Eliminar tareas individualmente.
-  Eliminar todas las tareas.
-  Visualizar las tareas registradas.
-  Definir el número de procesadores.
-  Planificar automáticamente las tareas.
-  Asignar tareas a los procesadores disponibles.
-  Calcular el tiempo de inicio y finalización.
-  Calcular el tiempo medio de finalización.
-  Mostrar los resultados mediante una interfaz gráfica.

---

## Tecnologías utilizadas

- **Python 3**
- **Tkinter**
- Programación Orientada a Objetos (POO)
- Arquitectura modular

---

## Estructura del proyecto

```text
planificador-tareas/
│
├── main.py
│
├── modelos/
│   ├── __init__.py
│   └── tarea.py
│
├── servicios/
│   ├── __init__.py
│   └── gestor_tareas.py
│
├── logica/
│   ├── __init__.py
│   └── planificador.py
│
└── interfaz/
    ├── __init__.py
    ├── vista_principal.py
    ├── titulo.py
    ├── formulario_tarea.py
    ├── tabla_tareas.py
    ├── botones.py
    └── resultados.py
```

## Instalación
1. Requisitos

Se necesita tener instalado:

-Python 3.10 o superior
-Tkinter

En Windows, Tkinter normalmente viene incluido con la instalación oficial de Python.
Puedes comprobar que Tkinter está disponible ejecutando:
```text
python -m tkinter
```
Si aparece una ventana de prueba de Tkinter, está correctamente instalado.

2. Clonar el repositorio

Clona el proyecto desde GitHub:
```text
git clone https://github.com/TU-USUARIO/planificador-tareas.git
```
Entra en la carpeta:

cd planificador-tareas
3. Ejecutar el programa

Ejecuta:
```text
python main.py
```

La aplicación gráfica se abrirá automáticamente.
