task = input("Enter your task: ")
task_priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match task_priority:
    case "high":
        if time_bound == "yes":
            print(f"Alert: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"ToDo: '{task}' which is an high priority program although not time bound, check again")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task and time-bound, do well to do it on time")
        else:
            print(f"Hello, you have a medium priority task you want to complete: {task}, however, it is not time-bound")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task and time-bound. Consider completing it before the deadline")
        else:
            print(f"Note: Hey there, remember you have a low-priority task: '{task}'. Try completing it when you have free time.")

