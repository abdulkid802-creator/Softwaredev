# from statistics import mean
#
# rainfall = []
# total_rainfall = 0
#
# for day in range(7):
#     print("Day", (day + 1), end= "")
#     daily_rainfall = float(input("- Please enter rainfall: "))
#     rainfall.append(daily_rainfall)
#     total_rainfall += daily_rainfall
# print(f"Average: {mean(rainfall):.2f}")
# print(f"Total rainfall {total_rainfall:.2f}mm")
#
# for index, daily_rainfall in enumerate(rainfall):
#     if daily_rainfall > 3.5:
#         print(f"Rainfall exceed 3.5mm on day {index + 1}")
#
# my_list = []
#
# for item in range(5):
#     num = int(input("Please enter number: "))
#     my_list.append(num)
# print(my_list)
#
# for item in range(len(my_list)):
#     my_list[item] += 1
# print(my_list)
#
# from statistics import mean
#
# name = []
# sale = []
# sales_people = int(input("Enter the number of sales people: "))
#
# for sales in range(sales_people):
#     temp_name = input("Enter your name: ")
#     name.append(temp_name)
#     temp_sales = float(input("Enter your sales: "))
#     sale.append(temp_sales)
# print("Sales person \t\t Sales €")
# print("------------------------------")
#
# for i in range(sales_people):
#     print(f"{name[i]} \t\t\t\t\t €{sale[i]}")
# print("-----------Summary------------")
# print(f"Total sales €{sum(sale)}")
# print(f"Average: ", round(mean(sale),2))
# print("Max: ", round(max(sale),2))
# print("Min: ", round(min(sale),2))
#
