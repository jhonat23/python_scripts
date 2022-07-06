"""Input format:
5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5
Code to understand named tuples"""

from collections import namedtuple

n = int(input())
Student, data = namedtuple('Students', input().split()), list(input().split() for _ in range(n))
data = list(Student(*i) for i in data)
result = sum([int(data[i].MARKS) for i in range(len(data))]) / len(data)

print(n, data)
print(result)
