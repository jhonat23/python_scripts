from itertools import product

a = tuple(map(int,input().split()))
b = tuple(map(int,input().split()))
c = product(a, b)

print(*c)