import random

class Bank:
    users = {}
    total_balance = 0
    loan_feature = True
    total_loan_amount = 0

    @classmethod
    def add_user(cls, user):
        cls.users[user.account_no] = user
        cls.total_balance += user.balance

    @classmethod
    def delete_user(cls, account_no):
        if account_no in cls.users:
            cls.total_balance -= cls.users[account_no].balance
            del cls.users[account_no]
            print(f"Account {account_no} deleted successfully.")
        else:
            print("Account not found.")

    @classmethod
    def view_all_users(cls):
        if not cls.users:
            print("No users available.")
            return
        for acc, user in cls.users.items():
            print(f"Account: {acc}, Name: {user.name}, Balance: {user.balance}")

    @classmethod
    def view_total_balance(cls):
        print(f"Total balance in the bank: {cls.total_balance}")

    @classmethod
    def view_total_loans(cls):
        print(f"Total loan amount given: {cls.total_loan_amount}")

    @classmethod
    def toggle_loan_feature(cls, status):
        cls.loan_feature = status
        print(f"Loan feature set to: {'ON' if status else 'OFF'}")


class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_no = random.randint(10000, 99999)
        self.balance = 0
        self.transaction_history = []
        self.loan_taken = 0

        Bank.add_user(self)

    def deposit(self, amount):
        self.balance += amount
        Bank.total_balance += amount
        self.transaction_history.append(f"Deposited {amount}")
        print(f"Deposited {amount} successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            if Bank.total_balance < amount:
                print("Bank is bankrupt! Cannot process withdrawal.")
            else:
                print("Withdrawal amount exceeded.")
            return
        self.balance -= amount
        Bank.total_balance -= amount
        self.transaction_history.append(f"Withdrew {amount}")
        print(f"Withdrawn {amount} successfully.")

    def check_balance(self):
        print(f"Available balance: {self.balance}")

    def check_transaction_history(self):
        print("\nTransaction History:")
        for txn in self.transaction_history:
            print(txn)

    def take_loan(self):
        if not Bank.loan_feature:
            print("Loan feature is turned off.")
            return

        if self.loan_taken >= 2:
            print("Loan limit exceeded (Max 2 times).")
            return

        loan_amount = self.balance
        self.balance += loan_amount
        self.loan_taken += 1
        Bank.total_balance += loan_amount
        Bank.total_loan_amount += loan_amount
        self.transaction_history.append(f"Took loan of {loan_amount}")
        print(f"Loan of {loan_amount} granted successfully.")

    def transfer_money(self, receiver_account_no, amount):
        if receiver_account_no not in Bank.users:
            print("Account does not exist.")
            return

        if amount > self.balance:
            print("Withdrawal amount exceeded.")
            return

        receiver = Bank.users[receiver_account_no]
        self.balance -= amount
        receiver.balance += amount
        self.transaction_history.append(f"Transferred {amount} to {receiver_account_no}")
        receiver.transaction_history.append(f"Received {amount} from {self.account_no}")
        print(f"Transferred {amount} to account {receiver_account_no} successfully.")


class Admin:
    @staticmethod
    def create_user(name, email, address, account_type):
        return User(name, email, address, account_type)

    @staticmethod
    def delete_user(account_no):
        Bank.delete_user(account_no)

    @staticmethod
    def view_all_users():
        Bank.view_all_users()

    @staticmethod
    def check_total_balance():
        Bank.view_total_balance()

    @staticmethod
    def check_total_loans():
        Bank.view_total_loans()

    @staticmethod
    def toggle_loan_feature(status):
        Bank.toggle_loan_feature(status)


# =================== REPLICA SYSTEM START ===================

def replica_system():
    users = {}
    admin = Admin()

    while True:
        print("\n==== Welcome to Bank Management System ====")
        print("1. User Sign Up")
        print("2. User Login")
        print("3. Admin Login")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account type (Savings/Current): ")
            user = admin.create_user(name, email, address, account_type)
            users[user.account_no] = user
            print(f"Account created! Your account number: {user.account_no}")

        elif choice == "2":
            acc_no = int(input("Enter your account number: "))
            if acc_no not in users:
                print("Invalid account number!")
                continue
            user = users[acc_no]
            while True:
                print(f"\n=== Welcome {user.name} ===")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Check Transaction History")
                print("5. Take Loan")
                print("6. Transfer Money")
                print("7. Logout")

                user_choice = input("Enter your choice: ")

                if user_choice == "1":
                    amount = int(input("Enter amount to deposit: "))
                    user.deposit(amount)

                elif user_choice == "2":
                    amount = int(input("Enter amount to withdraw: "))
                    user.withdraw(amount)

                elif user_choice == "3":
                    user.check_balance()

                elif user_choice == "4":
                    user.check_transaction_history()

                elif user_choice == "5":
                    user.take_loan()

                elif user_choice == "6":
                    receiver_acc = int(input("Enter receiver's account number: "))
                    amount = int(input("Enter amount to transfer: "))
                    user.transfer_money(receiver_acc, amount)

                elif user_choice == "7":
                    print("Logging out...")
                    break

                else:
                    print("Invalid choice.")

        elif choice == "3":
            while True:
                print("\n=== Admin Panel ===")
                print("1. View All Users")
                print("2. Delete a User")
                print("3. Check Total Bank Balance")
                print("4. Check Total Loans")
                print("5. Toggle Loan Feature")
                print("6. Logout")

                admin_choice = input("Enter your choice: ")

                if admin_choice == "1":
                    admin.view_all_users()

                elif admin_choice == "2":
                    del_acc = int(input("Enter account number to delete: "))
                    admin.delete_user(del_acc)
                    if del_acc in users:
                        del users[del_acc]

                elif admin_choice == "3":
                    admin.check_total_balance()

                elif admin_choice == "4":
                    admin.check_total_loans()

                elif admin_choice == "5":
                    status = input("Enter ON/OFF to toggle loan feature: ").strip().lower()
                    if status == "on":
                        admin.toggle_loan_feature(True)
                    elif status == "off":
                        admin.toggle_loan_feature(False)
                    else:
                        print("Invalid input.")

                elif admin_choice == "6":
                    print("Logging out admin...")
                    break

                else:
                    print("Invalid choice.")

        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# =============== RUN THE REPLICA SYSTEM ===============

replica_system()
