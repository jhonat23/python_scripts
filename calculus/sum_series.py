"""Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!"""

def get_sum (a,b):
    if a == b:
        return a
    A = a
    B = b
    if b < a:
        B = a
        A = b
    lst = list(range(A,B+1))
    return sum(lst)

print(get_sum(int(input()), int(input())))