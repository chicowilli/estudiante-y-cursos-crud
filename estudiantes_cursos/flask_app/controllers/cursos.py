from flask import Blueprint, flash, redirect, render_template, request, url_for

from flask_app.models.curso import Curso

cursos_bp = Blueprint("cursos", __name__, url_prefix="/cursos")


@cursos_bp.route("/", methods=["GET", "POST"])
def lista_cursos():
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        if nombre:
            Curso.crear(nombre)
            flash("Curso guardado.")
        else:
            flash("Escribe el nombre del curso.")
        return redirect(url_for("cursos.lista_cursos"))

    return render_template("cursos.html", cursos=Curso.todos())


@cursos_bp.route("/<int:curso_id>")
def mostrar_curso(curso_id):
    curso = Curso.por_id(curso_id)
    if curso is None:
        flash("No encontré ese curso.")
        return redirect(url_for("cursos.lista_cursos"))

    return render_template(
        "mostrar_curso.html",
        curso=curso,
        estudiantes=Curso.estudiantes(curso_id),
    )
