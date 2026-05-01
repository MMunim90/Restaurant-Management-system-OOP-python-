from users import Customer
from main import restora

def customer_menu():
    name = input('Enter Your Name: ')
    email = input('Enter Your Email: ')
    phone = int(input('Enter Your Phone: '))
    address = input('Enter Your Address: ')

    customer = Customer(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"Welcome {customer.name}!!!")
        print("1. View Menu")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            customer.view_menu(restora)
        elif choice == 2:
            item_name = input("Enter Item Name: ")
            item_quantity = int(input("Enter Item Quantity: "))

            customer.add_to_cart(restora, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            print("Thank You!!!")
            break
        else:
            print("Invalid Choice!")