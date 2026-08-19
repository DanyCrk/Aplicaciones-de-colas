from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from data.gestor import Gestor
from proceso.planificador import Planificador
from proceso.balanceo import balanceado


app = Flask(__name__)


app.secret_key = "planificador-tareas-clave"

gestor = Gestor()

CASOS_PRUEBA = [
    "[()]",
    "([)]",
    "[(])",
    "([[]])",
    "(()",
    ")("
]
@app.route("/")
@app.route("/")
def inicio():

    tareas = gestor.obtener_tareas()

    resultados_balanceo = []

    for caso in CASOS_PRUEBA:

        resultado, mensaje = balanceado(
            caso,
            mostrar_pasos=False
        )

        resultados_balanceo.append({
            "cadena": caso,
            "balanceada": resultado,
            "mensaje": mensaje
        })

    return render_template(
        "index.html",
        tareas=tareas,
        resultados=None,
        promedio=None,
        total=None,
        
        resultados_balanceo=obtener_resultados_balanceo()
    )
def obtener_resultados_balanceo():

    resultados = []

    for caso in CASOS_PRUEBA:

        resultado, mensaje = balanceado(
            caso,
            mostrar_pasos=False
        )

        resultados.append({
            "cadena": caso,
            "balanceada": resultado,
            "mensaje": mensaje
        })

    return resultados

@app.route("/agregar", methods=["POST"])
def agregar():

    nombre = request.form.get(
        "nombre",
        ""
    ).strip()

    tiempo_texto = request.form.get(
        "tiempo",
        ""
    ).strip()

    if not nombre:

        flash(
            "Debe ingresar el nombre de la tarea.",
            "error"
        )

        return redirect(
            url_for("inicio")
        )

    try:

        tiempo = float(tiempo_texto)

    except ValueError:

        flash(
            "El tiempo debe ser un número.",
            "error"
        )

        return redirect(
            url_for("inicio")
        )

    if tiempo <= 0:

        flash(
            "El tiempo debe ser mayor que cero.",
            "error"
        )

        return redirect(
            url_for("inicio")
        )

    gestor.agregar_tarea(
        nombre,
        tiempo
    )

    flash(
        f"Tarea '{nombre}' agregada correctamente.",
        "success"
    )

    return redirect(
        url_for("inicio")
    )


@app.route("/eliminar/<int:id_tarea>", methods=["POST"])
def eliminar(id_tarea):

    gestor.eliminar_tarea(
        id_tarea
    )

    flash(
        "Tarea eliminada correctamente.",
        "success"
    )

    return redirect(
        url_for("inicio")
    )

@app.route("/limpiar", methods=["POST"])
def limpiar():

    gestor.limpiar_tareas()

    flash(
        "Todas las tareas fueron eliminadas.",
        "success"
    )

    return redirect(
        url_for("inicio")
    )


@app.route("/planificar", methods=["POST"])
def planificar():

    tareas = gestor.obtener_tareas()

    if not tareas:

        flash(
            "Debe registrar al menos una tarea.",
            "error"
        )

        return redirect(
            url_for("inicio")
        )

    procesadores_texto = request.form.get(
        "procesadores",
        ""
    ).strip()

    try:

        numero_procesadores = int(
            procesadores_texto
        )

    except ValueError:

        flash(
            "El número de procesadores debe ser entero.",
            "error"
        )

        return redirect(
            url_for("inicio")
        )

    if numero_procesadores <= 0:

        flash(
            "Debe existir al menos un procesador.",
            "error"
        )

        return redirect(
            url_for("inicio")
        )

    planificador = Planificador(
        numero_procesadores
    )

    resultados = planificador.planificar(
        tareas
    )

    promedio = (
        planificador.tiempo_medio_fin(
            resultados
        )
    )

    total = (
        planificador.tiempo_total(
            resultados
        )
    )

    return render_template(
    "index.html",
    tareas=tareas,
    resultados=resultados,
    promedio=promedio,
    total=total,
    procesadores=numero_procesadores,
    resultados_balanceo=obtener_resultados_balanceo()
)

@app.route("/balancear", methods=["POST"])
def balancear():

    cadena = request.form.get(
        "cadena",
        ""
    )

    if not cadena.strip():

        flash(
            "Debe ingresar una cadena.",
            "error"
        )

        return redirect(
            url_for("inicio")
        )

    resultado, mensaje = balanceado(
        cadena,
        mostrar_pasos=False
    )

    return render_template(
        "index.html",
        tareas=gestor.obtener_todas(),
        resultados=None,
        promedio=None,
        total=None,
        cadena_balanceo=cadena,
        resultado_balanceo=resultado,
        mensaje_balanceo=mensaje
    )

if __name__ == "__main__":

    app.run(
        debug=True
    )