import sqlite3

con = sqlite3.connect("test.db")

cur = con.cursor()


cur.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            deadline TEXT NULLABLE,
            priority TEXT NOT NULL,
            completed BOOL NOT NULL
        )
    """
    )
