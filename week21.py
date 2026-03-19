# class Robot:
#     number_of_robot = 0
#     def __init__(self, name_in = None, number_of_legs_in = None):
#         if name_in is not None:
#             self.name = name_in
#         else:
#             self.name = "Not set"
#         if number_of_legs_in is not None:
#             self.number_of_legs = number_of_legs_in
#         else:
#             self.number_of_legs = 0
# user_name = input("Robot name: ")
# user_number_of_legs = int(input("Robot number of legs: "))
#
# r5 = Robot(user_name, user_number_of_legs)
# print("Robot 5")
# print(r5.name)
# print(r5.number_of_legs)

# class Student:
#     def __init__(self, name_in=None, fees_in=None):
#         if name_in is not None:
#             self.name = name_in
#         if fees_in is not None and fees_in > 0:
#             self.fees_in = fees_in
#         else:
#             self.fees_in = 15000
#     def print_details(self):
#         print("Student Name: ", self.name)
#         print("Student Fees: ", self.fees_in)
# # main body
# student1 = Student("John Smith", 10000)
# student1.print_details()

# class MotorBike:
#     def __init__(self, make_in=None):
#         if make_in is not None:
#             self.make = make_in
#         else:
#             self.make = "Unknown Make"
#         self.current_gear = 0
#     def up_gear(self):
#         if self.current_gear<6:
#             self.current_gear += 1
#     def down_gear(self):
#         if self.current_gear>0:
#             self.current_gear -= 1
#     def print_details(self):
#         print("Make: ",self.make)
#         print("Current Gear: ",self.current_gear)
# # main body
# mb1=MotorBike("Yamaha")
# mb1.print_details()
# mb1.up_gear()
# mb1.up_gear()
# mb1.up_gear()
# mb1.down_gear()
# mb1.print_details()
# for i in range(100):
#     mb1.up_gear()
# mb1.print_details()

# class DebitCard:
#     def __init__(self):
#         self.balance = 10
#     def lodge(self,amount):
#         if amount > 0:
#             self.balance += amount
#             return True
#         else:
#             return False
#     def withdraw(self,amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             return True
#         else:
#             return False
#
#     def print_details(self):
#         print("Balance :", self.balance)
#
# my_acc = DebitCard()
# my_acc.print_details()
# if my_acc.withdraw(2):
#     print("Money withdrawn successfully")
# else:
#     print("Error, not enough funds")
# my_acc.print_details()
# if my_acc.lodge(180):
#         print("Money Lodged successfully")
# else:
#     print("Error - contact bank")
# my_acc.print_details()

# class Person:
#     def __init__(self, name_in, age_in):
#         self.name = name_in
#         self.__age = age_in
#     def print_details(self):
#         print("Name :", self.name)
#         print("Age :", self.__age)
# # main code
# p1 = Person("John Smith", 33)
# p1.name = "Mr. John Smith"
# p1.age = 34
# p1.print_details()
# print(p1.name)
