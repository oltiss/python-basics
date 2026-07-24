import random
import sqlite3


isRunning = True


def _get_db_conn(db_name: str):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    return conn, cur


def print_menu():
    print("============ GUESS A NUMBER GAME ============")
    print("1. Play a game")
    print("2. Show stats")
    print("3. Quit")


def play_game():
    return


def show_stats():
    return


while isRunning:
    print_menu()
    choice = input("Enter number from 1-3: ")

    match choice:
        case "1":
            print("1")
            input("Press enter...")
            continue
        case "2":
            print("2")
            input("Press enter...")
            continue
        case "3":
            print("Thanks for playing my guess a number game!")
            isRunning = False
        case _:
            print("Please enter number from 1-3 !!!")
            continue
