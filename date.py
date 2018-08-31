
# TODO: Either delete this commented-out code or determine if you want to keep going
# down this route.
# # Global vars in this module
# SUNDAY = 1
# MONDAY = 2
# TUESDAY = 3
# WEDNESDAY = 4
# THURSDAY = 5
# FRIDAY = 6
# SATURDAY = 7

# def getUpcomingSunday():
#     """

#     """

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