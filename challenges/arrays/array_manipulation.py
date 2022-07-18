"""Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array."""
from collections import OrderedDict

def arrayManipulation(n, queries):
    # res = 0
    # #base = {i : 0 for i in range(1,n + 1)}
    # base = [0] * n
    # for query in queries:
    #     base[query[0] - 1] += query[2]
    #     if query[1] < n:
    #         base[query[1]] -= query[2]
    #     else:
    #         continue
    # for i in base:
    #     if i < 0:
    #         break
    #     res += i
    # MY NOT OPTIMIZED FIRST SOLUTION    
    base = {i : 0 for i in range(1,n + 1)}
    for query in queries:
        for i in range(query[0], query[1] + 1):
            base[i] += query[2]
    return print(max(base.values()))
    #return print(res)

if __name__ == '__main__':    

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)