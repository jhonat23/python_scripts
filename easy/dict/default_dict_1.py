from collections import defaultdict

nm = list(map(int, input().split()))

A, B = [input() for i in range(nm[0])], [input() for i in range(nm[1])]
C = defaultdict(list)

for i in range(len(B)):
    for j in range(len(A)):
        if B[i] == A[j]:
            C[A[j]].append(j+1)
    if B[i] not in A:
        C[B[i]].append(-1)

for i in C.keys():
    print(' '.join(map(str, C[i])))




