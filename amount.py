import sqlite3

'''
This is bad. The main funtion has errors line 8 and need need fixing.
Oh no. All the functions have errors. Quick, fix them all!
'''
def main():
    account_check = sqlite3.connect('bank.db')  # FIX: corrected sqlite3.con → sqlite3.connect
    cursor = account_check.cursor()  # FIX: corrected .cur() → .cursor()
    cursor.execute('''
        SELECT * FROM accounts  # FIX: added * to properly select data
    ''')
    accounts = cursor.fetchall()
    if not accounts:
        print("No accounts found. Please create an account first.")
    print(accounts)
    account_check.close()  # FIX: added to close connection


def deposit_money(username):
    amount = float(input("Enter amount to deposit: "))  # FIX: changed f() → float()
    conn = sqlite3.connect('bank.db')  # FIX: changed 'lank.db' → 'bank.db'
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE accounts
        SET balance = balance + ?
        WHERE username = ?
    ''', (amount, username))
    conn.commit()
    conn.close()
    return f"Deposited ${amount} to {username}'s account."


def withdraw_money(username):
    amount = float(input("Enter amount to withdraw: "))  # FIX: changed f() → float()
    conn = sqlite3.connect('bank.db')  # FIX: corrected sqlite3.con → sqlite3.connect
    cursor = conn.cursor()
    cursor.execute('''
        SELECT balance FROM accounts WHERE username = ?
    ''', (username,))  # FIX: added missing username parameter
    result = cursor.fetchone()
    if result is None:
        conn.close()
        return "Account not found."
    balance = result[0]
    if amount > balance:
        conn.close()
        return "Insufficient funds."
    else:
        cursor.execute('''
            UPDATE accounts
            SET balance = balance - ?
            WHERE username = ?
        ''', (amount, username))
        conn.commit()
        conn.close()
        return f"Withdrew ${amount} from {username}'s account."  # FIX: added variables in f-string


def check_balance(username):
    conn = sqlite3.connect('bank.db')  # FIX: changed 'lank.db' → 'bank.db'
    cursor = conn.cursor()
    cursor.execute('''
        SELECT balance FROM accounts WHERE username = ?
    ''', (username,))
    result = cursor.fetchone()
    conn.close()
    if result is None:
        return "Account not found."
    balance = result[0]
    return f"{username}'s current balance is: ${balance}"


def remove_account(username):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM accounts WHERE username = ?
    ''', (username,))  # FIX: added missing username tuple
    conn.commit()
    conn.close()
    return f"Account {username} has been removed."  # FIX: corrected {user_name} → {username}



if __name__ == "__main__":
    main()
