import sqlite3
import os

def create_db(db_name, db_info):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS info (id INTEGER PRIMARY KEY, status TEXT)')
    cursor.execute('INSERT INTO info (status) VALUES (?)', (db_info,))
    conn.commit()
    conn.close()
    print(f"Database {db_name} created with status: {db_info}")

if __name__ == "__main__":
    create_db('test_db_1.sqlite', 'This is Database ONE')
    create_db('test_db_2.sqlite', 'This is Database TWO')
