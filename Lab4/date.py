#1
from datetime import datetime, timedelta
# Get the current date
current_date = datetime.now()
# Subtract five days
five_days_ago = current_date - timedelta(days=5)
# Print the result
print("Five days ago:", five_days_ago.strftime("%Y-%m-%d"))

#2
from datetime import datetime, timedelta
# Get the current date
current_date = datetime.now()
# Calculate yesterday
yesterday = current_date - timedelta(days=1)
# Calculate tomorrow
tomorrow = current_date + timedelta(days=1)
# Print the results
print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", current_date.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))

#3
from datetime import datetime
# Get the current date and time
current_datetime = datetime.now()
# Drop microseconds
current_datetime_without_microseconds = current_datetime.replace(microsecond=0)
# Print the original and modified datetime
print("Original datetime:", current_datetime)
print("Datetime without microseconds:", current_datetime_without_microseconds)

#4
from datetime import datetime
def date_difference_in_seconds(date1, date2):
    # Calculate the difference between the two dates
    difference = date2 - date1
    # Convert the difference to seconds
    difference_in_seconds = difference.total_seconds()
    return difference_in_seconds
# Example dates
date1 = datetime(2022, 1, 1, 12, 0, 0)  # January 1, 2022 at 12:00:00 PM
date2 = datetime(2022, 1, 2, 12, 0, 0)  # January 2, 2022 at 12:00:00 PM
# Calculate the difference in seconds
difference_seconds = date_difference_in_seconds(date1, date2)
# Print the result
print("Difference between the two dates in seconds:", difference_seconds)
