"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
"""

def timeConversion(s):
    hour = s[:2]
    if s[8:] == 'AM' and s[:2] == '12':
        return '00' + s[2:8]
    elif s[8:] == 'PM' and s[:2] == '12':
        return s[:8]
    elif s[8:] == 'PM':
        return str(int(hour) + 12) + s[2:8]
    else:
        return s[:8]
    # Write your code here

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)
    print(result)