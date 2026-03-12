# class car:
#     def __init__(self):
#         print("A new car as been created")
#     def speak(self):
#         print("I am an instance of the class car")
#
# mercedes = car()
# bmw = car()
# audi = car()
# mercedes.speak()
# bmw.speak()
# audi.speak()

# class Robot:
#     def __init__(self, name_in, number_of_legs):
#         self.name = name_in
#         self.number_of_legs = number_of_legs
#         print("I am alive")
#
# r1 = Robot(name_in= "Asimov", number_of_legs= 2)
# print("Name: ", r1.name)
# print("Legs: ", r1.number_of_legs)
# r2 = Robot(name_in= "Capricorn", number_of_legs= 4)
# print("Name: ", r2.name)
# print("Legs: ", r2.number_of_legs)

# class Car:
#     def __init__(self, make_in, model_in, cc_in):
#         self.make = make_in
#         self.model = model_in
#         self.cc = cc_in
#
#     def print(self):
#         print("{:^40}".format("Car's Details"))
#         print("{:^40}".format("Make: " + self.make))
#         print("{:^40}".format("Model: " + self.model))
#         print("{:^40}".format("CCs: " + str(self.cc)))
#
# my_car = Car("Volvo", "590", 1200)
# your_car = Car("BMW", "300", 1100)
#
# my_car.print()
# print()
# your_car.print()

# class Robot:
#     number_of_robot = 0
#     def __init__(self, name_in = None, number_of_legs_in = None):
#         if name_in is not None:
#             self.name = name_in
#         else:
#             self.name = "Not set"
#         if number_of_legs_in is not None:
#             self.number_of_legs_in = number_of_legs_in
#         else:
#             self.number_of_legs_in = 0
#
# print("Number of Robots", Robot.number_of_robot)
# print("Robot 1")
# r1 = Robot("Asimov", 2)
# print(r1.name)
# print(r1.number_of_legs_in)
# r2 = Robot(number_of_legs_in= 6)
# print(r2.name)
# print(r2.number_of_legs_in)
# r3 = Robot()
# print(r3.name)
# print(r3.number_of_legs_in)