"""You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in ascending order."""

import os

from tables import EnumAtom

def minimumSwaps(arr):
    swaps = 0
    pos = [0] * (len(arr) + 1)
    for i, v in enumerate(arr):
        pos[v] = i
    for i in range (len(arr)):
        if arr[i] != i + 1:
            swaps += 1 
            chang = arr[i]
            arr[i] = i + 1
            arr[pos[i + 1]] = chang
            pos[chang] = pos[i + 1]
                   
    # for i, v in enumerate(arr):
    #     for j in range(i + 1, max(arr)):
    #         if arr[j] == i + 1:
    #             arr[j] = arr[i]
    #             arr[i] = i + 1
    #             swaps += 1
    #             continue
    return swaps


if __name__ == '__main__':
    
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)