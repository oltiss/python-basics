import sqlite3
import subprocess
from texttable import Texttable

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
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
        )
    """)
    conn.commit()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            type TEXT NOT NULL
        )
    """)
    conn.commit()

    conn.close()


def add_income():

    try:
        conn, cur = _conn_to_db()
        amount = float(input("Enter amount: "))
        if amount <= 0:
            return print("You cannot enter negative or zero income!")

        categories_query = "SELECT * FROM categories WHERE type = 'income'"
        cur.execute(categories_query)
        rows = cur.fetchall()
        t = Texttable()
        t.add_row(["ID", "Name"])
        for row in rows:
            t.add_row([row[0], row[1]])
        print(t.draw())

        id = int(input("Enter ID of category: "))

        category_query = "SELECT * FROM categories WHERE id = ?"
        cur.execute(category_query, (id, ))
        category = cur.fetchall()

        if not category:
            return print("Category with this ID doesn't exists")

        category = category[0][1]

        insert_query = "INSERT INTO finances (amount, category) VALUES(?, ?)"
        cur.execute(insert_query, (amount, category))
        conn.commit()
        print("Successfully added income")

    except ValueError:
        print("Please enter a number!")
    finally:
        conn.close()


def add_expense():
    try:
        conn, cur = _conn_to_db()
        amount = float(input("Enter amount: "))
        if amount <= 0:
            return print("You cannot enter negative or zero expense!")

        categories_query = "SELECT * FROM categories WHERE type = 'expense'"
        cur.execute(categories_query)
        rows = cur.fetchall()
        t = Texttable()
        t.add_row(["ID", "Name"])
        for row in rows:
            t.add_row([row[0], row[1]])
        print(t.draw())

        id = int(input("Enter ID of category: "))

        category_query = "SELECT * FROM categories WHERE id = ?"
        cur.execute(category_query, (id, ))
        category = cur.fetchall()

        if not category:
            return print("Category with this ID doesn't exists")

        category = category[0][1]

        insert_query = "INSERT INTO finances (amount, category) VALUES(?, ?)"
        cur.execute(insert_query, (amount, category))
        conn.commit()
        print("Successfully added expense")

    except ValueError:
        print("Please enter a number!")
    finally:
        conn.close()



# temporary to display table from db
def show_balance():
    t = Texttable()
    conn, cur = _conn_to_db()
    query = "SELECT * FROM finances"
    cur.execute(query)
    rows = cur.fetchall()
    t.add_row(["ID", "Amount", "category", "timestamp"])
    t.set_cols_dtype(["t", "t", "t", "t"])
    for row in rows:

        t.add_row([str(row[0]), str(row[1]), row[2], row[3]])

    print(t.draw())
    conn.close()

# Manage categories
def manage_categories():
    subprocess.run(["clear"])
    print("========= CATEGORIES =========")
    print("1. Add category")
    print("2. Delete category")
    print("3. Edit category")
    print("4. Show categories")
    print("5. Return to main menu")
    print("==============================")

    choice = input("Enter number from 1-5: ")

    match choice:
        case "1":
            add_category()
            input("Press enter...")
        case "2":
            delete_category()
            input("Press enter...")
        case "3":
            edit_category()
            input("Press enter...")
        case "4":
            show_categories()
            input("Press enter...")
        case "5":
            return
        case _:
            print("Please enter number from 1-6")
            return input("Press enter...")


def add_category():
    name = input("Enter name of category: ")
    type = input("Enter type of category (1 - income, 2 - expense): ")
    if type == '1':
        type = "income"
    elif type == '2':
        type = "expense"
    else:
        print("Please enter valid number!")
        return

    query = """INSERT INTO categories (name, type) VALUES(?, ?)"""
    conn, cur = _conn_to_db()
    cur.execute(query, (name, type))
    conn.commit()
    conn.close()


def delete_category():
    ok = show_categories()
    if ok:
        try:
            id = int(input("Enter ID of category you want to delete: "))

            conn, cur = _conn_to_db()

            query = """SELECT * FROM categories WHERE id = ?"""
            cur.execute(query, (id, ))
            category = cur.fetchall()

            if not category:
                return print("Category with this ID doesn't exists!")

            confirmation = input(f"Are you sure you want to delete category with ID = {category[0][0]} (y/N): ")

            if confirmation == "y" or confirmation == "Y":
                delete_query = """DELETE FROM categories WHERE id = ?"""
                cur.execute(delete_query, (id, ))
                conn.commit()
                print(f"Successfully deleted category with ID = {category[0][0]}!")
            else:
                print("Deletion has been canceled.")

        except ValueError:
            print("This is not valid ID!")
        except Exception as e:
            print(e)
        finally:
            conn.close()


def edit_category():
    ok = show_categories()
    if ok:
        try:
            id = int(input("Enter ID of category you want to edit: "))

            conn, cur = _conn_to_db()

            query = """SELECT * FROM categories WHERE id = ?"""
            cur.execute(query, (id, ))
            category = cur.fetchall()

            if not category:
                return print("Category with this ID doesn't exists!")


            name = category[0][1]
            type = category[0][2]

            new_name = input(f"Enter new name or press enter to skip (old: {name}): ")
            if new_name == "":
                new_name = name

            new_type = input(f"Enter new type (1 - income, 2 - expense) or press enter to skip (old: {type}): ")
            if new_type == "":
                new_type = type
            elif new_type == "1":
                new_type = "income"
            elif new_type == "2":
                new_type = "expense"
            else:
                return print("Please enter number from 1-2!")

            edit_query = """UPDATE categories SET name = ?, type = ? WHERE id = ?"""
            cur.execute(edit_query, (new_name, new_type, id))
            conn.commit()

            print(f"Successfully updated category with ID = {id}")

        except ValueError:
            print("This is not valid ID!")
        finally:
            conn.close()


def show_categories():
    t = Texttable()
    conn, cur = _conn_to_db()

    try:

        # List all categories
        query = "SELECT * FROM categories"
        cur.execute(query)
        rows = cur.fetchall()

        if rows:
            t.add_row(["ID", "Name", "Type"])
            for row in rows:
                t.add_row([row[0], row[1], row[2]])
            print(t.draw())
            return True
        else:
            print("No categories found.")
            return False
    except Exception as e:
        print(e)
        return False
    finally:
        conn.close()


def print_menu():
    print("========= FINANCE MANAGER =========")
    print("1. Add income")
    print("2. Add expense")
    print("3. Show balance")
    print("4. Show monthly finance analysis")
    print("5. Manage categories")
    print("6. Quit")
    print("===================================")


def main():
    while True:
        subprocess.run(["clear"])
        print_menu()

        choice = input("Enter number from 1-6: ")

        match choice:
            case "1":
                add_income()
                input("Press enter...")
            case "2":
                add_expense()
                input("Press enter...")
            case "3":
                show_balance()
                input("Press enter...")
            case "4":
                print("4")
                input("Press enter...")
            case "5":
                manage_categories()
            case "6":
                print("Thanks for using my finance manager!")
                break
            case _:
                print("Please enter number from 1-6")
                input("Press enter...")





if __name__ == '__main__':
    init_db()
    main()
