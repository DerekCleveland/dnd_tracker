import sqlite3

def get_sqlite_conn(db_file):
    conn = sqlite3.connect(db_file)
    return conn