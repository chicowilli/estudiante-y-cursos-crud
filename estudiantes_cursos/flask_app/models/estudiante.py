from flask_app.config.mysqlconnection import connectToMySQL


class Estudiante:
    @classmethod
    def crear(cls, nombre, apellido, edad, curso_id):
        return connectToMySQL().query_db(
            "INSERT INTO estudiantes (nombre, apellido, edad, cursos_id) "
            "VALUES (%s, %s, %s, %s)",
            (nombre, apellido, edad, curso_id),
        )
