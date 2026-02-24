# a = int(input("enter the integer value a "))
# b = int(input("enter the integer value b "))
# c = int(input("enter the integer value c "))
# n = int(input("enter the integer value n "))
#
# lhs_answer = (a**n)+(b**n)
# rhs_answer = c**n
#
# if n > 2:
#     if lhs_answer == rhs_answer:
#         print("Fermat's theorem does not hold true")
#     else:
#         print("Fermat's theorem does hold true")
# else:
#     print("n must the greater than 2")
#
# if n > 2 and lhs_answer == rhs_answer:
#     print("Fermat's theorem does not hold true")

# import time
# print(time.strftime("%H:%M:%S."))

# side1 = float(input("enter the first side size: "))
# side2 = float(input("enter the second side size: "))
# side3 = float(input("enter the third side size: "))
#
# if side1 > side2 and side1 > side3:
#     if ((side2**2)+(side3**2)) == (side1**2):
#         print("Your can make a right angled triangle ")
#     else:
#         print("You cannot make a right angled triangle")
# elif side2 > side1 and side2 > side3:
#     if ((side1 ** 2) + (side2 ** 2)) == (side2 ** 2):
#         print("Your can make a right angled triangle ")
#     else:
#         print("You cannot make a right angled triangle")
# else:
#     if ((side1 ** 2) + (side2 ** 2)) == (side3 ** 2):
#         print("Your can make a right angled triangle ")
#     else:
#         print("You cannot make a right angled triangle")
#
#
# side1 = float(input("Input the first side :"))
# side2 = float(input("Input the second side :"))
# side3 = float(input("Input the third side :"))
# if side1 > side2 and side1 > side3:
#     if ((side2 ** 2) + (side3 ** 2)) == (side1 ** 2):
#         print("You can make a right angle triangle from these sides")
#     else:
#         print("You cannot make a right angle triangle from these sides")
# elif side2 > side1 and side2 > side3:
#     if ((side1 ** 2) + (side3 ** 2)) == (side2 ** 2):
#         print("You can make a right angle triangle from these sides")
#     else:
#         print("You cannot make a right angle triangle from these sides")
# else:
#     if ((side1 ** 2) + (side2 ** 2)) == (side3 ** 2):
#         print("You can make a right angle triangle from these sides")
#     else:
#         print("You cannot make a right angle triangle from these sides")


# import random
# the_number = random.randint(1, 100)
# guess = int(input("Guess a number between 1 and 100: "))
#
# if guess > the_number:
#     print("too high")
# elif guess < the_number:
#     print("too low")
# else:
#     print("You guessed correctly")

# username = input("Enter username: ")
# password = input("Enter password: ")
# is_banned = False
# is_suspended = False
#
# if not (username == "" or password == "" or is_banned or is_suspended):
#     print("Access granted")
# else:
#     print("Access denied")