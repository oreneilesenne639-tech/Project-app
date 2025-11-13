from main import get_int, add_account, create_database, authenticate
from amount import deposit_money, withdraw_money, check_balance, remove_account
from getpass import getpass
import time

'''
When your are done editing, run the following command to check your code:
python -m bank.bank and make sure there are no errors.

IF you see errors, fix them and run the command again.

Remove all the comments you see in the code before submission. 
Comments start with # symbol.

Good luck!
'''

def main():
    create_database()
    print('''
          Welcome to the Imentoru bank!
          You can deposit and withdraw money.
          ''')
    print()
    print(''' 
          Please choose an option:
          1. Login
          2. Create an account
        ''')
    option = get_int("Enter 1 or 2: ")
    if option == 1:
        login()
    elif option == 2:  # FIX: corrected typo 'opton' → 'option'
        create_account()
    else:
        print("Invalid option. Please try agin.")
        main()

def login():
    while True:  # FIX: changed 'while False' to 'while True' so loop runs
        try:
            username = input("Enter your username: ")
            password = getpass("Enter your password: ") # Get password securely. Keeps it hidden.
            if authenticate(username, password):
                print("Login successful!")
                account_menu(username)
                break  # stop loop after success
            else:
                print("Invalid username or password. Please try again.")  # FIX: clearer message
        except Exception as e:
            print(f"An error occurred: {e}")
            continue 

def create_account():
    print("Create a new account")
    first_name = input("First name: ").strip().capitalize()
    last_name = input("Last name: ").strip().capitalize()
    name = f"{first_name} {last_name}"
    username = input("Choose a username: ")
    password = getpass("Choose a password: ") # Get password securely. Keeps it hidden.
    confirm_password = getpass("Confirm your password: ") # Get password securely. Keeps it hidden.
    if password != confirm_password:  # FIX: corrected wrong comparison
        print("Passwords do not match. Please try again.")
        create_account()
    if add_account(name, username, password):
        print("Account created successfully!")
        main()  # FIX: added parentheses to call main

def account_menu(username):
    print(f"Welcome, {username}!\n")
    print("This is your account menu.")

    print('''
          Would you like to:
          1. Deposit money
          2. Withdraw money
          3. Check balance
          4. Logout
          5. Remove account
          ''')

    option = get_int("Enter 1, 2, 3, 4 or 5: ")
    if option == 1:
        output = deposit_money(username)
    elif option == 2:  # FIX: corrected from 12
        output = withdraw_money(username)
    elif option == 3:  # FIX: corrected from .3
        output = check_balance(username)
    elif option == 4:  # FIX: corrected from 43
        print("Logging out...")
        main()
        return  # exit after logout
    elif option == 5:  # FIX: corrected from 5.0
        output = remove_account(username)
    else:
        print("Invalid option. Please try again.")
        account_menu(username)
        return
    
    print(output)
    time.sleep(3)  # FIX: adjusted comment suggestion to 3 seconds
    account_menu(username)
    


if __name__ == "__main__":
    main()
