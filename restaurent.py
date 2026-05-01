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
        for emp in self.employees:
            print(emp.name, emp.phone, emp.email, emp.address)

    def find_employee(self, employee_name):
        for emp in self.employees:
            if emp.name.lower() == employee_name.lower():
                return emp
        return None

    def remove_employee(self, employee_name):
        emp = self.find_employee(employee_name)

        if emp:
            self.employees.remove(emp)
            print(f'{employee_name} removed from employee list')
        else:
            print(f'{employee_name} not found in employee list')
