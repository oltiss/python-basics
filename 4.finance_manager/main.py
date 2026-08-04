import sqlite3
import subprocess


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
    conn.close()


def add_income():

    try:
        conn, cur = _conn_to_db()
        amount = input("Enter amount: ")
        if amount >= 0:
            print("You cannot enter negative or zero income!")
        else:


            query = "INSERT INTO finances (amount, category) VALUES(?, ?)"
            cur.execute(query, (amount, category))

    except ValueError:
        print("Please enter a number!")





def print_menu():
    print("========= FINANCE MANAGER =========")
    print("1. Add income")
    print("2. Add expense")
    print("3. Show balance")
    print("4. Show monthly expense analysis")
    print("5. Manage categories")
    print("5. Quit")
    print("===================================")

def main():
    while True:
        subprocess.run(["clear"])
        print_menu()

        choice = input("Enter number from 1-5: ")

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
                print("Thanks for using my finance manager!")
                break
            case _:
                print("Please enter number from 1-5")
                input("Press enter...")





if __name__ == '__main__':
    init_db()
    main()
