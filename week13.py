# # import random
# #
# # lotto_number = []
# # user_numbers = []
# #
# # for number in range(6):
# #     lotto_number.append(random.randint(1, 47))
# #
# # for number in range(6):
# #     user_numbers.append(int(input("Enter lotto number: ")))
# #
# # correct_guesses = 0
# #
# # for user_numbers in user_numbers:
# #     for lotto_number in lotto_number:
# #         if user_numbers == lotto_number:
# #             correct_guesses += 1
# #
# # print("Lotto Number: ", lotto_number)
# # print("Your Number: ", user_numbers)
# # print("Correct Guesses: ", correct_guesses)
#
#
# sales = []
# sales_amount = float(input("Enter sales amount or 0 to exit: "))
#
# while sales_amount != 0:
#     sales.append(sales_amount)
#     sales_amount = float(input("Enter sales amount or 0 to exit: "))
#
# print("Individual sale")
# print("----------------")
#
# counter = 1
#
# for sales in sales:
#     print("sale " + str(counter) + "€" + str(sales))
#     counter += 1
#
# for index in range(len(sales)):
#     print("Sale ", (index + 1), "€", sales[index])
#
# min = sales[0]
# max = sales[0]
# total = 0
#
# for sale in sales:
#     total += sale
#     if sale > max:
#         max = sale
#     if sale < min:
#         min = sale
#
# average = total / len(sales)
# print("Total: ", total)
# print("Min: ", min)
# print("Max: ", max)
# print("Average: ", average)