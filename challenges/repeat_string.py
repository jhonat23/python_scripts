#!/bin/python3
"""There is a string, s, of lowercase English letters that is repeated infinitely many times. Given an integer, n, find and print the number of letter a's in the first n letters of the infinite string."""

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n): 
    # n_string = s * int((n/len(s)) + 1)
    # n_string = n_string[:n]
    # c = Counter(n_string)
    # return c['a']
    c = Counter(s)
    cr = Counter(s[:(n % len(s))])
    return c['a'] * (n // len(s)) +  cr['a']

print(repeatedString('bcbccacaacbbacabcabccacbccbababbbbabcccbbcbcaccababccbcbcaabbbaabbcaabbbbbbabcbcbbcaccbccaabacbbacbc', 649606239668))

"""if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    aasdjkhragfhaasdsa

    s = input()
    ahtjiabgeap
    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()"""