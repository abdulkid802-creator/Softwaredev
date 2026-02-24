# choice = ""
# password = ""
# while choice != 5:
#     print("--- Password tool ---")
#     print("1. Enter password")
#     print("2. count digits")
#     print("3. count uppercase letter")
#     print("4. count lowercase letters")
#     print("5. exit")
#
#     choice = input("choose an option: ")
#     if choice == "1":
#         password = input("Enter password: ")
#     elif choice == "2":
#         password = input("Enter password: ")
#         count = 0
#         for character in password:
#             if character.isdigit():
#                 count += 1
#             print("Digits: ", count)
#     elif choice == "3":
#         count = 0
#         for character in password:
#             if character.isupper():
#                 count += 1
#             print("Uppercase: ", count)
#     elif choice == "4":
#         count = 0
#         for character in password:
#             if character.islower():
#                 count += 1
#             print("Lowercase: ", count)
#     else:
#         print("Invalid menu options")

# choice = ""
#
# while choice != 4:
#     print("---Time Table CALCULATOR---")
#     print("1. Show times table (1 - 12)")
#     print("2. Show numbers from A to B")
#     print("3. Sum all the numbers from A to B")
#     print("4. exit")
#
#     choice = input("Choose an option: ")
#
#     if choice == "1":
#         n = int(input("Enter the number (1 - 12): "))
#
#         for i in range(1, 13):
#             print(n, "x", i, "=", n*i)
#     elif choice == "2":
#         a = int(input("Enter A: "))
#         b = int(input("Enter B: "))
#         for i in range(a,(b+1)):
#             print(i)
#     elif choice == "3":
#         a = int(input("Enter A: "))
#         b = int(input("Enter B: "))
#         total = 0
#         for i in range(a, (b + 1)):
#             total+=i
#             print("Total: ", total)
#     else:
#         print("Invalid menu option. Must be between 1-4")

# choice = ""
#
# while choice != "4":
#     print("---Pattern Calculator---")
#     print("1. Horizonal line of stars")
#     print("2. Vertical line of stars")
#     print("3. Retangle box of stars")
#     print("4. exit")
#
#     choice = input("Choose an option: ")
#     if choice == "1":
#         n = int(input("How many stars: "))
#         print("*" * n)
#     elif choice == "2":
#         n = int(input("How many stars: "))
#         for i in range(n):
#             print("*")
#     elif choice == "3":
#         h = int(input("Height: "))
#         w = int(input("Width: "))
#         line = "*" * w
#         count = 0
#         while count < h:
#             print(line)
#             count+=1
#     elif choice == "4":
#         print("Exiting")
#         else:
#             print("Invalid menu option. Must be between 1-4")

# choice = ""
# number = 0
#
#
# while choice != "5":
#     print("---Pattern Calculator---")
#     print("1. Horizonal line of stars")
#     print("2. Vertical line of stars")
#     print("3. Retangle box of stars")
#     print("4. exit")
#
#     choice = input("Choose an option: ")
#
#     if choice == "1":
#         print()