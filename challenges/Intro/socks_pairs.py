"""Code for obtain pairs of numbers on a list"""
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    c = Counter(ar)
    return int(sum([i / 2 if i % 2 == 0 else (i-1) / 2 for i in c.values()]))
"""    for i in c.values():
        if i % 2 == 0:
            lst.append(i / 2)
        else:
            lst.append((i-1) / 2)
    return lst"""
    
    # Write your code here

print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10]))
#CODE FOR TESTING RESULTS
"""if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()"""
