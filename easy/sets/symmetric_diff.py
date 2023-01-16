n = input()
a = set(list(map(int,input().split())))

m = input()
b = set(list(map(int,input().split())))

c = sorted(list(a ^ b))

for i in c:
    print(i)
