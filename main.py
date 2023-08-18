from datetime import datetime
user_input = input("enter the goal with deadline, supported by ':' \n")
input_list = user_input.split(":")
goal = input_list[0]
deadline = input_list[1].strip()

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
date_today = datetime.today()
# calculate time from now to the deadline
time_left = deadline_date - date_today
print(f"dear user, the time remaining for you to complete your goal: {goal} is {time_left.days} days")
print("Thank You!")





