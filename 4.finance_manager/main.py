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
        amount = input("Enter amount: ")
        if amount >= 0:
            print("You cannot enter negative or zero income!")
        else:

            category = ""
            query = "INSERT INTO finances (amount, category) VALUES(?, ?)"
            cur.execute(query, (amount, category))

    except ValueError:
        print("Please enter a number!")



# Manage categories
def categories():
    t = Texttable()
    conn, cur = _conn_to_db()

    # List all categories
    query = "SELECT * FROM categories"
    cur.execute(query)
    rows = cur.fetchall()
    conn.commit()

    if rows:
        t.add_row(["ID", "Name", "Type"])
        for row in rows:
            t.add_row([row[0], row[1], row[2]])
        print(t.draw())
    else:
        print("No categories found.")
    conn.close()


def print_menu():
    print("========= FINANCE MANAGER =========")
    print("1. Add income")
    print("2. Add expense")
    print("3. Show balance")
    print("4. Show monthly expense analysis")
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
                print("1")
                input("Press enter...")
            case "2":
                print("2")
                input("Press enter...")
            case "3":
                print("3")
                input("Press enter...")
            case "4":
                print("4")
                input("Press enter...")
            case "5":
                categories()
                input("Press enter...")
            case "6":
                print("Thanks for using my finance manager!")
                break
            case _:
                print("Please enter number from 1-6")
                input("Press enter...")





if __name__ == '__main__':
    init_db()
    main()
