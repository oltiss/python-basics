import time
import sqlite3

# helper that connects to database
def _conn_to_db(db_name: str):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    return conn, cur

# Initializating database
def init_db():
    conn, cur = _conn_to_db("tasks.db")

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            deadline TEXT NULLABLE,
            priority TEXT NOT NULL,
            completed BOOL NOT NULL DEAFULT False
        )
    """
    )

    conn.close()

    print("Database has been initialized")

# Listing all tasks
def list_all_tasks():
    try:
        conn, cur = _conn_to_db("tasks.db")
        query = "SELECT * FROM tasks"
        cur.execute(query)
        rows = cur.fetchall()

        conn.close()
    except Exception as e:
        print(e)

    for row in rows:
        print(row)

# Adding task
def add_task(name, deadline, priority):

    
    try:
        conn, cur = _conn_to_db("tasks.db")
        query = "INSERT INTO tasks (name, deadline, priority) VALUES(?, ?, ?)"
        cur.execute(query, (name, deadline, priority))
        conn.commit()

        conn.close()
    except Exception as e:
        print(e)

def edit_task():
    return

def delete_task(id):
    return

# prints menu
def print_menu():
    print("============= To Do APP =============")
    print("1. List all tasks")
    print("2. Add task")
    print("3. Edit task")
    print("4. Delete task")
    print("5. Quit")
    print("=====================================")


def main():
    isRunning = True

    init_db()

    while isRunning:
        print_menu()
        try:
            choice = int(input("Choose number from 1-5: "))
        except ValueError:
            print("Error: Please enter number from 1-5!")

        match choice:
            case 1:
                list_all_tasks()
            case 2:
                print("Add task")
            case 3:
                print("Edit task")
            case 4:
                print("Delete task")
            case 5:
                print("Thanks for using my ToDo App")
                break
            case _:
                print("Error: Please enter number from 1-5!")
                continue


if __name__ == '__main__':
    main()
