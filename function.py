import lab19

lab19.menu()

while True:
    choice = input("Enter a number between 1 - 9: ")
    if choice == "1":
        a = float(input("Enter a number: "))
        b = float(input("Enter a number: "))
        lab19.add(a,b)
    elif choice == "2":
        a = float(input("Enter a number: "))
        b = float(input("Enter a number: "))
        lab19.subtraction(a, b)
    elif choice == "3":
        a = float(input("Enter a number: "))
        b = float(input("Enter a number: "))
        lab19.multiplication(a, b)
    elif choice == "4":
        a = float(input("Enter a number: "))
        b = float(input("Enter a number: "))
        lab19.division(a, b)
    elif choice == "5":
        a = float(input("Enter a number: "))
        b = float(input("Enter a number: "))
        lab19.power(a, b)
    elif choice == "6":
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        lab19.list_squares(a, b)
    elif choice == "7":
        user_input = input("Enter a string: ")
        lab19.count_case(user_input)
    elif choice == "8":
        user_input = input("Enter a string: ")
        position = int(input("Enter character position: "))

        while position <= 0 or position > len(user_input):
            position = int(input("Enter a position: "))
        lab19.display_element(user_input,position)
    elif choice == "9":
        print("Exiting")
        break
    else:
       print("invalid option")