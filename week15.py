# guest_list=[]
#
# while len(guest_list)<5:
#     name=input("Enter guest name: ")
#     if name not in guest_list:
#          guest_list.append(name)
#     else:
#          print("That person is already on the list. Try another one." )
# print("Final Guest List: ",guest_list)
#
# name = " John"
# name2 = name
# name += " Smith"
#
# print(name) # John Smith
# print(name2) # John
#
# todo = ["email clients", "prepare slides", "print handouts", "book room"]
# draft =todo[:]    #todo.copy()
# draft.remove("print handouts")
# draft.append("check equipment")
#
# print("Original List: ", todo)
# print("Draft Plan: ", draft)
#
# my_list = [0, 19, 0, 8, 5, 9, 0, 27, 9, 15, 0]
# print(my_list)
#
# if 0 in my_list:
#     total_of_non_zero_values=0
#     num_non_zero_values=0
#     for item in my_list:
#         if item != 0:
#             total_of_non_zero_values+=item
#             num_non_zero_values+=1
#     average_value = total_of_non_zero_values/num_non_zero_values
#
#     for index, item in enumerate(my_list):
#         if item ==0:
#             my_list[index]=round(average_value)
# print(my_list)
#
# my_data = [12.6, 19.2, 15, 13, 9, 51, 3.7, 45, 32, 8.9, 45.7777, 15.10]
# my_data_normalised=[]
# for number in my_data:
#     norm_number= (number-min(my_data))/(max(my_data)-min(my_data))
#     norm_number=round(norm_number,4)
#     my_data_normalised.append(norm_number)
# print(my_data)
# print(my_data_normalised)


# NUM_EMPLOYEES = 2
# NUM_DAYS = 5
# num_over = 0
# sp_numbers = []
# sales_figures = []
#
# target = float(input("Enter the weekly target €"))
#
# for sperson in range(NUM_EMPLOYEES):
#     total_sales_per_person = 0
#     sp_numbers.append(input("Saleperson number: "))
#     print("Daily sales figures: ")
#     for day in range(NUM_DAYS):
#         total_sales_per_person += float(input("Sale figure for day: " + str(day + 1) + "€"))
#     sales_figures.append(total_sales_per_person)
#     if total_sales_per_person > target:
#         difference = total_sales_per_person - target
#         print("Congratulations " + sp_numbers[sperson] + "You exceeded the target by €" + str(round(difference, 2)))
#         num_over += 1
# print("{:20}{:20}".format("Saleperson", "Weekly sales €"))
#
# for index, salesperson in enumerate(sp_numbers):
#     print("{:20}{:<6.2f}".format(salesperson, sales_figures[index]))
# print("\nTotal Weekly Sales €" + str(sum(sales_figures)))
# print("Number of sales person who exceeded their target: ", num_over)