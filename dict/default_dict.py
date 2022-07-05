from collections import defaultdict

def por_defecto():
    return 'Este valor no esta en el diccionario'

d = defaultdict(por_defecto)

d['a'] = 1
d['b'] = 2
d['c'] 
print(d)

print(d.__missing__('a'))
print(d.__missing__('b'))
print(d)

di = defaultdict(list)

print(di)