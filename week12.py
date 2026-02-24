# number = 1
#
# for iteration in  range(1, 13):
#     ans = number * iteration
#     print(number, "X", iteration, "\t", ans)
#     print()
#
# number = 2
#
# for iteration in range(1, 13):
#     ans = number * iteration
#     print(number, "X", iteration, "\t", ans)
#     print()
#
# number = 3
#
# for iteration in  range(1, 13):
#     ans = number * iteration
#     print(number, "X", iteration, "\t", ans)
#     print()
#
# for number in range(1, 4):
#     for iteration in range(1, 4):
#         ans = number * iteration
#         print(number, "X", iteration, "\t", ans)
#     print()
#
# for number in range(1, 13):
#     for iteration in range(1, 13):
#         ans = number * iteration
#         print(number, "X", iteration, "\t", ans)
#     print()
#
# rows = int(input("Enter the numbers or rows: "))
# cols = int(input("Enter the numbers or cols: "))
#
# for row in range(rows):
#     for col in range(cols):
#         print("*", end= "")
#     print()
#
# rows = int(input("Enter the numbers or rows: "))
# for row in range(rows):
#     for col in range(rows+1):
#         print("*", end="")
#     print()
#
# price_per_metre = float(input("Please enter the price per metre of the office space: "))
# print("\t\t\t5m\t\t\t10m\t\t\t15m\t\t\t 20m\t\t\t 25")
# for length in range(10, 101, 10):
#     print(length, "m\t", end="")
#     for width in range(5, 26, 5):
#         price = length * width * price_per_metre
#         price = round(price,2)
#         print("€", price, end= "\t")
#     print()
#
# import sys
#
# max1 = sys.float_info.min
# min1 = sys.float_info.max
# total1 = 0
# total2 = 0
# num_of_student = int(input("Enter number of student: "))
#
# for student in range(num_of_student):
#     print("Student Number ", (student + 1))
#     for subject in range(2):
#         if subject == 0:
#             result = float(input("enter mark for subject 1: "))
#             total1 = result
#             if result > max1:
#                 max1 = result
#             if result < min1:
#                 min1 = result
#         else:
#             total2 += float(input("Enter mark for subject 2: "))
#
# avg1 = total1/num_of_student
# avg2 = total1/num_of_student
#
# print("Average mark for subject 1 is: ", round(avg1, 2))
# print("Average mark for subject 2 is: ", round(avg2, 2))
# print("Lowest mark: ", min1)
# print("Highest mark: ", max1)
#
# total_sale_euro = 0
# total_sale_qty = 0
# total_items_sold = 0
#
# items_for_this_sale = int(input("Enter number of items in this sale or 0 to exit: "))
#
# while items_for_this_sale != 0:
#     total_sale_qty += 1
#     for sale_item in range(items_for_this_sale):
#         total_items_sold += 1
#         total_sale_euro += float(input("Enter item price: "))
#     items_for_this_sale = int(input("Enter number of items in this sale or 0 to exit: "))
#
# avg_sale_euro = total_sale_euro / total_sale_qty
# avg_item_per_sales = total_items_sold / total_sale_qty
#
# print("Total sales: ", total_sale_euro)
# print("Average spend per sale: ", avg_sale_euro)
# print("Average items sold per sale: ", avg_item_per_sales)
#
