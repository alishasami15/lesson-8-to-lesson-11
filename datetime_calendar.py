
import datetime
import calendar

print(" Date, Time & Calendar Examples\n")

# Current Date & Time
now = datetime.datetime.now()
print("Current Date & Time:", now)

# Today's date
today = datetime.date.today()
print("Today's Date:", today)

# Custom date
custom_date = datetime.date(2025, 4, 18)
print("Custom Date:", custom_date)

# Formatting date
print("Formatted Date:", today.strftime("%d-%b-%Y"))

# Calendar for a month
print("\n Calendar for April 2025:\n")
print(calendar.month(2025, 4))

# Check if year is leap
print("Is 2024 a leap year?", calendar.isleap(2024))