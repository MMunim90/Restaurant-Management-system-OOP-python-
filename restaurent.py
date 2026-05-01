from menu import Menu

class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees = [] # Employees Database
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print("Employee List: ")
        print("Name\tEmail\tPhone\tAge\tAddress\tDesignation\tSalary")
        for emp in self.employees:
            print(f"{emp.name}\t{emp.email}\t{emp.phone}\t{emp.age}\t{emp.address}\t{emp.designation}\t{emp.salary}")

    def find_employee(self, employee_name):
        for emp in self.employees:
            if emp.name.lower() == employee_name.lower():
                return emp
        return None

    def remove_employee(self, employee_name):
        emp = self.find_employee(employee_name)

        if emp:
            self.employees.remove(emp)
        else:
            print(f'{employee_name} not found in employee list')
