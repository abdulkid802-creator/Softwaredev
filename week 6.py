# age = int(input("Please enter your age: "))
# has_provisional = input("Do you have a provisional license (y/n): ")
#
# if age >= 17:
#     if has_provisional == "y":
#         print("You are eligible for a driving license")
#     else:
#         print("You are not eligible for a driving license")
# else:
#     print("You are not eligible for a driving license")
#
# age = int(input("Please enter your age: "))
# test_score = int(input("Please enter your score: "))
#
# if test_score >= 80:
#     if age <= 16:
#         print("Excellent")
#     else:
#         print("Your good")
# else:
#     print("Try again next time")
# COST = 57.23
# num_products = float(input("Enter the number of products purchased: "))
# gold_customer = input("Are you a gold customer (y/n): ")
#
# if gold_customer == "y":
#    gold_customer = True
# else:
#     gold_customer = False
#
# if gold_customer:
#     if num_products < 25:
#         total = (COST * num_products) * (1-.035)
#         print(f"Your total is {total} including a gold discount of 3.5% but no quantity discount was applied")
#     elif num_products < 100:
#         total = (COST * num_products) * (1 -(.035 + .05))
#         print(f"Your total is {total} including a gold discount of 3.5% and a quantity discount of 5%")
#     else:
#         total = (COST * num_products) * (1 - (.035 + .1))
#         print(f"Your total is {total} including a gold discount of 3.5% and a quantity discount of 10%")
# else:
#     total = (COST * num_products)
#     print(f"Your total is {total} no discount was applied to this order")

# x = 30
# y = 10
# if x == 30:
#     if y == 10:
#         print("Both x is 30 and y is 10")
#     else:
#         print("x is 30 but y is not 10")
# else:
#     print("x is not 30")
#
# num = int(input("Enter a number >= 0: "))
# if num < 10:
#     if num % 2 != 0:
#         print(f"the number {num} is a single digit number and is odd")
#     else:
#         print(f"the number {num} is a single digit number and is not odd")
# else:
#     print(f"the number {num} is a single not digit number")
