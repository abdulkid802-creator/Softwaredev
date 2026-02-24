# from statistics import mean
#
# travelled_distance = []
# DAYS = 5
# total_distance = 0
#
# for day in range(DAYS):
#     print(f"Day{day + 1}:", end= " ")
#     distance = int(input("Enter distance travelled: "))
#     travelled_distance.append(distance)
#     total_distance += distance
# print(f"Total distance travelled: {total_distance:.1f}kms")
# print(f"Average distance travelled {mean(travelled_distance):.1f}kms")
# print(f"Longest distance travelled {max(travelled_distance):.1f}kms")
# print(f"Shortest distance travelled {min(travelled_distance):.1f}kms")
#
# user_input = []
# LIMIT = 6
# for i in range(LIMIT):
#     user_input.append(input("Enter integers value: "))
# print(f"list after adding integers {user_input}")
#
# new_index = int(input("Enter the index to update (0-5): "))
#
# if new_index > 5:
#     print("invalid index. Please enter a number between 0 and 5")
#     new_index = int(input("Enter the index to update (0-5): "))
# new_value = int(input("Enter new value: "))
#
# user_input.insert(new_index, new_value)
# print(f"Updated list:{user_input}")
#
# trainees = []
# num_of_trainees = int(input("Enter number of trainees: "))
# trainee_number = 4000
# low_average = 0
#
# for i in range(num_of_trainees):
#     print(f"Trainee #{trainee_number}")
#     trainee_number += 1
#     total = 0
#     for exam in range(3):
#         result = int(input(f"Enter result{exam +1}: "))
#         total += result
#     average = total /3
#     print(average)
#     if average < 50:
#         low_average += 1
#
#     trainees.append(average)
# print("--------------------------------------------------")
# print("\t\t\t\t\t Trainee Statistics")
#
# trainee_number = 4000
#
# for index, value in enumerate(trainees):
#     print(f"Trainee #{index + trainee_number} {value}")
# print(f"Average result: {mean(trainees):.1f}")
# print(f"Maximum average: {max(trainees):.1f}")
# print(f"Minimum average: {min(trainees):.1f}")
# print(f"Number of low average result: {low_average}")