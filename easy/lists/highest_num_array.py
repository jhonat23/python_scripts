"""Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.

Examples
[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3

"""

# def highest_rank(arr):
#     count_arr = {}
#     for i in list(set(arr)):
#         count_arr[i] = arr.count(i)
#     return count_arr

def highest_rank(arr):
    return max(sorted(arr,reverse=True), key=arr.count)

print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10]))