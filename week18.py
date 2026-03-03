# def display_pi():
#     PI = 22.0/7.0
#     print("PI = ", PI)
#
# for i in range(5):
#     display_pi()
#
# import time
#
# def current_time():
#     time_now = time.strftime("%H:%M:%S")
#     print(time_now)
#
# for i in range(5):
#     current_time()
#
# def square_number(number_in):
#     ans = number_in ** 2
#     print(ans)
# # main body of code
# number = float(input("Please enter number to be squared: "))
# square_number(number)
#
# def largest_number(number1_in, number2_in):
#     if number1_in > number2_in:
#         print("The largest number is :", number1_in)
#     elif number2_in > number1_in:
#         print("The largest number is :", number2_in)
#     else:
#         print("The two numbers are equal")
# number1 = float(input("Please enter first number:"))
# number2 = float(input("Please enter second number:"))
# largest_number(number1, number2)

# def print_values(n1, n2):
#     nums = []
#     for i in range(n1, n2 + 1):
#         nums.append(i ** 2)
#     print(nums)
# print_values(1,4)

# def count_vowels(string_in):
#     vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
#     count = 0
#     for character in string_in:
#         if character in vowels:
#             count+=1
#     print("The number of vowels in {0} is {1}".format(string_in, count))
#
# # main body of code
# count_vowels("Python Programming")
# user_input = input("Enter String: ")
# count_vowels(user_input)

# def print_employee_status(name_in, status_in):
#     valid_status = ["FT", "PT", "S"]
#
#     if status_in in valid_status:
#         print(name_in, " has a valid status of: ", )

# def compound_interest(principal_amount, interest_rate, years = 1):
#     amount = principal_amount * ((1 +(interest_rate / 100)) ** years)
#     amount = round(amount, 2)
#     print("Amount: ", amount)
#
# compound_interest(principal_amount= 100, interest_rate= 10)
#
# def check_date(day=1, month=1):
#     num_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if day > num_days[month -1]:
#         print("Illegal day number of month, only {} days in that month".format(num_days[month-1]))
#     else:
#         print("Legal day value within month range")
#
# check_date(day= 32, month= 3)
# check_date()