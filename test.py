import sqlite3

con = sqlite3.connect("test.db")

cur = con.cursor()


cur.execute(
        """
        CREATE TABLE IF NOT EXISTS test (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """
    )



cur.execute("INSERT INTO test (name, age) VALUES(?, ?)", ("Joe", 30))
con.commit()
con.close()
