import random
import sqlite3
import subprocess


isRunning = True


def _get_db_conn(db_name: str):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    return conn, cur

def init_db():
    conn, cur = _get_db_conn("3.guess_number_game/results.db")

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY,
            level TEXT NOT NULL,
            guesses INTEGER NOT NULL
        )
    """
    )

    conn.close()


def print_menu():
    print("============ GUESS A NUMBER GAME ============")
    print("1. Play a game")
    print("2. Show stats")
    print("3. Quit")
    print("=============================================")


def guessing(level, min, max):

    conn, cur = _get_db_conn("3.guess_number_game/results.db")
    guesses = 0
    number = random.randint(min, max)

    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < min or guess > max:
                raise ValueError
            guesses += 1
        except ValueError:
            print(f"Please enter number from {min}-{max}!")
            continue

        if guess > number:
            print("Lower!")
            continue
        elif guess < number:
            print("Higher!")
            continue
        elif guess == number:
            print(f"You're right! The number was {number}")
            print(f"Total guesses: {guesses}")
            query = "INSERT INTO results (level, guesses) VALUES(?, ?)"
            cur.execute(query, (level, guesses))
            conn.commit()
            conn.close()
            break


def play_game():
    subprocess.run(["clear"])
    print("============ Choose difficulty ============")
    print("1. Easy - number from 1-30")
    print("2. Medium - number from 1-100")
    print("3. Hard - number from 1-1000")
    print("===========================================")
    diff = input("Enter number from 1-3: ")
    match diff:
        case "1":
            guessing("Easy", 1, 30)
        case "2":
            guessing("Medium", 1, 100)
        case "3":
            guessing("Hard", 1, 1000)
        case _ :
            print("Please enter number from 1-3 !!!")


def show_stats():
    conn, cur = _get_db_conn("3.guess_number_game/results.db")

    total_games = cur.execute("SELECT COUNT(*) FROM results")
    total_games = cur.fetchone()
    total_games = total_games[0]


    if total_games:
        total_sum = cur.execute("SELECT SUM(guesses) FROM results")
        total_sum = cur.fetchone()
        total_average = round((total_sum[0] / total_games), 2)
    else:
        total_average = 0
        total_games = 0


    easy_games = cur.execute("SELECT COUNT(*) FROM results WHERE level = 'Easy'")
    easy_games = cur.fetchone()
    easy_games = easy_games[0]

    if easy_games:
        easy_sum = cur.execute("SELECT SUM(guesses) FROM results WHERE level = 'Easy'")
        easy_sum = cur.fetchone()
        easy_average = round((easy_sum[0] / easy_games), 2)
    else:
        easy_games = 0
        easy_average = 0


    medium_games = cur.execute("SELECT COUNT(*) FROM results WHERE level = 'Medium'")
    medium_games = cur.fetchone()
    medium_games = medium_games[0]

    if medium_games:
        medium_sum = cur.execute("SELECT SUM(guesses) FROM results WHERE level = 'Medium'")
        medium_sum = cur.fetchone()
        medium_average = round((medium_sum[0] / medium_games), 2)
    else:
        medium_games = 0
        medium_average = 0


    hard_games = cur.execute("SELECT COUNT(*) FROM results WHERE level = 'Hard'")
    hard_games = cur.fetchone()
    hard_games = hard_games[0]

    if hard_games:
        hard_sum = cur.execute("SELECT SUM(guesses) FROM results WHERE level = 'Hard'")
        hard_sum = cur.fetchone()
        hard_average = round((hard_sum[0] / hard_games), 2)
    else:
        hard_games = 0
        hard_average = 0

    conn.close()

    stats = [total_games, total_average, easy_games, easy_average, medium_games, medium_average, hard_games, hard_average]

    print("================ STATS ================")
    print("Total games:             ", total_games)
    print("Total games average:     ", total_average)
    print("")
    print("Easy games:              ", easy_games)
    print("Easy games average:      ", easy_average)
    print("")
    print("Medium games:            ", medium_games)
    print("Medium games average:    ", medium_average)
    print("")
    print("Hard games:              ", hard_games)
    print("Hard games average:      ", hard_average)
    print("=======================================")




def main():
    isRunning = True
    while isRunning:
        subprocess.run(["clear"])
        print_menu()
        choice = input("Enter number from 1-3: ")

        match choice:
            case "1":
                play_game()
                input("Press enter...")
                continue
            case "2":
                show_stats()
                input("Press enter...")
                continue
            case "3":
                print("Thanks for playing my guess a number game!")
                isRunning = False
            case _:
                print("Please enter number from 1-3 !!!")
                input("Press enter...")
                continue



if __name__ == "__main__":
    init_db()
    main()
