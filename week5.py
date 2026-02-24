# age = int(input("Enter your age: "))
# if age > 17:
#     print("you are eligible to apply for a driving licence")
# elif age == 17:
#     print("you are just about eligible to apply for a driving licence")
# else:
#     print("you are not eligible to appy for a driving licence")
#
# hours = int(input("Enter hours: "))
# rate_of_pay = float(input("Enter rate of pay: "))
# pay = hours * rate_of_pay
# if hours > 40:
#     pay += ((hours - 40) * rate_of_pay * 5 )
# print(f"you worked {hours} at a rate of {rate_of_pay:.2f} per hour")
# print(f"your earned {pay:.2f} euros")
# print(f"your earned {round(pay, 2)} euros")

# tax = 25.0
# TAX_BRACKET = 300.0
#
# hours_worked = int(input("Enter the number of hours worked - whole number: "))
# rate_of_pay = float(input("Enter the hourly pay rate: "))
#
# gross_pay = hours_worked * rate_of_pay
#
# if gross_pay > TAX_BRACKET:
#     net_pay = gross_pay - tax
# else:
#     net_pay = gross_pay
# print(f"You worked {hours_worked} hours at a rate of {rate_of_pay} Euro per hour")
# print(f"You earned €{gross_pay: 2f} Euro gross pay")
# print(f"You earned €{net_pay: 2f} Euro net pay")

# gpa = float(input("Enter your Grade Point Average or GPA: "))
# num_passes = 0
# num_fails = 0
# num_merits = 0
#
# if gpa < 2.0:
#     print("You have failed - try again")
#     num_fails += 1
# elif gpa < 2.5:
#     print("You received a Pass")
#     num_passes += 1
# else:
#     print("You have received a Merits")
#     num_merits += 1
#
# print("Number of Fails: ", num_fails)
# print("Number of Passes: ", num_passes)
# print("Number of Merits: ", num_merits)


# number = int(input("Enter a whole number: "))
# remainder = number % 2
#
# if remainder == 0:
#     print("Number is even")
#     print(f"The number {number} is even")
# else:
#     print("Number is odd")
#
# email = input("Enter email address: ")
# if "@" in email:
#     print("@ present")
# else:
#     print("@ not present")