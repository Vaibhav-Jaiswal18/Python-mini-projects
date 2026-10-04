bank_accounts = {}


# ---------------- CREATE ACCOUNT ----------------
def create_account():

    account_no = input("Enter Account Number: ")

    if account_no in bank_accounts:
        print("Account already exists.")
        return

    name = input("Enter Customer Name: ")
    account_type = input("Enter Account Type (Saving/Current): ")
    mobile = input("Enter Mobile Number: ")

    while True:

        try:
            balance = float(input("Enter Initial Deposit: "))

            if balance >= 1000:
                break
            else:
                print("Minimum balance should be Rs.1000")

        except ValueError:
            print("Invalid amount.")

    bank_accounts[account_no] = {
        "Name": name,
        "Type": account_type,
        "Mobile": mobile,
        "Balance": balance
    }

    print("\nAccount Created Successfully.\n")


# ---------------- DEPOSIT MONEY ----------------
def deposit_money():

    account_no = input("Enter Account Number: ")

    if account_no not in bank_accounts:
        print("Account Not Found.")
        return

    amount = float(input("Enter Deposit Amount: "))

    if amount > 0:
        bank_accounts[account_no]["Balance"] += amount
        print("Amount Deposited Successfully.")
    else:
        print("Invalid Amount.")


# ---------------- WITHDRAW MONEY ----------------
def withdraw_money():

    account_no = input("Enter Account Number: ")

    if account_no not in bank_accounts:
        print("Account Not Found.")
        return

    amount = float(input("Enter Withdrawal Amount: "))

    balance = bank_accounts[account_no]["Balance"]

    if amount <= balance:
        bank_accounts[account_no]["Balance"] -= amount
        print("Withdrawal Successful.")
    else:
        print("Insufficient Balance.")


# ---------------- BALANCE ENQUIRY ----------------
def balance_enquiry():

    account_no = input("Enter Account Number: ")

    if account_no in bank_accounts:

        print("\nCustomer Name :", bank_accounts[account_no]["Name"])
        print("Account Type  :", bank_accounts[account_no]["Type"])
        print("Balance       :", bank_accounts[account_no]["Balance"])

    else:
        print("Account Not Found.")


# ---------------- DISPLAY ALL ACCOUNTS ----------------
def display_all_accounts():

    if len(bank_accounts) == 0:
        print("No Records Found.")
        return

    print("\n================ ACCOUNT DETAILS ================\n")

    for acc, details in bank_accounts.items():

        print("Account Number :", acc)

        for key, value in details.items():
            print(f"{key:10}: {value}")

        print("-" * 45)


# ---------------- SEARCH ACCOUNT ----------------
def search_account():

    name = input("Enter Customer Name: ").lower()

    found = False

    for acc, details in bank_accounts.items():

        if details["Name"].lower() == name:

            print("\nAccount Found")
            print("Account Number :", acc)

            for key, value in details.items():
                print(f"{key:10}: {value}")

            found = True

    if not found:
        print("Customer Not Found.")


# ---------------- CALCULATE INTEREST ----------------
def calculate_interest():

    if len(bank_accounts) == 0:
        print("No Accounts Available.")
        return

    rate = float(input("Enter Interest Rate (%): "))

    interests = [
        (
            acc,
            details["Name"],
            round(details["Balance"] * rate / 100, 2)
        )
        for acc, details in bank_accounts.items()
    ]

    print("\nInterest Details\n")

    for account in interests:

        print("Account :", account[0])
        print("Name    :", account[1])
        print("Interest:", account[2])
        print("-" * 35)


# ---------------- MEMBERSHIP OPERATOR DEMO ----------------
def membership_demo():

    account = input("Enter Account Number: ")

    if account in bank_accounts:
        print("Account Exists.")
    else:
        print("Account Does Not Exist.")


# ---------------- IDENTITY OPERATOR DEMO ----------------
def identity_demo():

    print("\nIdentity Operator Demonstration\n")

    if len(bank_accounts) < 2:
        print("Create at least two accounts.")
        return

    keys = list(bank_accounts.keys())

    first = bank_accounts[keys[0]]
    second = bank_accounts[keys[1]]

    if first is second:
        print("Both references point to the same object.")
    else:
        print("Both references point to different objects.")


# ---------------- HIGH BALANCE CUSTOMERS ----------------
def high_balance_customers():

    amount = float(input("Enter Minimum Balance: "))

    customers = [
        details["Name"]
        for details in bank_accounts.values()
        if details["Balance"] >= amount
    ]

    if customers:

        print("\nCustomers having balance above", amount)

        for customer in customers:
            print(customer)

    else:
        print("No Customer Found.")


# ================= MAIN MENU =================

while True:

    print("\n")

    print("=" * 55)
    print("          BANKING MANAGEMENT SYSTEM")
    print("=" * 55)

    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Balance Enquiry")
    print("5. Display All Accounts")
    print("6. Search Customer")
    print("7. Calculate Interest")
    print("8. Membership Operator Demo")
    print("9. Identity Operator Demo")
    print("10. High Balance Customers")
    print("11. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == '1':
        create_account()

    elif choice == '2':
        deposit_money()

    elif choice == '3':
        withdraw_money()

    elif choice == '4':
        balance_enquiry()

    elif choice == '5':
        display_all_accounts()

    elif choice == '6':
        search_account()

    elif choice == '7':
        calculate_interest()

    elif choice == '8':
        membership_demo()

    elif choice == '9':
        identity_demo()

    elif choice == '10':
        high_balance_customers()

    elif choice == '11':
        print("Thank You for Using Banking Management System.")
        break

    else:
        print("Invalid Choice. Please Try Again.")