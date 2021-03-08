import pymysql

# Connect, select and CRUD Database functions

def connect_to_db():
    return pymysql.connect("localhost", "root", "password", "miniproject")

def execute_sql_crud(connection, statement):
    cursor = connection.cursor()
    cursor.execute(statement)
    cursor.close()
    connection.commit()
    
def execute_sql_select(connection, statement):
    cursor = connection.cursor()
    cursor.execute(statement)
    cursor.close()
    return cursor.fetchall()

def execute_sql_select_(statement):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(statement)
    cursor.close()
    return cursor.fetchall()
