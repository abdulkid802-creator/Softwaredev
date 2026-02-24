# stock = []      # empty list
# stock = [[2323,"pencils",1.5,100],[1010,"pens",2,300]]      # empty list
# print menu (4‑space indent using format)
# print("{:4s}***********************".format(""))
# print("{:4s}*        Menu         *".format(""))
# print("{:4s}***********************".format(""))
# print("{:4s}* 1) Add stock        *".format(""))
# print("{:4s}* 2) Stock list       *".format(""))
# print("{:4s}* 3) Stock List sorted*".format(""))
# print("{:4s}*    (by id number)   *".format(""))
# print("{:4s}* 4) Max stock item   *".format(""))
# print("{:4s}*    (largest qty)    *".format(""))
# print("{:4s}***********************".format(""))
# print("{:4s}* 5) Exit             *".format(""))
# print("{:4s}***********************".format(""))
#
# menu_option = int(input("{:4s}Please enter menu options: ".format("")))
#
# while menu_option != 5:
#     if menu_option == 1:
#         stock_id = input("{:4s}Please enter Stock ID: ".format(""))
#         description = input("{:4s}Please enter description: ".format(""))
#         sales_price = float(input("{:4s}Please enter sales price: ".format("")))
#         qty = int(input("{:4s}Please enter quantity: ".format("")))
#         stock.append([stock_id, description, sales_price, qty])
#     elif menu_option == 2:
#         print("{:4s}***********************".format(""))
#         print("{:4s}*     Stock List      *".format(""))
#         print("{:4s}***********************".format(""))
#         print("{0:4s}{1:10}{2:15}{3:10}{4:10}".format("","ID", "Desc", "RRP", "QTY"))
#
#         for item in stock:
#             print("{0:4s}{1:10}{2:15}{3:10}{4:10}".format("", item[0], item[1], item[2], item[3]))
#
#     elif menu_option == 3:
#         stock.sort()
#         print("{:4s}***********************".format(""))
#         print("{:4s}*  Stock List sorted  *".format(""))
#         print("{:4s}***********************".format(""))
#         print("{0:4s}{1:10}{2:15}{3:10}{4:10}".format("","ID", "Desc", "RRp", "QTY"))
#         for item in stock:
#             print("{0:4s}{1:10}{2:15}{3:10}{4:10}".format("", item[0], item[1], item[2], item[3]))
#
#     elif menu_option == 4:
#         print("{:4s}***********************".format(""))
#         print("{:4s}*    Max List Item    *".format(""))
#         print("{:4s}***********************".format(""))
#         print("{0:4s}{1:10}{2:15}{3:10}{4:10}".format("", "ID", "Desc", "RRP", "Qty"))
#         max_qty = stock[0][3]
#         max_index = 0
#
#         for i, item in enumerate(stock):
#             if item[3] > max_qty:
#                 max_qty = item[3]
#                 max_index = i
#         print("{:4s}Max stock qty: {:5}".format("", max_qty))
#         print("{:4s}Max stock ID: {:5}".format("", stock[max_index][0]))
#
#         qty_list = [row[3] for row in stock]
#         max_stock = max(qty_list)
#         print("{:4s}Max stock qty: {:5}".format("", max_qty))
#         print("{:4s}Max stock ID: {:5}".format("", stock[qty_list.index(max_stock)][0]))
#     else:
#         print(":4s}Please enter number 1-5: ".format(""))
#     print("{:4s}***********************".format(""))
#     print("{:4s}*        Menu         *".format(""))
#     print("{:4s}***********************".format(""))
#     print("{:4s}* 1) Add stock        *".format(""))
#     print("{:4s}* 2) Stock list       *".format(""))
#     print("{:4s}* 3) Stock List sorted*".format(""))
#     print("{:4s}*    (by id number)   *".format(""))
#     print("{:4s}* 4) Max stock item   *".format(""))
#     print("{:4s}*    (largest qty)    *".format(""))
#     print("{:4s}***********************".format(""))
#     print("{:4s}* 5) Exit             *".format(""))
#     print("{:4s}***********************".format(""))
#
#     menu_option = int(input("{:4s}Please enter menu options: ".format("")))

# from statistics import mean
#
# salaries_2Dlist = [[40000.00,45000.00,55000.00], [35000.00,47500.00,53000.00], [47000.00, 52500.00,58000.00]]
#
# print("*" * 50)
# print(" " * 15)
# print("*" * 50)
# print(f"{"Year 1":15}{"Year 2":15}{"Year 3":15}")
# print("*" * 50)
#
# for sal in salaries_2Dlist:
#     print(f"{sal[0]}{sal[1]:15}{sal[2]:15}")
#
# year1_list = [row[0] for row in salaries_2Dlist]
# average_year1 = mean(row[0] for row in salaries_2Dlist)
# average_year1 = round(average_year1, 2)
#
# year2_list = [row[1] for row in salaries_2Dlist]
# average_year2 = mean(row[1] for row in salaries_2Dlist)
# average_year2 = round(average_year2, 2)
#
# year3_list = [row[2] for row in salaries_2Dlist]
# average_year3 = mean(row[2] for row in salaries_2Dlist)
# average_year3 = round(average_year3, 2)
#
# print("Average for year 1 €"+ str(average_year1))
# print("Average for year 2 €"+ str(average_year2))
# print("Average for year 3 €"+ str(average_year3))
#
# NUM_YEARS =3
#
# for year in range(NUM_YEARS):
#     year_list = [row[year] for row in salaries_2Dlist]
#     average_year = mean(year_list)
#     average_year = round(average_year, 2)
#     print("Average for year" + str(year + 1) + " €" + str(average_year))
# print()
#
# averages = [mean(row) for row in salaries_2Dlist]
#
# for index, average in enumerate(averages):
#     print("Average for employee " + str(index + 1) + " €" + str(round(average, 2)))
#
# max_value = max(averages)
# print("Highest Average earned € " + str(max_value))
# print("Earned by employee # " + str(averages.index(max_value) + 1))
# print()
#
# for index, row in enumerate(salaries_2Dlist):
#     print("Increase in salary for employee "
#           + str((index + 1)) + " €" + str(row[-1] - row[0]))
#
# MIN = 1
# MAX = 3
# update = True
#
# while update:
#     emp_no = int(input("Employee number: 1...3 "))
#     while emp_no < MIN or emp_no > MAX:
#         emp_no = int(input("RE-ENTER Employee number: 1...3 "))
#
#     year_no = int(input("Year number: 1...3 "))
#     while emp_no < MIN or emp_no > MAX:
#         year_no = int(input("RE-ENTER Year number: 1...3 "))
#     new_salary = float(input("New Salary €"))
#     salaries_2Dlist[emp_no - 1][year_no - 1] = new_salary
#     another = input("Another update y/n: ")
#
#     if another != "y":
#         update = False