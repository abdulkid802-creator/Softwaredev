# def menu():
#     print("*" * 30)
#     print("* Calculator + *")
#     print("1- Add ")
#     print("2- Subtraction ")
#     print("3- Multiplication ")
#     print("4- Division ")
#     print("5- Raise to the power ")
#     print("6- List of squares")
#     print("7- Upper and Lower Case")
#     print("8- Display specific element")
#     print("9- Exit")
#     print("*" * 30)
#
# def add(a, b):
#     print("Result", a +b)
#
# def subtraction(a, b):
#     print("Result", a - b)
#
# def multiplication(a, b):
#     print("Result", a * b)
#
# def division(a, b):
#     print("Result", a / b)
#
# def power(a, b):
#     print("Result", a ** b)
#
# def list_squares(a, b):
#     for i in range(a, b + 1):
#         print(i * i, end= " ")
#     print()
#
# def count_case(user_input):
#     upper = 0
#     lower = 0
#
#     for char in user_input:
#         if char.isupper():
#             upper += 1
#         elif char.islower:
#             lower += 1
#     print("The number of upper case is", user_input)
#     print("The number of lower case is", user_input)
#
# def display_element(user_input, position):
#     print("Character: ", user_input[position])
#
# while True:
#     menu()
#     choice = input("Enter a number between 1 - 9: ")
#     if choice == "1":
#         a = float(input("Enter a number: "))
#         b = float(input("Enter a number: "))
#         add(a,b)
#     elif choice == "2":
#         a = float(input("Enter a number: "))
#         b = float(input("Enter a number: "))
#         subtraction(a, b)
#     elif choice == "3":
#         a = float(input("Enter a number: "))
#         b = float(input("Enter a number: "))
#         multiplication(a, b)
#     elif choice == "4":
#         a = float(input("Enter a number: "))
#         b = float(input("Enter a number: "))
#         division(a, b)
#     elif choice == "5":
#         a = float(input("Enter a number: "))
#         b = float(input("Enter a number: "))
#         power(a, b)
#     elif choice == "6":
#         a = int(input("Enter a number: "))
#         b = int(input("Enter a number: "))
#         list_squares(a, b)
#     elif choice == "7":
#         user_input = input("Enter a string: ")
#         count_case(user_input)
#     elif choice == "8":
#         user_input = input("Enter a string: ")
#         position = int(input("Enter character position: "))
#
#         while position <= 0 or position > len(user_input):
#             position = int(input("Enter a position: "))
#         display_element(user_input,position)
#     elif choice == "9":
#         print("Exiting")
#         break
#     else:
#        print("invalid option")
