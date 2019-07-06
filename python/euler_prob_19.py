#  Project Euler - Problem 19 - Counting Sundays
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import datetime

sundays = 0
date = datetime.datetime(1901,01,01) # start with 01/01/1901
end_date = datetime.datetime(2000,12,31) # end with 12/31/2000
step = datetime.timedelta(days=1) # increment by one day for each step

while date <= end_date:
    if date.day == 1 and date.weekday() == 6:
        sundays += 1 # add one to sundays fitting the criteria
    date = date + step # add one day to the date

print(sundays)