from abc import ABC

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = None
    
    def view_menu(self, restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self, restaurent, item_name):
        item = restaurent.menu.find_item(item_name)

        if item:
            pass
        else:
            print("Item not found")

    def view_cart(self):
        print("******Cart******")
        print("Name\tPrice\tQuentity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print("Total Price : {self.cart.total_price}")


class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity
        else:
            self.items[item] = item.quantity

    def remove(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())
    
    def clear(self):
        self.items = {}


class Employee(User):
    def __init__(self, name, phone, email, address,  age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary


# emp = Employee('Munim', 'munim@gmail.com', 123434, 'Dhaka', 23, 'chef', 12000)
# print(emp.name)


class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)

    def view_employee(self, restaurent):
        restaurent.view_employee()

    def add_new_item(self, restaurent, item):
        restaurent.menu.add_menu_item(item)

    def remove_item(self, restaurent, item):
        restaurent.menu.remove_item(item)


class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees = [] # Employees Database
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print("Employee List: ")
        for emp in self.employees:
            print(emp.name, emp.phone, emp.email, emp.address)

class Menu:
    def __init__(self):
        self.items = [] # Items Database

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
            print(f'{item_name} deleted')
        else:
            print(f'{item_name} not found')

    def show_menu(self):
        print("******Menu******")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')


class Food_item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

        

# ad = Admin('Shahidul', 23423423, 'shahidul@gmail.com', 'Dhaka')
# ad.add_employee('Sagor', 234234, 's@gmail.com', 'Khulna', 32, 'chef', 12000)

# ad.view_employee()


mn = Menu()
item = Food_item("Pizza", 12.45, 10)
mn.add_menu_item(item)
mn.show_menu()