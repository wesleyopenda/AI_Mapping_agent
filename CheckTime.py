from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M")

time_now = current_time.replace(":", "")

timeNow = int(time_now)

if timeNow in range(700, 840) or timeNow in range(900, 1040) or timeNow in range(1100, 1240) or timeNow in range(1320, 1500) or timeNow in range(1530, 1710) or timeNow in range(1730, 1910) or timeNow in range(1920, 2100):
    print("Current Time is", current_time, " Human and Vehicle traffic is Not busy as most students are in class. We recommend the shortest route.")
elif timeNow in range(840, 900) or timeNow in range(1040, 1100) or timeNow in range(1240, 1320) or timeNow in range(1500, 1530) or timeNow in range(1710, 1730) or timeNow in range(1910, 1930):
    print("Current Time is", current_time, " It is after class hours. We advise the longer route to avoid human/vehicle traffic.")
else:
    print("The school is closed at this time.")
