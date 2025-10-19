import json
import os


ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "pass123"


DATA_FILE = "bank_data.txt"


if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        user_data = json.load(file)
else:
    user_data = {}

next_account_number = 1001


def save_data():
    """Save all account data to file"""
    with open(DATA_FILE, "w") as file:
        json.dump(user_data, file, indent=4)


def create_acc():
    """Create a new bank account"""
    global next_account_number
    name = input("Enter account user name: ").strip()
    try:
        initial_balance = float(input("Enter initial deposit amount: "))
        if initial_balance < 0:
            print("❌ Invalid amount!")
            return
    except ValueError:
        print("❌ Please enter a valid number!")
        return

    password = input("Create your password: ").strip()

    account_number = str(next_account_number)
    next_account_number += 1

    user_data[account_number] = {
        "name": name,
        "balance": initial_balance,
        "password": password,
        "transactions": [("Initial Deposit", initial_balance)],
    }

    save_data()
    print(f"✅ Account created successfully! Your Account Number: {account_number}")


def login_customer():
    """Customer login"""
    account_number = input("Enter your Account Number: ").strip()
    password = input("Enter your password: ").strip()

    if account_number in user_data and user_data[account_number]["password"] == password:
        print(f"🎉 Welcome {user_data[account_number]['name']}!")
        return account_number
    else:
        print("❌ Invalid account number or password!")
        return None


def deposit(account_number):
    """Deposit money into an account"""
    try:
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("❌ Amount must be positive!")
            return
        user_data[account_number]["balance"] += amount
        user_data[account_number]["transactions"].append(("Deposit", amount))
        save_data()
        print("💰 Deposit successful!")
    except ValueError:
        print("❌ Invalid input!")


def withdraw(account_number):
    """Withdraw money"""
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("❌ Invalid amount!")
            return
        if amount > user_data[account_number]["balance"]:
            print("⚠️ Insufficient balance!")
            return

        user_data[account_number]["balance"] -= amount
        user_data[account_number]["transactions"].append(("Withdraw", -amount))
        save_data()
        print("✅ Withdrawal successful!")
    except ValueError:
        print("❌ Invalid input!")


def check_balance(account_number):
    """Check account balance"""
    balance = user_data[account_number]["balance"]
    print(f"💵 Current Balance: {balance:.2f}")


def transaction_history(account_number):
    """Display transaction history"""
    print("\n📜 Transaction History:")
    for t_type, amount in user_data[account_number]["transactions"]:
        print(f" - {t_type}: {amount:.2f}")


def admin_menu():
    """Admin menu"""
    while True:
        print("\n===== 🧑‍💼 ADMIN MENU =====")
        print("1. Create New Account")
        print("2. View All Accounts")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_acc()
        elif choice == "2":
            for acc_no, details in user_data.items():
                print(f"\nAccount: {acc_no}")
                print(f"Name: {details['name']}")
                print(f"Balance: {details['balance']}")
        elif choice == "3":
            print("👋 Logged out from Admin.")
            break
        else:
            print("❌ Invalid option!")


def customer_menu(account_number):
    """Customer menu"""
    while True:
        print("\n===== 👤 CUSTOMER MENU =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            deposit(account_number)
        elif choice == "2":
            withdraw(account_number)
        elif choice == "3":
            check_balance(account_number)
        elif choice == "4":
            transaction_history(account_number)
        elif choice == "5":
            print("👋 Logged out successfully.")
            break
        else:
            print("❌ Invalid option!")


def main():
    """Main login system"""
    while True:
        print("\n===== 🏦 SIMPLE BANKING SYSTEM =====")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Exit")

        option = input("Enter your choice: ")

        if option == "1":
            user = input("Admin username: ").strip()
            pwd = input("Admin password: ").strip()

            if user == ADMIN_USERNAME and pwd == ADMIN_PASSWORD:
                print("✅ Admin login successful!")
                admin_menu()
            else:
                print("❌ Wrong admin credentials!")

        elif option == "2":
            account = login_customer()
            if account:
                customer_menu(account)

        elif option == "3":
            print("🙏 Thank you for using our bank!")
            break
        else:
            print("❌ Invalid option!")


if __name__ == "__main__":
    main()
