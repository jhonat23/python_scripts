#!/bin/python3
"""There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.

Data entry:
7
0 0 1 0 0 1 0"""

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    c = list(map(int, c.split()))
    jumps = 0
    while len(c) > 1:
        if c[0] == 0 and c[1] == 0 and len(c) == 2:
            c = c[1:]
        elif c[0] == 0 and c[1] == 0 and c[2] == 1:
            c = c[1:]
        elif c[0] == 0 and c[1] == 1 and c[2] == 0:
            c = c[2:]
        elif c[0] == 0 and c[1] == 0 and c[2] == 0:
            c = c[2:]
        jumps += 1
        print(c)
    return jumps
    # Write your code here

print(jumpingOnClouds('0 0 0 1 0 0'))

"""if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()"""