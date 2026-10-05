# Cursos y estudiantes

Proyecto sencillo de Flask para practicar la relación de un curso con varios estudiantes usando MySQL.

## Estructura

```text
flask_app/
  bd/schema.sql
  config/mysqlconnection.py
  controllers/
  models/
  templates/
  static/css/
  static/js/
  static/img/
  server.py
```

## Preparar MySQL

1. Asegúrate de que el servidor MySQL esté iniciado.
2. Abre una terminal en esta carpeta y ejecuta el SQL:

```powershell
mysql -u root -p < flask_app/bd/schema.sql
```

El script crea la base `estudiantes` y las tablas `cursos` y `estudiantes`. Cada estudiante queda ligado a un curso.

3. Copia el ejemplo a la raíz del proyecto y cambia `MYSQL_PASSWORD` para que coincida con tu instalación de MySQL. Si tu usuario no es `root`, cambia también `MYSQL_USER`.

```powershell
Copy-Item flask_app/.env.example .env
```

## Instalar y arrancar

Desde la carpeta del proyecto:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r flask_app/requirements.txt
py -m flask_app.server
```

Abre <http://127.0.0.1:5000>. En Cursos puedes crear cursos; en Nuevo estudiante puedes elegir un curso y agregar un estudiante. Al abrir un curso aparece su lista de estudiantes.
