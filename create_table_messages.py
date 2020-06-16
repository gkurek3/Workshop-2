from psycopg2 import connect, OperationalError
import psycopg2.errors

USER = "postgres"
HOST = "localhost"
PASSWORD = "coderslab"
DATABASE = "application_db"


def messages():
    """
    creates table
    :return:
    """
    try:
        sql = """
        CREATE TABLE messages 
        (id serial,
        from_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
        to_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
        text varchar(255),
        creation_date timestamp default CURRENT_TIMESTAMP, 
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
    messages()
