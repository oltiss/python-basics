import time, os
import sqlite3

# helper that connects to database
def _conn_to_db(db_name: str):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    return conn, cur

def _validate_input(question: str, error: str):
    try:
        answer = int(input(question))
        return answer
    except ValueError:
        print(error)
        return None

# Initializating database
def init_db():
    conn, cur = _conn_to_db("tasks.db")

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            deadline TEXT,
            priority TEXT NOT NULL,
            completed TEXT NOT NULL DEFAULT NO
        )
    """
    )

    conn.close()

    print("Database has been initialized")

## CRUD functions

# Listing all tasks
def list_all_tasks():
    from texttable import Texttable
    t = Texttable()


    try:
        conn, cur = _conn_to_db("tasks.db")
        query = "SELECT * FROM tasks"
        cur.execute(query)
        rows = cur.fetchall()

        conn.close()

        if rows:
            t.add_row(["ID", "Name", "Deadline", "Priority", "Completed"])

            for row in rows:
                t.add_row([row[0], row[1], row[2], row[3], row[4]])

            print(t.draw())

        else:
            print("You don't have any tasks")

        print()
        # print("=====================================")

    except Exception as e:
        print(e)

# Adding task
def add_task():

    priority_map = {1: "low", 2: "medium", 3: "high"}

    try:
        name = input("Enter name of task: ")
        deadline = input("Enter deadline of task (YYYY-MM-DD): ")
        priority_num = int(input("Enter priority of task (1-low, 2-medium, 3-high): "))

        if priority_num not in priority_map:
            print("Invalid priority. Please enter a number from 1-3.")
            return

        priority_str = priority_map[priority_num]

        conn, cur = _conn_to_db("tasks.db")
        query = "INSERT INTO tasks (name, deadline, priority) VALUES(?, ?, ?)"
        cur.execute(query, (name, deadline, priority_str))
        conn.commit()
        conn.close()

        print("Task added successfully!")

    except ValueError:
        print("Invalid input. Priority must be a number. Please try again.")
    except Exception as e:
        print(e)

# Editing task
def edit_task(id):
    return

# Deleting task
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
        os.system("clear")
        print_menu()

        try:
            choice = int(input("Enter number from 1-5: "))
            print("=====================================")
        except ValueError:
            print("Error: Please enter number from 1-5!")
            input("Press Enter to continue...")
            continue

        match choice:
            case 1:
                list_all_tasks()
                input("Press Enter to continue...")
            case 2:
                add_task()
                input("Press Enter to continue...")
            case 3:
                print("Edit task")
                input("Press Enter to continue...")
            case 4:
                print("Delete task")
                input("Press Enter to continue...")
            case 5:
                print("Thanks for using my ToDo App")
                break
            case _:
                print("Error: Please enter number from 1-5!")
                input("Press Enter to continue...")
                continue


if __name__ == '__main__':
    main()
