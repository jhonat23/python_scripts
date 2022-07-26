"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Data Input: [1, 2, 3, 4, 5]
Output
10 14
"""
def miniMaxSum(arr):
    return print(sum(sorted(arr)[:4]), sum(sorted(arr)[1:]))
    # Write your code here

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


