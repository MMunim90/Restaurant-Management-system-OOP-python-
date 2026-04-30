from abc import ABC

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


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
        self.employees = [] # Database

    def add_employee(self, name, phone, email, address, age, designation, salary):
        employee = Employee(name, phone, email, address, age, designation, salary)
        self.employees.append(employee)
        print(f"{employee.name} is added as employee!!")

    def view_employee(self):
        print("Employee List: ")
        for emp in self.employees:
            print(emp.name, emp.phone, emp.email, emp.address)

ad = Admin('Shahidul', 23423423, 'shahidul@gmail.com', 'Dhaka')
ad.add_employee('Sagor', 234234, 's@gmail.com', 'Khulna', 32, 'chef', 12000)

ad.view_employee()