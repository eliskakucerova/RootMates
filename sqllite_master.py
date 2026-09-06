import sqlite3

def get_tables_name(database:str = "plantsdb.db", to_print:bool = False) -> list[str]:
    """
    Process sqlite_master and returns a list of table names located in the database

    Parameters
    ----------
    database : str
        database name
    to_print: bool
        Prints table names

    Returns
    -------
    tables: list[str]
        List of table names
    """
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if to_print:
            for table in tables:
                print(table[0])

    return [x[0] for x in tables]