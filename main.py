import sqlite3

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value  # FIX: changed from 'return v' to 'return value'
        except ValueError:
            print("Invalid input. Please enter an integer.")


def create_database():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            balance REAL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()


def query_db(query, params=()):
    conn = sqlite3.connect('bank.db')  # FIX: changed from 'lank.db' to 'bank.db'
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


def add_account(name, username, password):
    # Placeholder function to simulate adding an account
    # In a real application, this would interact with a database
    q = "INSERT INTO accounts (name, username, password) VALUES (?, ?, ?)"
    query_db(q, (name, username, password))
    print(f"Account for {name} with username {username} created.")
    return True


def authenticate(username, password):
    q = "SELECT * FROM accounts WHERE username = ? AND password = ?"
    results = query_db(q, (username, password))
    if results:
        return True
    return False  # FIX: added explicit False return for failed login
