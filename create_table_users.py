from psycopg2 import connect, OperationalError
import psycopg2.errors

USER = "postgres"
HOST = "localhost"
PASSWORD = "coderslab"
DATABASE = "application_db"


def users():
    """
    creates table
    :return:
    """
    try:
        sql = """
        CREATE TABLE users 
        (id serial, 
        username varchar(255) UNIQUE, 
        hashed_password varchar(80), 
        PRIMARY KEY (id));"""
        cnx = connect(user=USER, password=PASSWORD, host=HOST, database=DATABASE)
        cnx.autocommit = True
        cursor = cnx.cursor()
        cursor.execute(sql)
        print("You've created table")
    except OperationalError as e:
        print("Connection error!", e)
    except psycopg2.errors.DuplicateTable as e:
        print('Table already exists!', e)
    else:
        cursor.close()
        cnx.close()


if __name__ == '__main__':
    users()
