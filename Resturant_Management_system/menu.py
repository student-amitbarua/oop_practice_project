class Menu:
    def __init__(self):
        self.items = []


        def add_menu_item(self, item):
            self.items.append(item)

        
        def find_item(self, item_name):
            for item in self.items:
                if item.name.lower() == item_name.lower():
                    return item
                return None 
            
        def remove_item(self, item_name):
            item = self.find_item(item_name)
            if item:
                self.items.remove(item)
                print('item delete')

            else: 
                print('item Not found ')


        def show_menu(slef):
            print("*********Menu***********")
            print("Name\tPrice\tquantity")
            for item in self.items:
                (f'{item.name}\t{item.price}\t{item.quantity}')
