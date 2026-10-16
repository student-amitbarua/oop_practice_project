from food_item import FoodItem
from menu import Menu
from user import Customers, Admin, Employee
from resturant import Resturant 
from orders import Order


mamar_resturant = Resturant("mamar restaurent")

def customer_menu():
    name = input('Enter your Name :')
    email = input('Enter your Email : ')
    phone = input('Enter your phone :')
    address = input('Enter your address :')
    customer = Customers(name=name, email=email, phone=phone, address=address)

    while True:
        print(f'welcome {customer.name}!!')
        print(f'1. View Menu')
        print(f'2. Add item to cart')
        print(f'3. view cart')
        print(f'4. PayBill')
        print(f'5. exit')


        choice = int(input('enter Your choice: '))
        if choice == 1:
            customer.view_menu(mamar_resturant)

        elif choice == 2:
            item_name = input('Enter your item name : ')
            item_quantity = input('Enter item quantity : ')
            customer.add_to_cart(mamar_resturant, item_name, item_quantity)

        elif choice == 3:
            customer.view_cart()

        elif choice == 4:
            customer.pay_bill()


        elif choice == 5:
            break

        else:
            print("Invalid Input")



def admin_menu():
    name = input('Enter your Name:')
    email = input('Enter your Email')
    phone = input('Enter your phone')
    address = input('Enter your address')
    admin = Admin(name=name, email=email, phone=phone, address=address)


    while True:
        print(f'welcome {admin.name}!!')
        print(f'1. Add new item')
        print(f'2. Add new Employee')
        print(f'3. view employee')
        print(f'4. View Items')
        print(f'5. Delete Item')
        print(f'6. exit')

        choice = int(input( "Enter ypur choice : "))

        if choice == 1:
            item_name = input('Enter item Name : ')
            item_price = input('Enter your Item price : ')
            item_quantity = input('Enter your  item quantity : ')

            item = FoodItem(item_name, item_price, item_quantity)

            admin.add_new_item(mamar_resturant, item)


        elif choice == 2:
            name = input('Enter employee name : ')
            phone = input('Enter employee Phone : ')
            email = input("Enter employee Email : ")
            designation = input('Enter employee designation : ')
            age = input('Enter employee age : ')
            salary = input('Enter employee salary : ')

            address = input('Enter employee address : ')
            employee = Employee(name, email, phone, address, age,  designation, salary)

            admin.view_employee(mamar_resturant, employee)


        elif choice == 3:
            admin.view_employee(mamar_resturant)
        
        elif choice == 4:
            admin.view_menu(mamar_resturant)

        elif choice == 5:
            item_name = input("Enter item name : ")
            admin.remove_item(mamar_resturant, item_name)

        elif choice == 6: 
            break
        else: 
            print("Invalid Input")

while True:
    print ('welcome!!')
    print ('1. customer')
    print ('2. admin')
    print ('3. exit')

    choice = int(input('Enter your choice : '))
    if choice == 1:
        customer_menu()
    elif choice == 2: 
        admin_menu()
    elif choice == 3:
        break
    else: 
        print('Invalid Input')
           

