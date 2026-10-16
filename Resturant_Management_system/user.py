from abc import ABC
from orders import Order

class User(ABC):
    def __init__(self,name, phone , email , address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        

class Employee(User):
    
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, phone, address, email)
        self.age = age 
        self.designation = designation
        self.salary = salary 

class Customers(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()
        

    def view_menu(self, resturant):
        resturant.menu.show_menu()

    def add_to_card(self, resturant, item_name, quantity):
        item = resturant.menu.find_item(item_name)

        if item:
            if quantity > item.quantity :
                print("Item quantity exceeded !")

            else:
                 item.quantity = quantity
                 self.cart.add_item(item)
                 print("item added")

        else: 
            print ("Item not found")

    def view_card(self):
        print("**view card**")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{item.quantity}')

        print(f'Total Price : {self.cart.total_price}')


    def pay_bill(self):
        print(f"Total {self.cart.total_price} paid successfully")
        self.cart.clear()



class Admin(User):
    def __init__ (self, name, email, address, phone):
        super().__init__(name, email, address, phone)

        def add_employee(self, resturant, employee):
            resturant.add_employee(employee)

        def view_employee(self, resturant):
            resturant.view_employee()

        def add_new_item(self, resturant, item):
            resturant.add_new_item(item)

        def remove_item(self, resturant, item):
            resturant.menu.remove_item(item)

        def view_menu(slef, resturant):
            resturant.menu.show_menu()



