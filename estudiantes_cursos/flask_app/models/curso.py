from flask_app.config.mysqlconnection import connectToMySQL


class Curso:
    @classmethod
    def todos(cls):
        return connectToMySQL().query_db(
            "SELECT id, nombre FROM cursos ORDER BY nombre"
        )

    @classmethod
    def crear(cls, nombre):
        return connectToMySQL().query_db(
            "INSERT INTO cursos (nombre) VALUES (%s)", (nombre,)
        )

    @classmethod
    def por_id(cls, curso_id):
        cursos = connectToMySQL().query_db(
            "SELECT id, nombre FROM cursos WHERE id = %s", (curso_id,)
        )
        return cursos[0] if cursos else None

    @classmethod
    def estudiantes(cls, curso_id):
        return connectToMySQL().query_db(
            "SELECT nombre, apellido, edad FROM estudiantes "
            "WHERE cursos_id = %s ORDER BY apellido, nombre",
            (curso_id,),
        )
