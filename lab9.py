# sum = 50
# total = 0
#
# while sum <= 100:
#     total += sum
#     sum += 1
# print(total)
#
# total = 0
#
# for sum in range(50, 101):
#     total += sum
# print("total is",total)

# total = 0

# for value in range(5):
#     num = float(input("enter 5 float numbers: "))
#     total+=num
# avg = total / 5
# print("avg is", avg)

# sum = 0
# sum2 = 0
# for num in range(1,21):
#     if num % 2 != 0:
#         sum += num
#     else:
#         sum2 += num
# print("odd", sum2)
# print("even", sum)

# t_pay_rate = float(input("Enter today price rate of one euro in yen: "))
# euro_amount = float(input("Enter euro amount: "))
# euro_to_yen = 0
#
# while euro_amount != 0:
#     euro_to_yen = euro_amount * t_pay_rate
#     print(euro_to_yen)
#     euro_amount = int(input("Enter euro amount: "))
# print("done")

# start_num = int(input("Enter a starting number: "))
# end_num = int(input("Enter a ending number: "))
# step_num = int(input("Enter the step value: "))
# total = 0
#
# for value in range(start_num, end_num + 1, step_num):
#     total += value
#     print(value)
# print(f"The total of the number from {step_num}, to {end_num}, in step of {step_num} is: {total} ")