# correct_username = "Admin"
# correct_password = "AD2025"
# print("Welcome to Dublin Football League Analysis System \nWelcome Screen")
# username = input("Enter a username: ")
# password = input("Enter a password: ")
#
# if username != correct_username or password != correct_password:
#     print("Access Denied")
# else:
#     print("Access Granted")
#     choice = ""
#     pay_per_goal = 49.50
#     extra_pay = 100.50
#
#     # Variables to store striker details
#     name1 = ""
#     name2 = ""
#     goals1 = None
#     goals2 = None
#
#     while choice != "3":
#         print("--- MAIN MENU ---")
#         print("1. Enter Striker Details & Calculate Pay")
#         print("2. Determine Player for Promotional Function")
#         print("3. Exit")
#
#         choice = input("Choose an option: ")
#
#         if choice == "1":
#             team_pay = 0
#
#             print("Striker 1")
#             name1 = input("Enter name: ")
#             goals1 = int(input("Enter goals scored this week: "))
#             pay1 = pay_per_goal * goals1
#             if goals1 >= 3:
#                 pay1 += extra_pay
#                 print("BONUS AWARDED: Player has earned the goal bonus!")
#                 print(f"Pay for {name1}: €{pay1}")
#             else:
#                 print("€", pay1)
#             team_pay += pay1
#
#             print("Striker 2")
#             name2 = input("Enter name: ")
#             goals2 = int(input("Enter goals scored this week: "))
#             pay2 = pay_per_goal * goals2
#             if goals2 >= 3:
#                 pay2 += extra_pay
#                 print("BONUS AWARDED: Player has earned the goal bonus!")
#                 print(f"Pay for {name2}: €{pay2}")
#             else:
#                 print("€", pay2)
#             team_pay += pay2
#
#             print(f"Total striker pay for the team: €{team_pay}")
#
#         elif choice == "2":
#             import random
#             if goals1 is None or goals2 is None:
#                 print("Error: Please enter striker details first (Option 1).")
#             else:
#                 if goals1 > goals2:
#                     print(f"{name1} will represent the league at the promotional function this week.")
#                 elif goals2 > goals1:
#                     print(f"{name2} will represent the league at the promotional function this week.")
#                 else:
#                     chosen = random.choice([1, 2])
#                     if chosen == 1:
#                         print(f"{name1} will represent the league at the promotional function this week.")
#                     else:
#                         print(f"{name2} will represent the league at the promotional function this week.")
#
#         elif choice == "3":
#             print("Program ending. Goodbye!")
#
#         else:
#             print("Invalid selection. Please try again.")
