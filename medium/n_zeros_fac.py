""" 
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 *  ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html
"""

import math

def zeros(n: int) -> int:
    count = 0
    i = 5
    while (n / i >= 1):
        count += n // i
        i *= 5
    return count

    

if __name__ == '__main__':
    print(zeros(621097049))
