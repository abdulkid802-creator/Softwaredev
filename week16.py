# my2D_list = [["Honda", "Civic", "99-D-1234"], ["Nissan", "Pulsar", "01-KE-33456"]]
#
# for i in range(2):
#     car_make = input("Enter the car make: ")
#     car_model = input("Enter the car model: ")
#     car_reg = input("Enter the car reg: ")
#
#     single_car = [car_make, car_model, car_reg]
#     my2D_list.append(single_car)
#
# print(f"{"Make":10}{"Model":10}{"Year":10}")
# print("-"*30)
#
# for row in my2D_list:
#     for col in row:
#         print(f"{col:10}", end= "")
#     print()
#
# league_table = []
#
# for counter in range(4):
#     name = input("Enter team name: ")
#     win = int(input("Enter number of wins: "))
#     draws = int(input("Enter number of draws: "))
#     loses = int(input("Enter number of loses: "))
#     team = [name, win, draws, loses]
#     league_table.append(team)
#
# print("{0:20}{1:10}{2:10}{3:10}{4:10}".format("Team", "Wins", "Draws", "Loses", "Point"))
# print("-"*60)
#
# for team in league_table:
#     for i, information in enumerate(team):
#         if i == 0:
#             print("{0:20}".format(information), end= "")
#         else:
#             print("{0:<10}".format(information), end= "")
#     points = (3 *team[1] + 1 * team[2])
#     print("{0:<10}".format(points))

# league_table = [["Man U", 3, 2, 1], ["Liverpool", 2, 2, 2], ["Spurs", 1, 2, 3], ["Leeds", 0, 3, 3]]
#
# max_wins = max([row[1] for row in league_table])
#
# print(max_wins)

cubes = []
for i in range(5): # i ranges from 0 to 4 incl.
    cubes.append(i ** 3)
print(cubes)