import sqlite3
from sqllite_master import get_tables_name

plants_table_name, relation_table_name = get_tables_name()
POSITIVE = "přítel"
NEGATIVE = "nepřítel"
INPUT = "brambory"

def get_all_table_rows(cursor_obj:sqlite3.Cursor, table_name:str):
    cursor_obj.execute(f"SELECT * FROM {table_name}")
    command = cursor_obj.fetchall()
    for row in command:
        print(row)

def get_positive_relations(cursor_obj:sqlite3.Cursor):
    """
    TBD
    Parameters
    ----------
    cursor_obj

    Returns
    -------

    """
    cursor_obj.execute(f"SELECT name_b, reason FROM {relation_table_name} WHERE id_a = ? AND relation = ?",
                   (plant_id, POSITIVE,))
    command = cursor.fetchall()

    print(f"S čím doporučuji vysázet {INPUT}: ")
    for row in command:
        print(f"Co: {row[0]}, Proč: {row[1]}")

def get_negative_relations(cursor_obj:sqlite3.Cursor):
    """
    TBD
    Parameters
    ----------
    cursor_obj

    Returns
    -------

    """
    cursor_obj.execute(f"SELECT name_b, reason FROM {relation_table_name} WHERE id_a = ? AND relation = ?",
                       (plant_id, NEGATIVE,))
    command = cursor.fetchall()

    print(f"S čím NEdoporučuji vysázet {INPUT}: ")
    for row in command:
        print(f"Co: {row[0]}, Proč: {row[1]}")

def process_user_input(cursor_obj:sqlite3.Cursor) -> str:
    """
    TBD
    Parameters
    ----------
    cursor_obj

    Returns
    -------

    """
    cursor_obj.execute(f"SELECT id FROM {plants_table_name} WHERE name = ?", (INPUT,))
    command = cursor.fetchall()  # return list with tuples
    plant_id = ''.join([str(x[0]) for x in command])
    return plant_id


with sqlite3.connect("plantsdb.db") as connection:
    cursor = connection.cursor()
    plant_id = process_user_input(cursor)
    get_positive_relations(cursor)
    print("\n")
    get_negative_relations(cursor)
