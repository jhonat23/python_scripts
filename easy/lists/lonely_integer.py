"""
Given an array of integers, where all elements but one occur twice, find the unique element.
Example: 
Input: [1,2,3,4,3,2,1]
Ouput: 4
"""
from collections import Counter

def lonelyinteger(a):
    c = Counter(a)
    for i in c.keys():
        if c[i] == 1:
            return i

    # Write your code here

if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    print(result)