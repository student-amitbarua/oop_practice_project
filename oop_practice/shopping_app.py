class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password


class Seller(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.product_list = []

    def publish_product(self, product):
        self.product_list.append(product)
        

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class Customer(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.order = []

    def place_order(self, product, quantity):
        if product.stock >= quantity:
            product.stock -= quantity
            self.order.append((product.name, quantity))
            print (f'order placed for {quantity} units of {product.name}')

        else:
            print('product is out of stock ')


seller1 = Seller("seller@example.com", "password123")
product1 = Product("Laptop", 1000, 5)
seller1.publish_product(product1)

customer1 = Customer("customer@example.com", "securepass")
customer1.place_order(product1, 2)