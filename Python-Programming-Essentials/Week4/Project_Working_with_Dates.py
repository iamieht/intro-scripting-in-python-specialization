"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    date_month = datetime.date(year, month, 1)

    # Manual calculation of next month and next year. 
    # Special case when month is 12, as year must be change as well.
    if date_month.month == 12:
        next_month = 1
        year += 1
    else:
        next_month = month + 1

    date_next_month = datetime.date(year, next_month, 1)
    
    # compute the difference between the first day of the month - the first day of next month
    number_of_days_in_month = date_next_month - date_month

    return number_of_days_in_month.days

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if year < datetime.MINYEAR or year > datetime.MAXYEAR:
        return False
    elif month < 1 or month > 12:
        return False
    # Checking wheter the day/month combination is valid
    elif day <= 0 or day > days_in_month(year, month): 
        return False
    else:
        return True

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """

    if not is_valid_date(year1, month1, day1) or not is_valid_date(year2, month2, day2):
        return 0
    elif datetime.date(year1, month1, day1) > datetime.date(year2, month2, day2):
        return 0
    else:
        difference = datetime.date(year2, month2, day2) - datetime.date(year1, month1, day1)
        return difference.days

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    today = datetime.date.today()

    if not is_valid_date(year, month, day):
        return 0
    elif datetime.date(year, month, day) > today:
        return 0
    else:
        return days_between(year, month, day, today.year, today.month, today.day)


# Unit Tests
# days_in_month
#print(days_in_month(2020,2))
#print(days_in_month(2020,12))
#print(days_in_month(2019,2))
#print(days_in_month(1400,1))

# is_valid_date
# print(is_valid_date(2020, 1, 1))
# print(is_valid_date(2020, 2, 29))
# print(is_valid_date(2019, 2, 29))
# print(is_valid_date(9999, 1, 1))
# print(is_valid_date(2020, -1, 1))
# print(is_valid_date(1400, 1, 0))

# days_between
# Invalid dates
# print(days_between(2020, -1, 1, 2020, 1, 1))
# print(days_between(2020, 1, 1, 2020, -1, 1))
# print(days_between(2020, -1, 1, 2020, -1, 1))

# Second date later than first date
# print(days_between(2020, 1, 1, 2019, 1, 1))

# Valid scenario
# print(days_between(2019, 1, 1, 2020, 1, 1))
# print(days_between(2019, 1, 1, 2020, 2, 29))

# age_in_days
# print(age_in_days(2020, 3, 7))
# print(age_in_days(2020, -1, 0))
# print(age_in_days(1977, 4, 10))
