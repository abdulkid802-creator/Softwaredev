# import random
#
# lotto_numbers = []
# user_numbers = []
#
# for number in range(6):
#     lotto_numbers.append(random.randint(1, 47))
#
# for number in range(6):
#     user_numbers.append(int(input("Input lotto number: ")))
#
# correct_guesses = 0
# for user_number in user_numbers:
#     for lotto_number in lotto_numbers:
#         if user_number == lotto_numbers:
#             correct_guesses += 1
#
# print("Lotto Number: ", lotto_numbers)
# print("Your Number: ", user_numbers)
# print("Correct guesses: ", correct_guesses)
#
# sales = []
# sales_amount = float(input("Enter sales amount or 0 to exit: "))
# while sales_amount != 0:
#     sales.append(sales_amount)
#     sales_amount = float(input("Enter sales amount or 0 to exit: "))
# print("Individual Sales")
# print(".........................")
# print(sales)
#
# counter = 1
#
# for sale in sales:
#     print("sale: ", str(counter)+"€", str(sale))
#     counter += 1
# min = sales[0]
# max = sales[0]
# total = 0
#
# for sale in sales:
#     total += sale
#     if sale > max:
#         max = sale
#     if sale > min:
#         min = sale
#
# avrage = total/len(sales)
#
# print("Total: ", total)
# print("Max: ", max)
# print("Min: ", min)
# print("Average: ", avrage)
#
# my_list = [1, 19, 27, 8, 5, 1, 9]
# search_key = 1
# count_key = 0
# for index in range(len(my_list)):
#     if my_list[index] == search_key:
#         count_key += 1
#         print("Found at index: ", index)
# print("Occurs: ", count_key, "times")
#
# my_list = [1, 19, 27, 8, 5, 1, 9]
# print(my_list)
# index = 0
#
# while index < len(my_list):
#     if my_list[index] < 10:
#         my_list[index] = 10
#     index += 1
# print(my_list)
#
# my_list = [1, 19, 27, 8, 5, 1, 9]
# print(my_list)
#
# for item in my_list:
#     if item < 10:
#         my_list[my_list.index(item)] = 10
# print(my_list)
#
# my_list = [1, 19, 27, 8, 5, 1, 9]
# print(my_list)
# for index, item in enumerate(my_list):
#     if item < 10:
#         my_list[index] = 10
# print(my_list)
#
# from statistics import mean
#
# student_names = []
# student_grades = []
#
# num_student = int(input("Enter number of students: "))
#
# for student in range(num_student):
#     temp_name = input("Enter name: ")
#     student_names.append(temp_name)
#     temp_grade = float(input("Enter student grade: "))
#     student_grades.append(temp_grade)
#
# print("---------------Class Summary-----------------")
# print(f"{"Class Summary":-^30}")
#
# for index, student in enumerate(student_names):
#     print("{0:25} {1:4}".format(student, student_grades[index]))
#
# print(f"{"Class Scores":-^15}")
# print("Average: ", round(mean(student_grades),2))
# print("Max: ", round(max(student_grades),2))
# print("Min: ", round(min(student_grades),2))