# def display_pi():
#     PI = 22.0/7.0
#     print("PI = ", PI)
#
# for i in range(5):
#     display_pi()

import time

def current_time():
    time_now = time.strftime("%H:%M:%S")
    print(time_now)

for i in range(5):
    current_time()
