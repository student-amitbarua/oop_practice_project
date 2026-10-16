from menu import Menu

class Resturant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()


        def add_employee(self, employee):
            self.employees.append(employee)


        def view_employee(slef):
            print('employee List:')

            for emp in self.employees:

                print(emp.name, emp.email, emp.phone, emp.address)
