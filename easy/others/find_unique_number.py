"""There is an array with some numbers. All numbers are equal except for one. Find it

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

Arrays with minimun 3 numbers"""

from collections import Counter

def find_uniq(arr):
    c = Counter(arr)
    return min(c, key=c.get)

print(find_uniq([0, 1, 1, 1, 1 ]))