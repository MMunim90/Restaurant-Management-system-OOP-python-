from restaurent import Restaurent
restora = Restaurent("Sultan\'s Dine")

while True:
    print("*********Welcome**********")
    print("1. Admin")
    print("2. Customer")
    print("3. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        from admin_menu import admin_menu
        admin_menu(restora)
    elif choice == 2:
        from customer_menu import customer_menu
        customer_menu(restora)
    elif choice == 3:
        print("Thank You")
        break
    else:
        print("Invalid Choice")
    