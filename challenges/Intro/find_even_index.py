"""You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1."""
def find_even_index(arr):
    sum_left = 0
    sum_rigth = 0
    for i in range(len(arr)):
        sum_left = sum(arr[:i])
        sum_rigth = sum(arr[i+1:])
        if sum_left == sum_rigth:
            return i
        elif i == len(arr)  -1 :
            return -1
        

print(find_even_index([1,2,3,4,5,6]))