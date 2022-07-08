"""Alice and Bob have two arrays with three grades, compare each note and give 1 point if Alice have a greater grade per arr[i] or viceversa"""

def compareTriplets(a, b):
    A = 0
    B = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            A +=1
        elif a[i] < b[i]:
            B += 1
    return A, B