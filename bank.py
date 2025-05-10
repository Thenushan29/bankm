user_name = "admin"
password = "pass123"

user_data = {}
next_account_number = 1001

def create_acc():
    global next_account_number
    name = input("Enter account user name: ")
    try:
        initial_balance = float(input("Enter the amount: "))
        if initial_balance < 0:
            print("Invalid amount😒")
            return
    except ValueError:
        print("Invalid amount entered.")
        return

    account_number = next_account_number
    next_account_number += 1

    user_data[account_number] = {
        "name": name,
        "balance": initial_balance,
        "transactions": [("Initial Deposit", initial_balance)]
    }

    print(f"Account created successfully. Account Number: {account_number}")

def deposit():
    try:
        account_number = int(input("Enter account number: "))
        if account_number not in user_data:
            print("Account not found.")
            return
        
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Amount must be positive.")
            return

        user_data[account_number]["balance"] += amount
        user_data[account_number]["transactions"].append(("Deposit", amount))
        print("Deposit successful.")
    except ValueError:
        print("Invalid input.")

def withdraw_money():
    try:
        account_number = int(input("Enter account number: "))
        if account_number not in user_data:
            print("Account not found.")
            return
            
        amount = float(input("Enter amount to withdraw: "))
        
        if amount > user_data[account_number]["balance"] and amount < 0:
            print("Insufficient balance.")
            return

        user_data[account_number]["balance"] -= amount
        user_data[account_number]["transactions"].append(("Withdrawal", amount))
        print("Withdrawal successful.")
    except ValueError:
        print("Invalid input.")

def opption_admin():
    print("1 = Creat account\n 2 = deposit\n 3 = withdraw\n 4 = check balance\n 5 = Transaction History\n 6 = Exit")
    

def opption_cus():
   print("1 = Withdraw\n 2 = Diposit\n 3 = Check balance\n 4 = Transaction History\n 5 = Exit")
  

while True:

    user = (input("Enter your user name: "))
    code = (input("Enter your password: "))
    
    if user == user_name  and code == password:
       print("login successfullly👍😎")
       opption_admin()
       
       break
    
    elif user in user_data and code in user_data:
        print("login successfullly👍😎")
        opption_cus()
        break
    else:
        print("invalid password or user name! 😦😥")
        
choice = input("Enter the opption: ")
    
def balance():
    acc_num = input("Enter the account number: ")
    if acc_num in user_data:
        print("your account balance is: ", balance) 

    else:
        print("invalid account number")

def Transaction():
    acc_num = input("Enter your account number: ")
    if acc_num in user_data:
        print() 


    else:
        print("invalid account number")
if user == user_name and code == password:
    while True:

        if choice == "1":
            create_acc()
            opption_admin()
            choice = input("Enter the opption: ")
    

        elif choice == "2":
            deposit()
            opption_admin()
            choice = input("Enter the opption: ")
    

        elif choice == "3":
            Withdraw()
            opption_admin()
            choice = input("Enter the opption: ")
    

        elif choice == "4":
            balance()
            opption_admin()
            choice = input("Enter the opption: ")
    

        elif choice == "5":
            Transaction()
            opption_admin()
            choice = input("Enter the opption: ")
    

        elif choice == "6":
            print("Tnq😁")
            break

        else:
            print("invalid opption 🤦‍♂️")
            opption_admin()
            choice = input("Enter the opption: ")
    


elif user in user_data and code in user_data:
    while True:

        if choice == "1":
            deposit()
            opption_cus()
            choice = input("Enter the opption: ")
    

        elif choice == "2":
            Withdraw()
            opption_cus()
            choice = input("Enter the opption: ")
    

        elif choice == "3":
            balance()
            opption_cus()
            choice = input("Enter the opption: ")
    

        elif choice == "4":
            Transaction()
            opption_cus()
            choice = input("Enter the opption: ")
    

        elif choice == "5":
            print("Tnq😁")
            break
        else:
            print("invalid opption 🤦‍♂️")
            opption_cus()
            choice = input("Enter the opption: ")

else:
    print("invalid username or password ")
