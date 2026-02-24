# length_of_rectangle = float(input("Enter the length of the rectangle: "))
#
# while length_of_rectangle <0:
#     length_of_rectangle = float(input("error Length must be greater than 0 please try again: "))
# width_of_rectangle = float(input("Enter the width of the rectangle: "))
#
# while width_of_rectangle <0:
#     width_of_rectangle = float(input("error Width must be greater than 0 please try again: "))
# area = length_of_rectangle * width_of_rectangle
# print("the area of the rectangle is", area)
#
# costumer_screening = input("Are u a costumer for screening (enter yes or no): ")
# total = 0
#
# while costumer_screening == "yes":
#     costumer_age = int(input("Enter your age: "))
#     if costumer_age < 18:
#         ticket_pay = 2.50
#         print("your price is", ticket_pay)
#         total += ticket_pay
#     else:
#         ticket_pay = 5.50
#         print("your price is", ticket_pay)
#         total += ticket_pay
#     costumer_screening = input("Are u a costumer for screening (enter yes or no): ")
# print("total takings", total)