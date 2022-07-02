"""entry type:
3
1 2 3
2
3 45
2 28
1 56"""

from collections import Counter

X = int(input())
size_list = Counter(list(map(int, input().split())))
N = int(input())
order = list(list(map(int,input().split())) for _ in range(N))

money_earned = 0

print(size_list)
print(order)

for i in range(len(order)):
    if order[i][0] in size_list.keys():
        print('Si manejamos talla {}, bien pueda'.format(order[i][0]))
        if size_list[order[i][0]] != 0:
            size_list[order[i][0]] -= 1 
            money_earned += order[i][1] 
            print('Gracias por la compra') 
        else:
            print('Ya se nos acabaron')   
    else:
        print('No tenemos en talla {}'.format(order[i][0]))

print(size_list)
print(money_earned)