from datetime import datetime

# Function to get Julian day from a given date
def get_julian_day(date):
    return date.strftime("%j")

# Prompt the user to enter a date
date_input = input("Enter a date (YYYY-MM-DD) or press Enter to use today's date: ")

# If the user does not provide a date, use today's date
if not date_input:
    date = datetime.today()
else:
    try:
        # Try to parse the provided date
        date = datetime.strptime(date_input, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        exit(1)

# Get the Julian day
julian_day = get_julian_day(date)

print(f"The Julian day for the date {date.strftime('%Y-%m-%d')} is: {julian_day}")
