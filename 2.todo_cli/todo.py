import time, os
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
            deadline TEXT,
            priority TEXT NOT NULL
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
            t.add_row(["ID", "Name", "Deadline", "Priority"])
            i = 0

            for row in rows:
                t.add_row([row[0], row[1], row[2], row[3]])
                i += 1

            print(t.draw())
            print("=====================================")

            if i == 1:
                return f"\033[1mYou have {i} task \033[0m"
            else:
                return f"\033[1mYou have {i} tasks \033[0m"


        else:
            return "\033[1mYou don't have any tasks\033[0m"


    except Exception as e:
        return e

# Adding task
def add_task():

    priority_map = {1: "low", 2: "medium", 3: "high"}

    try:
        name = input("Enter name of task: ")
        deadline = input("Enter deadline of task (YYYY-MM-DD): ")
        # Date validation

        priority_num = int(input("Enter priority of task (1-low, 2-medium, 3-high): "))

        if name == "":
            return print("You must enter a name! Please try again.")

        if priority_num not in priority_map:
            return print("Invalid priority. Please enter a number from 1-3.")

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
def edit_task():
    print(list_all_tasks())

    priority_map = {1: "low", 2: "medium", 3: "high"}


    try:
        id = int(input("Enter ID of task you want to edit: "))

        conn, cur = _conn_to_db("tasks.db")

        query = "SELECT * FROM tasks WHERE id = ?"
        cur.execute(query, (id, ))
        task = cur.fetchall()

        if not task:
            conn.close()
            return print("Task with this ID doesn't exists")

        new_name = input(f"Enter new name or press enter to skip (old: {task[0][1]}): ")
        if new_name == "":
            new_name = task[0][1]


        new_deadline = input(f"Enter new deadline or press enter to skip (old: {task[0][2]}): ")
        if new_deadline == "":
            new_deadline = task[0][2]
        # Date validation

        new_priority_num = input(f"Enter new priority (1-3) or press enter to skip (old: {task[0][3]}): ")
        if new_priority_num == "":
            new_priority_str = task[0][3]
        else:
            int(new_priority_num)

            if new_priority_num not in priority_map:
                conn.close()
                return print("Invalid priority. Please enter a number from 1-3.")

            new_priority_str = priority_map[new_priority_num]

        update_query = "UPDATE tasks SET name = ?, deadline = ?, priority = ? WHERE id = ?"
        cur.execute(update_query, (new_name, new_deadline, new_priority_str, id))
        conn.commit()
        conn.close()

        return print(f"Successfully updated task with ID = {id}")




    except ValueError:
        print("Invalid input. Your input must be a number. Please try again.")

# Deleting task
def delete_task():
    print(list_all_tasks())

    try:
        conn, cur = _conn_to_db("tasks.db")

        id = int(input("Enter ID of task which you want to delete: "))

        query = "SELECT * FROM tasks WHERE id = ?"
        cur.execute(query, (id, ))
        task = cur.fetchall()

        if not task:
            conn.close()
            return print("Task with this ID doesn't exists")

        confirmation = input(f"Are you sure you want to delete task with ID = {task[0][0]} (y/N): ")

        if confirmation == "y" or confirmation == "Y":
            delete_query = "DELETE FROM tasks WHERE id = ?"
            cur.execute(delete_query, (task[0][0], ))
            conn.commit()
            conn.close()
            return print(f"Successfully deleted task with ID = {task[0][0]}")
        else:
            conn.close()
            return print(f"Deletion of task with ID = {task[0][0]} has been cancelled")


    except ValueError:
        print("Task with this ID doesn't exists")


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
                print(list_all_tasks())
                input("Press Enter to continue...")
            case 2:
                add_task()
                input("Press Enter to continue...")
            case 3:
                edit_task()
                input("Press Enter to continue...")
            case 4:
                delete_task()
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
