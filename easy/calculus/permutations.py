from itertools import permutations

data = tuple(input().split())

lst = list(permutations(data[0], int(data[1])))

for tup in sorted(lst):
    print(''.join(tup))