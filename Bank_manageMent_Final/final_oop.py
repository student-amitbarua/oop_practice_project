import random

class Bank:
    def __init__(self):
        self.users = {}
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature  = True

        
    def add_user(self, name, email, address, account_type):
            account_number = random.randint(10000, 99999)
            self.users[account_number] = User(self, name, email, address, account_type, account_number)
            return account_number
        
    def delete_user(self, account_number):
            if account_number in self.users:
                del self.users[account_number]

                print(' user account deleted.')

            else:
                print('Account does not exist.')


    def get_all_users(self):
            for user in self.users.values():
                print(user)


    def check_total_balance(self):
            print(f'Total available balance in the bank : {self.total_balance}')

    def total_loan(self):
            print(f'total loan amount : {self.total_loan_amount}')

    def loan_feature(self, status):
            self.loan_enabled = status
            print(f'loan feature {'enabled'if status else 'disabled'}.  ')
             


class User:
    def __init__(self, name, email, address, account_type, account_number):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = account_number
        self.balance = 0
        self.transaction_history = []
        self.loan_count = 0
        

    def deposite(self, amount):
        self.balance += amount
        Bank.total_balance += amount
        self.transaction_history.append(amount)
        print(f"Depostite {amount} successfully")



    def Withdraw(self, amount):
        if amount > self.balance:
            if Bank.total_balance < amount:
             print('Bank is bankurpt')
            else: 
                print('Withdraw amount exceeded')

        self.balance -= amount
        self.transaction_history.append(amount)
        print(f'withdraw {amount}')


    def check_balance(self):
        print(f'Available Blance : {self.balance}')


    def check_transaction(self):
        print('\n ---Transaction----')
        for txn in self.transaction_history:
            print (txn)
    

    def take_loan(self):
        if not Bank.loan_feature:
            print('Loan feature is disable')


        if self.loan_count >= 2:
            print('Loan limit exceeded. Only 2 loans allowed')

            return
        
        loan_amount = self.balance
        self.balance += loan_amount
        Bank.total_balance += loan_amount
        Bank.total_loan_amount += loan_amount
        self.loan_count += 1
        self.transaction_history.append(loan_amount)
        print(f'loan of {loan_amount} granted.')

    def transfer(self, receiver_acc_no, amount):
        if receiver_acc_no not in Bank.users:
            print('Account does not exist.')
            return 
        if amount > self.balance:
            print('Withdraw amount exceeded.')
            return 
        

        receiver = Bank.users[receiver_acc_no]
        self.balance -= amount
        receiver.balance += amount
        self.transaction_history.append(f'Transfered {amount} to {receiver_acc_no}')
        receiver.transaction_history.append(f'Received {amount} from {self.account_number}')

        print(f' Transferred {amount} to account {receiver_acc_no} successfully')


class Admin:

    def __init__(self,bank):
        self.bank = bank

    def create_user(name, email, address, account_type):
        return User(name, email, address, account_type)

    

    def delete_user(account_no):
        Bank.delete_user(account_no)

    

    def view_all_user():
        Bank.get_all_users()    


    
    def check_total_balance():
        Bank.total_balance()


    
    def check_total_loans():
        Bank.total_loan()

    

    def loan_feature(status):
        Bank.loan_feature()



###### replica ############


def replica():
    users = {}
    admin = Admin()

    while True:
        print('1. Create User Account')
        print('2. User Login')
        print('3. Admin Login')
        print('4. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            name = input('Enter Name: ')
            email = input('Enter Email: ')
            address = input('Enter adress: ')
            account_type = input('Enter Account Type : ')
            user = admin.create_user(name, email, address, account_type)
            users[user.account_number] = user
            print('Account Created!')

        elif choice == '2':
             acc_no = int(input('Enter your Account Number:'))

             if acc_no not in users:
                 print('Invalid Account Number!')
                 continue
             
             user = users[acc_no]

             while True:
                 
                 print(f' Wellcome {user.name}  ')
                 print('1. Deposit Money')
                 print('2. Withdraw Money')
                 print('3. check Balance.')
                 print('4. check Transaction History')
                 print('5. Take Loan')
                 print('6. Transfer Money')
                 print('7. Logout')

                 user_choice= input('Enter your choice: ')



                 if user_choice == '1':
                     amount = int(input('Enter your amount to deposit: '))

                     user.deposit(amount)

                 elif user_choice == '2':
                     amount = int(input('Enter your withdraw ammount '))

                     user.Withdraw(amount)

                 elif user_choice == '3':
                     user.check_balance()

                 elif user_choice == '4':
                     user.check_transaction()

                 elif user_choice == '5':
                     user.take_loan()

                 elif user_choice == '6':
                     receiver_acc = int(input('Enter receiver account number: '))

                     amount = int(input('Enter your amount: '))
                     user.transfer(receiver_acc, amount)


                 elif user_choice == '7':
                     print( ' Logging out..')
                     break
                 
                 else:
                     print("invalid choice")

        elif choice == '3':

            while True:
                print('*** Admin Panel *****')
                print('1. view all users ') 
                print('2. delete a user ') 
                print('3. check total bank balance ') 
                print('4. check total loans ') 
                print('5. Loan feature ') 
                print('6. Logout') 
                

            admin_choice = input('Enter your choice: ')


            if admin_choice == '1':
                admin.view_all_user()

            elif admin_choice == '2':

                del_ac = int(input('Enter account number to delete: '))
                admin.delete_user(del_ac)
                if del_ac in users:
                    del users[del_ac]

            elif admin_choice == '3':
                admin.check_total_balance()

            elif admin_choice == '4':
                admin.check_total_loans()

            elif admin_choice == '5':
                status = input('Enter ON/OFF:').lower()
                if status == 'on':
                    admin.loan_feature(True)

                elif status == 'off':
                    admin.loan_feature(False)

                else: 
                    print('Invalid input.')

            
        elif  choice == '4':
             print('Exiting the system. ')
             break
        else:
            print('Invalid choice, try again.')



replica()
