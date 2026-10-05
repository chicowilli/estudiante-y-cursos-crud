from flask import redirect, url_for

from flask_app import create_app

app = create_app()


@app.route("/")
def inicio():
    return redirect(url_for("cursos.lista_cursos"))


if __name__ == "__main__":
    app.run(debug=True)
