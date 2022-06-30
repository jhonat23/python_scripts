"""Given an integer, n, print the following values for each integer i from 1 to n:

Decimal
Octal
Hexadecimal (capitalized)
Binary"""

def print_formatted(number):
    mar = len(bin(number)) - 1
    for i in range(1, number + 1):
        print(str(i).rjust(mar-1,' ') + format(i, 'o').rjust(mar,' ') + format(i, 'X').rjust(mar,' ') + format(i, 'b').rjust(mar,' '))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)