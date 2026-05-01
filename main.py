from restaurent import Restaurent
from customer_menu import customer_menu
from admin_menu import admin_menu

restora = Restaurent("Sultan\'s Dine")
customer_menu(restora)
admin_menu(restora)

while True:
    print("*********Welcome**********")
    print("1. Admin")
    print("2. Customer")
    print("3. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        admin_menu()
    elif choice == 2:
        customer_menu()
    elif choice == 3:
        print("Thank You")
        break
    else:
        print("Invalid Choice")
    