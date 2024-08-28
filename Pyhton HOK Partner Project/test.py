from datetime import datetime, timedelta

# Initial time and date
initial_time_str = "2024-08-27 12:18:00"
initial_time = datetime.strptime(initial_time_str, "%Y-%m-%d %H:%M:%S")

# Adding 36 hours to the initial time
added_time = initial_time + timedelta(hours=36)

# Format the result
result_time_str = added_time.strftime("%Y-%m-%d %H:%M:%S")

# Print the result
print(result_time_str)