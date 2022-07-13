"""Given a 6X6 2D array find the max sum of hourglass composed in this form:
acb
 d
efg

inside in array. Example input:
-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0

 or :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
"""

def hourglassSum(arr):
    sums = []
    sum_mid = []
    tsums = []
    for i in range(0, len(arr)):
        sums.append([sum(arr[i][j:j + 3]) for j in range(len(arr)-2)])
        if i > 0 and i < len(arr)-1:
            sum_mid.append(arr[i][1:5])
    for i in range(len(sum_mid)):
        tsums.append([sums[i][j]+sums[i+2][j] for j in range(len(sums)-2)])
    return max([max([tsums[i][j]+sum_mid[i][j] for j in range(len(tsums))]) for i in range(len(sum_mid))])
    # Write your code here

arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

print(hourglassSum(arr))