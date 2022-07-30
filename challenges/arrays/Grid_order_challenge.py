"""
Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.
Example:
a b c
a d e
e f g
Ouput : YES
"""
from tkinter.messagebox import NO


def gridChallenge(grid):
    lst = [sorted(i) for i in grid]
    lstf = [list(i) for i in zip(*lst)]
    lstc = [sorted(i) for i in lstf]
    return 'YES' if lstf == lstc else 'NO'

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

    print(result)