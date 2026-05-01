from food_item import Food_item
from users import Admin

def admin_menu(restora):
    name = input('Enter Your Name: ')
    email = input('Enter Your Email: ')
    phone = int(input('Enter Your Phone: '))
    address = input('Enter Your Address: ')

    admin = Admin(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"Welcome {admin.name}!!!")
        print("1. Add New Employee")
        print("2. View Employee")
        print("3. Remove Employee")
        print("4. Add New Item")
        print("5. View Item")
        print("6. Delete Item")
        print("7. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            name = input("Enter Employee Name: ")
            phone = int(input("Enter Employee Phone: "))
            email = input("Enter Employee Email: ")
            age = int(input("Enter Employee Age: "))
            designation = input("Enter Employee Designation: ")
            salary = int(input("Enter Employee salary: "))
            address = input("Enter Employee Address: ")

            admin.add_employee(name, phone, email, age, designation, salary, address)
        elif choice == 2:
            admin.view_employee(restora)
        elif choice == 3:
            employee_name = input("Enter Employee name: ")
            delete = input(f"Type \'DELETE\' to remove {employee_name} from employee list: ")
            if delete == 'DELETE':
                admin.remove_employee(restora, employee_name)
                print(f"{employee_name} was deleted from employee list")
            else:
                print("Character did\'nt match!")
        elif choice == 4:
            item_name = input("Enter Item Name: ")
            item_price = int(input("Enter Item Price: "))
            item_quantity = int(input("Enter Item Quantity: "))

            item = Food_item(item_name, item_price, item_quantity)
            admin.add_new_item(restora, item)

        elif choice == 5:
            admin.view_item(restora)
        elif choice == 6:
            item_name = input("Enter Item name: ")
            delete = input(f"Type \'DELETE\' to remove {item_name} from item list: ")
            if delete == 'DELETE':
                admin.remove_item(restora, item_name)
                print(f"{item_name} was deleted from item list")
            else:
                print("Character did\'nt match!")
        elif choice == 7:
            print("Thank You!!!")
            break
        else:
            print("Invalid Choice!")