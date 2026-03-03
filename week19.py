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

def min_max(my_list):
    return max(my_list), min(my_list)
#ensure you have enough variables specified to catch the returned values
nums = [10,20,30,40]
max_num, min_num, = min_max(nums)
print("The maximum value in the list : ",max_num)
print("The minimum value in the list : ",min_num)