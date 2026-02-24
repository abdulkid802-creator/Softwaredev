# step_count = 3
#
# step_data = [[5400, 6200], [8520, 7900], [ 4600, 5020]]
#
# print("Participant \t\t Week1 \t\t Week2")
# print("-"* 40)
#
# for i in range(len(step_data)):
#     print("Participant", i + 1, "\t\t ", step_data[i][0], "\t\t ", step_data[i][1])

# step_count = 3
#
# step_data = [[5400, 6200], [8520, 7900], [ 4600, 5020]]
#
# week1_step = int(input("Enter Week 1 step total: "))
# week2_step = int(input("Enter Week 2 step total: "))
#
# print("Participant \t\t Week1 \t\t Week2")
# print("-"* 40)
#
# step_data.append([week1_step,week2_step])
#
# for i in range(len(step_data)):
#     print("Participant", i + 1, "\t\t ", step_data[i][0], "\t\t ", step_data[i][1])

# step_count = 3
#
# step_data = [[5400, 6200], [8520, 7900], [ 4600, 5020]]
#
# week1_step = int(input("Enter Week 1 step total: "))
# week2_step = int(input("Enter Week 2 step total: "))
#
# print("Participant \t\t Week1 \t\t Week2 \t\t Improvement")
# print("-"* 55)
#
# step_data.append([week1_step,week2_step])
#
# for row in step_data:
#     improvement = row[1] - row[0]
#     row.append(improvement)
#
# for i in range(len(step_data)):
#     print("Participant", i + 1, "\t\t ", step_data[i][0], "\t\t ", step_data[i][1], "\t\t", step_data[i][2])

# step_count = 3
#
# step_data = [[5400, 6200], [8520, 7900], [ 4600, 5020]]
#
# week1_step = int(input("Enter Week 1 step total: "))
# week2_step = int(input("Enter Week 2 step total: "))
#
# print("Participant \t\t Week1 \t\t Week2 \t\t Improvement")
# print("-"* 55)
#
# step_data.append([week1_step,week2_step])
#
# for row in step_data:
#     improvement = row[1] - row[0]
#     row.append(improvement)
#
# for i in range(len(step_data)):
#     print("Participant", i + 1, "\t\t ", step_data[i][0], "\t\t ", step_data[i][1], "\t\t", step_data[i][2])
#
# max_improvement = step_data[0][2]
# min_improvement = step_data[0][2]
# max_participant = 1
# min_participant = 1
# for i in range(len(step_data)):
#     if step_data[i][2] > max_improvement:
#         max_improvement = step_data[i][2]
#         max_participant = i + 1
#     if step_data[i][2] < min_improvement:
#         min_improvement = step_data[i][2]
#         min_participant = i + 1
# print("Largest improvement: Participant", max_participant)
# print("Smallest improvement: Participant", min_participant)
#
# step_data = [[5400, 6200], [8520, 7900], [ 4600, 5020]]
#
# for row in step_data:
#     row.append(row[1] - row[0])
#
# improvements = [row[2] for row in step_data]
#
# max_improvement = max(improvements)
# min_improvement = min(improvements)
#
# print("Largest improvement:", max_improvement)
# print("Smallest improvement:", min_improvement)

# step_count = 3
#
# step_data = [[5400, 6200], [8520, 7900], [ 4600, 5020]]
#
# week1_step = int(input("Enter Week 1 step total: "))
# week2_step = int(input("Enter Week 2 step total: "))
#
# print("Participant \t\t Week1 \t\t Week2 \t\t Improvement")
# print("-"* 55)
#
# step_data.append([week1_step,week2_step])
#
# for row in step_data:
#     improvement = row[1] - row[0]
#     row.append(improvement)
#
# for i in range(len(step_data)):
#     print("Participant", i + 1, "\t\t ", step_data[i][0], "\t\t ", step_data[i][1], "\t\t", step_data[i][2])
#
# print()
# print("Participants who reached 10,000 steps in Week 2:")
# print("Participant \t\t Week2 \t\t Status")
# print("-"* 60)
#
# for row in step_data:
#     row.append(row[1] - row[0])
#
# for i in range(len(step_data)):
#     if step_data[i][1] >= 10000:
#         print(i+1, "\t\t\t\t\t", step_data[i][1], "\t\t\t" "reached 10,000 steps!")
#     else:
#         print (i + 1, "\t\t\t\t\t", step_data[i][1],"\t\t\t", "below 10,000 steps!")