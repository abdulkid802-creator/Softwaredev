# # import random
# #
# # class Animal:
# #     def __init__(self, number_id, animal_type):
# #         self.number = number_id
# #         self.type = animal_type
# #     def display_details(self):
# #         print("ID", self.number)
# #         print("Type", self.type)
# #
# # class Greyhound(Animal):
# #     def __init__(self, name, sex, father, mother, litters, pup):
# #         number_id = random.randint(1000, 9999)
# #         super().__init__(number_id, "Greyhound")
# #
# #         self.name = name
# #         self.sex = sex
# #         self.father = father
# #         self.mother = mother
# #         self.litters = 0
# #         self.pup = 0
# #
# #     def update_breeding_record(self, pup_born):
# #         self.litters += 1
# #         self.pup = pup_born
# #
# #     def display_details(self):
# #         super().display_details()
# #         print("Name", self.name)
# #         print("Sex", self.sex)
# #         print("Father", self.father)
# #         print("Mother", self.mother)
# #
# # dog = Greyhound("Mrs Flash", "female", "Tom Foley", "The Late Late Show", 2, 9)
# # dog.update_breeding_record(2)
# # dog.update_breeding_record(4)
# # dog.display_details()
#
# class Employee:
#     def __init__(self, name = "", employee_number = 0, wages_per_hour = 0, hours_worked = 0):
#         self.name = name
#         self.employee_number = employee_number
#         self.wages_per_hour = wages_per_hour
#         self.hours_worked = hours_worked
#
#         if wages_per_hour <= 0:
#             self.wages_per_hour = 0
#         else:
#             self.wages_per_hour = wages_per_hour
#
#     def calculate_salary(self):
#         salary = self.wages_per_hour * self.hours_worked
#         return salary
#
#
#     def print(self):
#         print("Name", self.name)
#         print("employee_number", self.employee_number)
#         print("wages_per_hour", self.wages_per_hour)
#         print("Hours Worked this week", self.hours_worked)
#
# class Trainee(Employee):
#     TRAINEE_PAY = 5
#     def __init__(self, name = "", employee_number = 0, wages_per_hour = 0, hours_worked = 0, training_hours = 0):
#         super().__init__( name, employee_number, wages_per_hour, hours_worked)
#         if training_hours <= 0:
#             self.training_hours = 0
#         else:
#             self.training_hours = training_hours
#
#     def calculate_salary(self):
#         salary = self.wages_per_hour * self.hours_worked
#         trainee_pay = self.TRAINEE_PAY * self.training_hours
#         total_pay = salary + trainee_pay
#         return  total_pay
#
#     def print(self):
#         print("Name", self.name)
#         print("Employee_number", self.employee_number)
#         print("Wages_per_hour", self.wages_per_hour)
#         print("Hours Worked this week", self.hours_worked)
#         print("-" * 40)
#         print("Salary", self.calculate_salary())
#         print("Training_hours", self.training_hours)
#
# trainee = Trainee("John Smith", 1234, 20, 40, 2)
# trainee.print()