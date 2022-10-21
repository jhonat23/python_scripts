"""Do a left rotation on array when a number d of rotations are given"""

def rotLeft(a, d):
    #if d > n then change a*2 for a*d
    total_list = a * d
    return total_list[d + 1:len(a) + d + 1]

    # Write your code here

print(rotLeft([1,2,3,4,5,6,7], 3))