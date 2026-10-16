import random

class Bank:
    def __init__(self):
        self.users = {}
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature = True
    
    def add_user(self, name, email, address, account_type):
        account_number = random.randint(10000, 99999)
        self.users[account_number] = User(name, email, address, account_type, account_number)
        return account_number

    def delete_user(self, account_number):
        if account_number in self.users:
            del self.users[account_number]
            print('User account deleted.')
        else:
            print('Account does not exist.')

    def get_all_users(self):
        for user in self.users.values():
            print(user)

    def check_total_balance(self):
        print(f'Total available balance in the bank: {self.total_balance}')

    def total_loan(self):
        print(f'Total loan amount: {self.total_loan_amount}')  # Fixed string formatting

    def set_loan_feature(self, status):  # Renamed method to avoid name conflict
        self.loan_feature = status
        print(f'Loan feature {"enabled" if status else "disabled"}.')

class User:
    def __init__(self, name, email, address, account_type, account_number):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = account_number  # Used the provided account number instead of generating a new one
        self.balance = 0
        self.transaction_history = []
        self.loan_count = 0

    def deposit(self, bank, amount):  # Added bank parameter for updating total balance
        self.balance += amount
        bank.total_balance += amount  # Fixed reference to total balance
        self.transaction_history.append(f'Deposited {amount}')
        print(f"Deposited {amount} successfully")

    def withdraw(self, bank, amount):  # Added bank parameter for updating total balance
        if amount > self.balance:
            print('Withdraw amount exceeded.')
        elif bank.total_balance < amount:  # Corrected reference to bank's balance
            print('Bank is bankrupt.')
        else:
            self.balance -= amount
            bank.total_balance -= amount  # Adjusted bank's total balance
            self.transaction_history.append(f'Withdrawn {amount}')
            print(f'Withdrawn {amount} successfully')

    def check_balance(self):
        print(f'Available Balance: {self.balance}')

    def check_transaction(self):
        print('\n---Transaction History---')
        for txn in self.transaction_history:
            print(txn)

    def take_loan(self, bank):  # Added bank parameter for loan validation
        if not bank.loan_feature:  # Fixed reference to loan feature
            print('Loan feature is disabled')
            return

        if self.loan_count >= 2:
            print('Loan limit exceeded. Only 2 loans allowed')
            return

        loan_amount = self.balance  # Changed loan amount to balance
        self.balance += loan_amount
        bank.total_balance += loan_amount
        bank.total_loan_amount += loan_amount
        self.loan_count += 1
        self.transaction_history.append(f'Loan of {loan_amount} granted.')
        print(f'Loan of {loan_amount} granted.')

    def transfer(self, bank, receiver_acc_no, amount):  # Added bank parameter for accessing users
        if receiver_acc_no not in bank.users:
            print('Account does not exist.')
            return

        if amount > self.balance:
            print('Withdraw amount exceeded.')
            return

        receiver = bank.users[receiver_acc_no]
        self.balance -= amount
        receiver.balance += amount
        self.transaction_history.append(f'Transferred {amount} to {receiver_acc_no}')
        receiver.transaction_history.append(f'Received {amount} from {self.account_number}')
        print(f'Transferred {amount} to account {receiver_acc_no} successfully')

class Admin:
    def __init__(self, bank):  # Added bank instance reference
        self.bank = bank

    def create_user(self, name, email, address, account_type):
        return User(name, email, address, account_type, random.randint(10000, 99999))

    def delete_user(self, account_no):
        self.bank.delete_user(account_no)  # Fixed reference to Bank instance

    def view_all_users(self):
        self.bank.get_all_users()  # Fixed reference to Bank instance

    def check_total_balance(self):
        self.bank.check_total_balance()  # Fixed reference to Bank instance

    def check_total_loans(self):
        self.bank.total_loan()  # Fixed reference to Bank instance

    def loan_feature(self, status):
        self.bank.set_loan_feature(status)  # Fixed reference to method

def replica():
    bank = Bank()
    admin = Admin(bank)  # Passed bank instance to Admin

    while True:
        print("\n1. Create User Account")
        print("2. User Login")
        print("3. Admin Login")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            account_type = input("Enter Account Type: ")
            acc_number = bank.add_user(name, email, address, account_type)
            print(f"Account Created! Your account number is {acc_number}")

        elif choice == "2":
            acc_no = int(input("Enter your Account Number: "))

            if acc_no not in bank.users:
                print("Invalid Account Number!")
                continue

            user = bank.users[acc_no]

            while True:
                print(f"\nWelcome {user.name}")
                print("1. Deposit Money")
                print("2. Withdraw Money")
                print("3. Check Balance")
                print("4. Check Transaction History")
                print("5. Take Loan")
                print("6. Transfer Money")
                print("7. Logout")

                user_choice = input("Enter your choice: ")

                if user_choice == "1":
                    amount = int(input("Enter the amount to deposit: "))
                    user.deposit(bank, amount)  # Passed bank instance

                elif user_choice == "2":
                    amount = int(input("Enter the amount to withdraw: "))
                    user.withdraw(bank, amount)  # Passed bank instance

                elif user_choice == "3":
                    user.check_balance()

                elif user_choice == "4":
                    user.check_transaction()

                elif user_choice == "5":
                    user.take_loan(bank)  # Passed bank instance

                elif user_choice == "6":
                    receiver_acc = int(input("Enter receiver account number: "))
                    amount = int(input("Enter the amount: "))
                    user.transfer(bank, receiver_acc, amount)  # Passed bank instance

                elif user_choice == "7":
                    print("Logging out...")
                    break

                else:
                    print("Invalid choice!")

        elif choice == "3":
            while True:
                print("\n*** Admin Panel ***")
                print("1. View all users")
                print("2. Delete a user")
                print("3. Check total bank balance")
                print("4. Check total loans")
                print("5. Toggle Loan feature")
                print("6. Logout")

                admin_choice = input("Enter your choice: ")

                if admin_choice == "1":
                    admin.view_all_users()

                elif admin_choice == "2":
                    del_acc = int(input("Enter account number to delete: "))
                    admin.delete_user(del_acc)

                elif admin_choice == "3":
                    admin.check_total_balance()

                elif admin_choice == "4":
                    admin.check_total_loans()

                elif admin_choice == "5":
                    status = input("Enter ON/OFF: ").lower()
                    admin.loan_feature(status == "on")

                elif admin_choice == "6":
                    print("Logging out...")
                    break

                else:
                    print("Invalid choice!")

        elif choice == "4":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice, try again.")

# Run the simulation
replica()
