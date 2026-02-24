# counter = 0
# while counter < 101:
#     print(counter)
#     counter += 2


# counter = 0
# total = 0
# while counter < 101:
#     total += counter
#     print(counter)
#     counter += 2
# print(total)

# total = 0
# number = 1
# while total <= 1000000:
#     total = total + number
#     number = number + 1
#     print(total)

# product = 1
# number = 1
# count = 20
# last_number = 2 * count - 1
#
# while number <= last_number:
#     product = product * number
#     number = number + 2
#     print(product)

# total = 0
# number= 0
# while number<=5:
#     print(number)
#     total=total+number
#     number=number+1
# print("Total of number 0-5 incl.:",total)

# import math
#
# radius = float(input("Enter radius - must be > 0: "))
#
# while radius < 0:
#     radius = float(input("Error Re-Enter radius - must be > 0: "))
# area = math.pi*(radius **2 )
# area = round(area, 4)
# print("Area of circle is: ", area)

# mark = float(input("Enter mark - must be between 0-100: "))
#
# while mark <0 or mark > 100:
#     mark = float(input("Error mark must be between 0-100: "))
# print("your mark is: ", mark)

# age = int(input("Enter age between 0 and 129 incl: "))
#
# while age <0 or age >129:
#     age = int(input("Error Re Enter age between 0 and 129 incl: "))
# print("Age is: ", age)

# SENTINEL = 0
# total = 0
# input_number = int(input("Enter 1st Number: "))
#
# while input_number != SENTINEL:
#     total += input_number
#     input_number = int(input("Enter the next number: "))
# print("total is: ", total)

# secret_number = 7
# is_running = True
#
# while is_running:
#     guess = int(input("Guess the number between 1 and 10: "))
#     if guess == secret_number:
#         print("Correct")
#     elif guess < secret_number:
#         print("Too low")
#     else:
#         print("Too high")
# print("Exiting program")
