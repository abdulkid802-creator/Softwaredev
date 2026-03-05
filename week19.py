# x = [1, 2, 3]
# print(id(x)) # prints 8009128
# y = x
# print(id(y)) # prints 8009128
# y[0] = 9
# print(x)
# print(y)

# def print_number(my_list):
#     my_list[3] = 33
#     print(my_list)
# # main code
# my_list = [1, 2, 3, 4] # Global Variable
# print_number(my_list)
# print(my_list)

# def print_number(my_list):
#     my_local_list = my_list[:] # Deep copy to local variable
#     print(id(my_list)) #4994472
#     print(id(my_local_list)) #4995632
#     print(my_local_list) #[1, 2, 3, 4]
#     my_local_list[0] = 99
#     print(my_local_list) # [99, 2, 3, 4]
# # main code
# my_list = [1, 2, 3, 4] # Global Variable
# print_number(my_list)
# print(my_list) # my_local_list not accessible [1, 2, 3, 4]

# def volume_of_a_sphere(radius):
#     volume = (4.0 / 3.0) * 3.14 * (radius ** 3)
#     print("The volume of the sphere is", volume)
#     return volume
# volume = volume_of_a_sphere(6371000)
# mass = volume * 5515.3
# print("Mass of earth is:", mass, "KG")

# def compound_interest(principal_amount, interest_rate, years=1):
#     amount = principal_amount * ((1 + (interest_rate / 100)) ** years)
#     return amount
#
# principal_amount = float(input("Enter principal amount: "))
# total_amount = compound_interest(principal_amount, interest_rate= 3.23, years= 5)
# total_amount = round(total_amount)
# print("Total Amount: ", total_amount)
# print("Interest: ", total_amount - principal_amount)

# def square(num=1):
#     return num*num
# square_value = square(10)
# print("Square: ", square_value)
#
# square_value = square()
# print("Square: ", square_value)

# def min_max(my_list):
#     return max(my_list), min(my_list)
# #ensure you have enough variables specified to catch the returned values
# nums = [10,20,30,40]
# max_num, min_num, = min_max(nums)
# print("The maximum value in the list : ",max_num)
# print("The minimum value in the list : ",min_num)

# def sum_row(list_in):
#     totals = []
#     for row in list_in:
#         total = sum(row)
#         totals.append(total)
#     return totals
#
# nums = [[1,2,3,4], [5,6,7,8],[9,10,11,12]]
# returned_list = sum_row(nums)
# print(returned_list)
# print(sum_row(nums))

# def is_valid_code(code_in):
#     valid_code = ["pt", "ft", "s"]
#     if code_in.lower() in valid_code:
#         return True
#     else:
#         return False
# user_code = input("Worker's code: ")
# user_valid = is_valid_code(user_code)
#
# while not user_valid:
#     user_code = input("Invalid RE-Enter Worker's code: ")
#     user_valid = is_valid_code(user_code)
# print(user_valid, "is valid. Please continue. ")
#
# while not is_valid_code(user_code):
#     user_code = input("Invalid RE-Enter Worker's code: ")
# print(user_valid, "is valid. Please continue. ")

# def apply_discount(rrp, discount_pc=0):
#     sale_price = rrp *(1-(discount_pc/100))
#     return sale_price
# price = apply_discount(rrp=100, discount_pc= 50)
# print(price)
# price = apply_discount(100)
# print(price)

# def list_contains(list_in, value):
#     occurrences = 0
#     for item in list_in:
#         if item == value:
#             occurrences += 1
#     if occurrences > 1:
#         return True
#     else:
#         return False
# my_list = [1, 2, 3, 4, 4, 9]
# user_number = int(input("Enter Number: "))
#
# # in_list = list_contains(my_list, user_number)
# # if in_list == True:
#
# if list_contains(my_list, user_number):
#     print(user_number, "is in the list more than once")
# else:
#     print(user_number, "is not in the list more than once")

# def determine2d_max(list_in):
#     max_row = [max(row) for row in list_in]
#     print(max_row)
#     return max(max_row)
# nums = [[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12]]
# max_number = determine2d_max(nums)
# print("The max value in the 2D list: ", max_number)
