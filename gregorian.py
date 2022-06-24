# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

from calendar import isleap


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    else:
        return False
    
    # Write your logic here
    # leap = False
    # return leap

year = int(input())
print(is_leap(year))

##other way:

def is_leap(year):
    return isleap(year)