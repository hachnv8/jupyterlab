import sqlite3
import os

def create_db(db_name, db_info):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    # Create 'info' table
    cursor.execute('CREATE TABLE IF NOT EXISTS info (id INTEGER PRIMARY KEY, status TEXT)')
    cursor.execute('INSERT INTO info (status) VALUES (?)', (db_info,))
    
    # Create 'tasks' table for Scheduling examples
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY, 
            task_name TEXT, 
            due_date TEXT, 
            status TEXT
        )
    ''')
    
    # Insert some sample tasks
    sample_tasks = [
        ('Daily Report', '2026-04-02', 'Pending'),
        ('Database Backup', '2026-04-03', 'Scheduled'),
        ('Weekly Sync', '2026-04-05', 'Pending')
    ]
    cursor.executemany('INSERT INTO tasks (task_name, due_date, status) VALUES (?, ?, ?)', sample_tasks)
    
    conn.commit()
    conn.close()
    print(f"Database {db_name} initialized with 'info' and 'tasks' tables.")

if __name__ == "__main__":
    create_db('test_db_1.sqlite', 'This is Database ONE')
    create_db('test_db_2.sqlite', 'This is Database TWO')
