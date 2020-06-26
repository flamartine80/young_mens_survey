
# 1. Imports
import sqlite3
import pandas as pd



#2. Database conections and cursor initialization
conexion = sqlite3.connect('database.db', check_same_thread = False)

cursor = conexion.cursor()

#3. Create Table
def create_table():
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS encuesta_hhjj_2020_b(name text, p1 integer, p2 integer,p3 integer,p4 integer)')


def insert_record(name, p1, p2, p3, p4):
    cursor.execute("INSERT INTO encuesta_hhjj_2020_b VALUES (:name, :p1, :p2, :p3, :p4)",
                   {'name': name, 'p1': p1, 'p2': p2, 'p3': p3, 'p4': p4})
    conexion.commit()

    # shows last state of the database

    # conexion.close()


# insert_record('Felipe', 2,4,3,1)


def show_database():
    # cursor.execute("SELECT * FROM encuesta_hhjj_2020_b", conexion)
    df = pd.read_sql_query("SELECT * FROM encuesta_hhjj_2020_b", conexion)
    print(df)
    # print(cursor.fetchall())

# def show_database2():
#     # cursor.execute("SELECT * FROM encuesta_hhjj_2020_b", conexion)
#     df = pd.read_sql_query("SELECT * FROM encuesta_hhjj_2020_b", conexion)
#     print(df)
#     # print(cursor.fetchall())

# insert_record('Marta',1,1,4,4)

show_database()

#


# print(df)



