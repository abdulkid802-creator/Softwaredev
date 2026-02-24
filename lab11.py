# male = 0
# female = 1
# option = input("Enter y to calculate a height anything else to exit: ").lower()
# feet_in_inches = 12
#
# while option == "y":
#     while True:
#         gender = int(input("Enter the gender of child 1 for female 0 for male: "))
#         if gender == male or gender == female:
#             break
#         else:
#             print("Error please re-enter")
#     mother_height_feet = int(input("Enter mother height in feets: "))
#     mother_height_inches = int(input("Enter mother height in inches: "))
#     father_height_feet = int(input("Enter father height in feets: "))
#     father_height_inches = int(input("Enter father height in inches: "))
#
#     hmother = (mother_height_feet * feet_in_inches ) + mother_height_inches
#     hfather = (father_height_feet * feet_in_inches ) + father_height_inches
#
#     if gender == male:
#         Hmale_child = ((hmother * 13 / 12) + hfather) / 2
#         feet = Hmale_child // feet_in_inches
#         inches = Hmale_child % feet_in_inches
#         print(f"Your future child is estimated to grow to {feet} feet and {inches} inches")
#     elif gender == female:
#         Hfemale_child = ((hfather * 12 / 13) + hmother) / 2
#         feet = int(Hfemale_child // feet_in_inches)
#         inches = int(Hfemale_child % feet_in_inches)
#         print(f"Your future child is estimated to grow to {feet} feet and {inches} inches")
#     option = input("Enter y to calculate a height anything else to exit: ").lower()
# print("GoodBye")