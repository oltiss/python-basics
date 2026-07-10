import time
import sqlite3


def connect_to_db(db_name):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    return cur

def init_db():
    cur = connect_to_db("tasks.db")
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
    print("Database has been initialized")





def list_all_tasks():
    cur = connect_to_db("tasks.db")
    tasks = cur.execute("SELECT * FROM tasks")
    return

def add_task(id, name, deadline, priority):
    return

def edit_task():
    return

def delete_task():
    return

def main():
    isRunning = True

    init_db()

    while isRunning:
        print("============= To Do APP =============")

        print("=====================================")



if __name__ == '__main__':
    main()
