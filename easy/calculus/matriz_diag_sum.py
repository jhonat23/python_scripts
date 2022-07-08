n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

print(arr)

result1 =0
result2 = 0

for i in range(len(arr)):
    result1 += arr[i][i]
    result2 += arr[i][n-1-i]

print(abs(result1-result2))