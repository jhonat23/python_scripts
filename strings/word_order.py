from collections import Counter

print(Counter(['a', 'b', 'c', 'a', 'b', 'b']))
print(Counter({'a': 2, 'b': 3, 'c': 1}))
print(Counter(a=2, b=3, c=1))
print(Counter(['hola', 'como', 'estas', 'hola']))

dicc = Counter([input() for _ in range(int(input()))])
print(dicc)
print(len(dicc))
print(*dicc.values())
