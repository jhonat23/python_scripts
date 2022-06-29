N, M = map(int, input().split())
vert = N
horz = M
c = '.|.'
a = int((horz-1) / 2)
b = int((vert-1) / 2)
for i in range(0,b):
    #print(type(a))
    print((c*i).rjust(a-1, '-') + c + (c*i).ljust(a-1, '-'))
print('WELCOME'.center(horz, '-'))
for i in range(b-1,-1,-1):
    #print(type(a))
    print((c*i).rjust(a-1, '-') + c + (c*i).ljust(a-1, '-'))
