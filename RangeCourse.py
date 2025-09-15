
# List of daily tasks for a week
weekly_tasks = [
    "Restock Fruits",
    "Clean Dairy Section",
    "Review Meat Inventory",
    "Restock Vegetables",
    "Check Bakery Expiry Dates",
    "Organize Front Displays",
    "Prepare Weekly Sales Report"
]

# List of weekdays corresponding to each task
weekdays = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
]
_dictionary = {}
# Loop through each day using the range function
for day in range(7):
    task = weekly_tasks[day]  # Access the task corresponding to the current day
    weekday = weekdays[day]   # Access the corresponding weekday
    print(f"{weekday} Task: {task}")
    _dictionary[weekday] = task
print(_dictionary)