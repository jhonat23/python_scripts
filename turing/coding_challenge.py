def baseball(ops: list) -> int:

    lst = []

    for i in ops:
        if i.isdigit():
            d = int(i)
            lst.append(d)
        elif i == '+':
            b = lst.pop()
            a = lst.pop()
            c = b + a
            lst.append(a)
            lst.append(b)
            lst.append(c)
        elif i == 'D':
            a = lst.pop()
            b = a * 2
            lst.append(a)
            lst.append(b)
        elif i == 'C':
            lst.pop()

    result = sum(lst)
    return result

if __name__ == '__main__':
    data = input().split()
    print(data)
    r = baseball(data)
    print(r)