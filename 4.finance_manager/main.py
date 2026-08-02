import sqlite3


db_name = "4.finance_manager/finances.db"


# db config
def _conn_to_db():
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    return conn, cur

def init_db():
    conn, cur = _conn_to_db()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS finances (
            id INTEGER PRIMARY KEY,
            amount INTEGER NOT NULL,
            category TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        )
    """)
    conn.commit()
    conn.close()


def print_menu():
    print("========= FINANCE MANAGER =========")
    print("1. Add income")
    print("2. Add expense")
    print("3. Show balance")
    print("4. Show monthly expense analysis")
    print("===================================")

def main():
    print_menu()




if __name__ == '__main__':
    init_db()
    main()
