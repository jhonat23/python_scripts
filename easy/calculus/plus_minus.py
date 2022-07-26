"""Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.
Example:
Input = [1, 1, 0, -1, -1]
Output:
0.400000 (+)
0.400000 (-)
0.200000 (0)
"""

def plusMinus(arr):
    return print('{:.6f}\n'.format(len([i for i in arr if i > 0]) / len(arr)),'{:.6f}\n'.format(len([i for i in arr if i < 0]) / len(arr)),'{:.6f}\n'.format(len([i for i in arr if i == 0]) / len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
