from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase, DuplicateTable

USER = "postgres"
HOST = "localhost"
PASSWORD = "coderslab"


def create_db():
    """
    Create db with given name.
    """
    try:
        sql = "CREATE DATABASE application_db;"
        cnx = connect(user=USER, password=PASSWORD, host=HOST)
        cnx.autocommit = True
        cursor = cnx.cursor()
        cursor.execute(sql)
        print("You've created database")
    except OperationalError as e:
        print("Connection error!", e)
    except DuplicateDatabase as e:
        print('Database already exists!', e)
    else:
        cursor.close()
        cnx.close()


if __name__ == '__main__':
    create_db()
