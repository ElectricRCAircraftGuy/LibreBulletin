"""
date.py
- helper date and time functions

By Gabriel Staples
https://www.ElectricRCAircraftGuy.com
- Find my email by clicking the "Contact me" link at the top of my website above.

Part of LibreBulletin automated bulletin generation
https://github.com/ElectricRCAircraftGuy/LibreBulletin

License: LGPL v3 or later 
(open source; can be used for commercial products; you DO have to maintain this code open source, including any changes
or improvements you make to it, but you do NOT have to open source any of your proprietary code which uses this code)
- See LICENSE.txt for details.

References:
- *****https://docs.python.org/3/library/datetime.html#datetime.datetime
- 

"""

import datetime
import sys

def getUpcomingSundayDateTime(time_to_use_next_sunday_date = None):
    """
    Return the datetime.datetime (see https://docs.python.org/3/library/datetime.html) object for the upcoming Sunday.

    Inputs:
    time_to_use_next_sunday_date     Time after which we will use *next Sunday* as the date, assuming today is Sunday.
        Ex: "12:30pm". If today is Sunday, and *before* 12:30pm we will use today's date. If today is Sunday but 
        *after* "12:30pm" we will use next Sunday's date.
        Don't pass in a value for this parameter if you'd just like to use today's date in case today is Sunday.   

    For a description of acceptably-formatted time strings, see "bulletin_INPUTS.txt" near the 
    "time_to_use_next_sunday_date" parameter.

    References:
    datetime.date:
    - https://stackoverflow.com/a/8801540/4561887
    - https://stackoverflow.com/a/41056161/4561887
    strftime format string:
    - https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
    """

    # Steps: figure out what today is. Figure out what this coming Sunday is. If today == this coming Sunday, then see
    # if the time right now > the threshold time. If it is, then use the Sunday 7 days from now. If not, then use 
    # today.
    SUNDAY_WEEKDAY_NUM = 6

    if time_to_use_next_sunday_date != None and len(time_to_use_next_sunday_date) != 4:
        print('Error: invalid "time_to_use_next_sunday_date" time string. '
              'It must be 24-hr time and exactly 4 digits. Ex: use "1330" for 1:30pm, and "0930" for 9:30am.')
        # sys.exit()

    today = datetime.datetime.now()
    # FOR TESTING PURPOSES TO FORCE A CERTAIN DATE TO BE "TODAY" (comment out when done)
    # today = datetime.datetime(2018, 9, 28)
    # today = datetime.datetime(2018, 12, 12) # GOOD TEST--helped me catch a bug regarding getting data from the next yr
    # today = datetime.datetime(2018, 12, 28) # GOOD TEST--forces script to start table with data from the next yr
    # today = datetime.datetime(2018, 12, 31)
    this_sunday = today + datetime.timedelta(days = (SUNDAY_WEEKDAY_NUM - today.weekday()) % 7)

    # If today is Sunday *and* the user has passed in a time.
    if today == this_sunday and time_to_use_next_sunday_date != None:
        # parse the passed-in time
        # The time string must be in a *4-digit* 24-hr time. 
        # Ex: 12:30pm is "1230". 1:15am is "0115". 1:15pm is "1315". 11:15pm is "2315", etc.
        print(40)
        hour = int(time_to_use_next_sunday_date[0:2])
        minute = int(time_to_use_next_sunday_date[2:])
        # print("hour:min = {}:{}".format(hour, minute))
        datetime_threshold = datetime.datetime(this_sunday.year, this_sunday.month, this_sunday.day, hour, minute)
        # If the time today is past the threshold, then use next Sunday as the day instead of today.
        if today > datetime_threshold:
            this_sunday += datetime.timedelta(days = 7)

    # print("this_sunday = {}".format(this_sunday))

    return this_sunday

def getDateInfo(datetime_obj):
    """
    Return the month number, month string, and date string for this datetime object.
    Date string format example: "August 26, 2018"
    """
    month_num = datetime_obj.month
    month_str = datetime_obj.strftime("%B") # See: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
    date_str = month_str + " " + str(datetime_obj.day) + ", " + str(datetime_obj.year) 

    return month_num, month_str, date_str

def isFastSunday(time_to_use_next_sunday_date = None):
    """
    Return True if the upcoming Sunday is the first Sunday of the month, or False otherwise. Clearly, we are assuming
    that Fast Sunday is the first Sunday of the month.

    Inputs:
    time_to_use_next_sunday_date     Time after which we will use *next Sunday* as the date, assuming today is Sunday.
        Ex: "12:30pm". If today is Sunday, and *before* 12:30pm we will use today's date. If today is Sunday but 
        *after* "12:30pm" we will use next Sunday's date.
        Don't pass in a value for this parameter if you'd just like to use today's date in case today is Sunday.
    """



def getRelativeMonth(current_month_num, months_from_now):
    """
    Given a month number 1-12, and the number of months from now (+/- any integer), 
    get the next month's number (1-12) and string (ex: "January").
    
    Usage examples: 
    1) 
    `month_num, month_str = getRelativeMonth(1, 3)`
    Result: month_num is 4 and month_str is "April"

    2) 
    `month_num, month_str = getRelativeMonth(1, -3)`
    Result: month_num is 10 and month_str is "October"
    """

    # Ensure current_month_num is within valid bounds
    if (current_month_num < 1 or current_month_num > 12):
        relative_month_num = -1
        relative_month_name = 'ERROR'
        print('ERROR: INPUT VALUE FOR "current_month_num" OUT OF BOUNDS')

    else:
        # Use zero-indexing in order to use the modulus operator
        current_month_i = current_month_num - 1
        relative_month_i = (current_month_i + months_from_now) % 12 # 0 to 11
        relative_month_num = relative_month_i + 1 # 1 to 12

        month_name_list = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]

        relative_month_name = month_name_list[relative_month_i]

    return relative_month_num, relative_month_name

if __name__ == '__main__':

    # Test some `getRelativeMonth()` examples
    num, name = getRelativeMonth(1, 3)
    print('(num, name) = ({}, {})'.format(num, name))

    num, name = getRelativeMonth(1, -3)
    print('(num, name) = ({}, {})'.format(num, name))

    num, name = getRelativeMonth(3, 15)
    print('(num, name) = ({}, {})'.format(num, name))

    num, name = getRelativeMonth(12, 0)
    print('(num, name) = ({}, {})'.format(num, name))

    num, name = getRelativeMonth(0, 3)
    print('(num, name) = ({}, {})'.format(num, name))

    num, name = getRelativeMonth(13, 3)
    print('(num, name) = ({}, {})'.format(num, name))

    # Valid result:
    """
    (num, name) = (4, April)
    (num, name) = (10, October)
    (num, name) = (6, June)
    (num, name) = (12, December)
    ERROR: INPUT VALUE FOR "current_month_num" OUT OF BOUNDS
    (num, name) = (-1, ERROR)
    ERROR: INPUT VALUE FOR "current_month_num" OUT OF BOUNDS
    (num, name) = (-1, ERROR)
    """

    # Unit test the getUpcomingSundayDateTime() function.
