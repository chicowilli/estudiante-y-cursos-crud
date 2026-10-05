import os

import pymysql
from dotenv import load_dotenv

load_dotenv()


class MySQLConnection:
    def __init__(self, db=None):
        self.db = db or os.getenv("MYSQL_DATABASE", "estudiantes")

    def query_db(self, query, data=None):
        connection = pymysql.connect(
            host=os.getenv("MYSQL_HOST", "localhost"),
            user=os.getenv("MYSQL_USER", "root"),
            password=os.getenv("MYSQL_PASSWORD", "root"),
            database=self.db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )

        try:
            with connection.cursor() as cursor:
                cursor.execute(query, data)
                if query.lstrip().lower().startswith("select"):
                    return cursor.fetchall()
                connection.commit()
                return cursor.lastrowid or cursor.rowcount
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()


def connectToMySQL(db=None):
    return MySQLConnection(db)
