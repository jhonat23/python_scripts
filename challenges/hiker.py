#!/bin/python3
"""data entry:
8
UDDDUDUU
where:
8 - number of steps
UDDDUDUU - U: step up D: step down
counter for "valleys" when the path pass for zero
"""

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    valleys = 0
    a = 0
    p = [1 if i == 'U' else -1 for i in path]
    for i in range(len(p)):
        p[i] += a
        a = p[i]
    for i in range(len(p)):
        if p[i] == 0 and p[i-1] < 0:
            valleys += 1    
    return valleys
    # Write your code here

print(countingValleys(8, 'DDUUDDUU'))
"""if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()"""