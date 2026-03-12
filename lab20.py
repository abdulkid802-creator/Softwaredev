# class student:
#     def __init__(self, student_id, name, subject, ca1_result, ca2_result):
#         self.student_id = student_id
#         self.name = name
#         self.subject = subject
#         self.ca1_result = ca1_result
#         self.ca2_result = ca2_result
#         self.grade = ""
#
#     def print(self):
#         print("*" * 15)
#         print("*   student   *")
#         print("*" * 15)
#         print("Id", self.student_id)
#         print("Name", self.name)
#         print("Subject", self.subject)
#         print("Ca1", self.ca1_result)
#         print("Ca2", self.ca2_result)
#         print("Grades", self.grade)
#
#     def set_grade(self):
#         average = (self.ca1_result + self.ca2_result) / 2
#         if 80<= average <= 100:
#             self.grade = "A"
#         elif 60<= average <= 79:
#             self.grade = "B"
#         elif 40<= average <= 59:
#             self.grade = "C"
#         else:
#             self.grade = "F"
#     def get_grade(self):
#         return self.grade
#
# student1 = student("X123456", "John Smith", "Software Development", 77, 80)
# student1.print()
# student1.set_grade()
# student1.print()
#
#
# class printcard:
#     def __init__(self, account_number, password, credit):
#         self.account_number = account_number
#         self.password = password
#         self.credit = credit
#
#     def print(self):
#         print("*" * 30)
#         print("*     Print Card Details     *")
#         print("*" * 30)
#         print("Account: ", self.account_number)
#         print("Credit: ", self.credit)
#     def add_bonus(self):
#         self.credit = self.credit + 400
#
#     def get_credits(self):
#         return self.credit
#
# test = printcard(236589, "Txy54", 100)
# test.print()
#
# if student1.get_grade() == "A" or student1.get_grade() == "B":
#     print("Updating credits for average")
#     test.add_bonus()
#     print("Credit: ", test.credit)