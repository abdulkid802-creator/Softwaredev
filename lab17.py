from statistics import mean

hourly_rate = ([10.5, 12.0, 14.5, 16.75, 18.0], [20.5, 22.25, 24.0, 26.25, 28.0],
               [34.0, 36.5, 38.0, 40.35, 43.0], [50.0, 60.0, 70.0, 80.0, 99.99],)

for index, i in enumerate(hourly_rate):
    average_pay = mean(i)
    print(f"Average pay of Grade {index + 1} employees: €, {average_pay:.2f}")

for index, i in enumerate(hourly_rate):
    pay_difference = i[4] - i[0]
    print(f"Pay difference at Grade Level {index + 1} €, {pay_difference:.2f}")

counter = 1

print(" " * 35, "Payscale Table")
print(f"{"":15}{"Step 1":15}{"Step 2":15}{"Step 3":15}{"Step 4":15}{"Step 5":15}")
print("-"* 90)

for grade in hourly_rate:
    print(f"Grade:{counter} {grade[0]:12}{grade[1]:15}{grade[2]:15}{grade[3]:15}{grade[4]:15}")
    counter += 1

print()


INCREASE_PAY = 1.50
counter = 1
for row in range(len(hourly_rate)):
    for col in range(len(hourly_rate[row])):
        hourly_rate[row][col] += INCREASE_PAY


print(" " * 35, "Payscale Updated Table")
print(f"{"":15}{"Step 1":15}{"Step 2":15}{"Step 3":15}{"Step 4":15}{"Step 5":15}")
print("-"* 90)

for grade in hourly_rate:
    print(f"Grade:{counter} {grade[0]:12}{grade[1]:15}{grade[2]:15}{grade[3]:15}{grade[4]:15}")
    counter += 1