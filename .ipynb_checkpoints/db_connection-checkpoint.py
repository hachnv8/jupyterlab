import sqlite3
import os

DB1_PATH = 'test_db_1.sqlite'
DB2_PATH = 'test_db_2.sqlite'

class DBConnector:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        print(f"Connected to {self.db_path}")
        return self.conn

    def close(self):
        if self.conn:
            self.conn.close()
            print(f"Closed connection to {self.db_path}")

def get_connection(db_num):
    """Utility to switch between DB 1 and 2"""
    if db_num == 1:
        return DBConnector(DB1_PATH).connect()
    elif db_num == 2:
        return DBConnector(DB2_PATH).connect()
    else:
        raise ValueError("Invalid database number. Use 1 or 2.")

if __name__ == "__main__":
    # Quick test
    conn1 = get_connection(1)
    status1 = conn1.execute("SELECT status FROM info").fetchone()[0]
    print(f"DB 1 Status: {status1}")
    conn1.close()

    conn2 = get_connection(2)
    status2 = conn2.execute("SELECT status FROM info").fetchone()[0]
    print(f"DB 2 Status: {status2}")
    conn2.close()
