"""Code for create a secuence of numbers on string"""

if __name__ == '__main__':
    n = int(input())
    number = ''
    for i in range(1, n + 1):
        number += str(i)
print(number)