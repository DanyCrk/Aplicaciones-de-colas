# Aplicaciones-de-colas

## Planificador de Tareas

Aplicación web desarrollada en **Python y Flask** que permite registrar y planificar un conjunto de tareas en múltiples procesadores.

El sistema busca distribuir las tareas entre los procesadores disponibles y calcular el tiempo de inicio, tiempo de finalización, tiempo medio de finalización y tiempo total de ejecución.

La aplicación cuenta con una interfaz web desarrollada utilizando **HTML, CSS y JavaScript**, mientras que la lógica de procesamiento se mantiene implementada en Python.

---

## Características

- Registrar tareas.
- Asignar un tiempo de ejecución a cada tarea.
- Eliminar tareas individualmente.
- Eliminar todas las tareas.
- Visualizar las tareas registradas.
- Definir el número de procesadores.
- Planificar automáticamente las tareas.
- Distribuir las tareas entre los procesadores disponibles.
- Calcular el tiempo de inicio de cada tarea.
- Calcular el tiempo de finalización de cada tarea.
- Calcular el tiempo medio de finalización.
- Calcular el tiempo total de planificación.
- Visualizar los resultados mediante una interfaz web.
- Verificar cadenas balanceadas utilizando una estructura de datos tipo pila.
- Mostrar los resultados del algoritmo de balanceo directamente en la interfaz web.

---

## Tecnologías utilizadas

### Backend

- **Python 3**
- **Flask**
- Programación Orientada a Objetos (POO)
- Arquitectura modular

### Frontend

- **HTML5**
- **CSS3**
- **JavaScript**

### Algoritmos y estructuras de datos

- Planificación de tareas en múltiples procesadores.
- Ordenamiento de tareas por tiempo de ejecución.
- Asignación de tareas al procesador disponible.
- Cálculo de tiempos de finalización.
- Cálculo del tiempo medio de finalización.
- Estructura de datos **Pila (Stack)** para verificar cadenas balanceadas.

---

## Estructura del proyecto

```text
AsignacióndeTareas/
│
├── main.py
│
├── data/
│   ├── __init__.py
│   └── gestor.py
│
├── modelo/
│   ├── __init__.py
│   └── ...
│
├── proceso/
│   ├── __init__.py
│   ├── planificador.py
│   └── balanceo.py
│
├── interfaz/
│   ├── __init__.py
│   └── ...
│
└── web/
    ├── __init__.py
    ├── app.py
    │
    ├── templates/
    │   └── index.html
    │
    └── static/
        ├── css/
        │   └── estilos.css
        │
        └── js/
            └── app.js
```
Instalación
## Requisitos

Se necesita tener instalado:

Python 3.10 o superior
Flask

Si Flask todavía no está instalado:
```text 
python -m pip install flask

```
verificar la instalación:
```text 
python -m flask --version
```

## Clonar el repositorio

Clona el proyecto desde GitHub:
```text 
git clone https://github.com/TU-USUARIO/planificador-tareas.git
```


Entra en la carpeta:

cd planificador-tareas

## Ejecución de la aplicación

Es importante ejecutar Flask desde la carpeta raíz del proyecto.

```text 
python -m web.app

```
## Abrir la aplicación

Después de ejecutar el comando anterior Flask mostrará algo similar a:

* Serving Flask app 'web.app'
* Debug mode: on
* Running on http://127.0.0.1:5000

Abre el siguiente enlace en tu navegador:

http://127.0.0.1:5000
