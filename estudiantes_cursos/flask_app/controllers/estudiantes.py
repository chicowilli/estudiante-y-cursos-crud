from flask import Blueprint, flash, redirect, render_template, request, url_for

from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante

estudiantes_bp = Blueprint("estudiantes", __name__, url_prefix="/estudiantes")


@estudiantes_bp.route("/nuevo", methods=["GET", "POST"])
def nuevo_estudiante():
    cursos = Curso.todos()

    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        apellido = request.form.get("apellido", "").strip()
        edad_texto = request.form.get("edad", "").strip()
        curso_id_texto = request.form.get("curso_id", "").strip()

        try:
            edad = int(edad_texto)
            curso_id = int(curso_id_texto)
        except ValueError:
            flash("Revisa la edad y el curso.")
            return render_template(
                "nuevo_estudiante.html",
                cursos=cursos,
                curso_seleccionado=curso_id_texto,
            )

        if not nombre or not apellido or edad < 0:
            flash("Completa los datos del estudiante.")
            return render_template(
                "nuevo_estudiante.html",
                cursos=cursos,
                curso_seleccionado=curso_id_texto,
            )
        if not any(curso["id"] == curso_id for curso in cursos):
            flash("Selecciona un curso válido.")
            return render_template(
                "nuevo_estudiante.html",
                cursos=cursos,
                curso_seleccionado=curso_id_texto,
            )

        Estudiante.crear(nombre, apellido, edad, curso_id)
        flash("Estudiante guardado.")
        return redirect(url_for("cursos.lista_cursos"))

    curso_seleccionado = request.args.get("curso_id", type=int)
    return render_template(
        "nuevo_estudiante.html",
        cursos=cursos,
        curso_seleccionado=curso_seleccionado,
    )
