"""Staircase detail

This is a staircase of size :

   #
  ##
 ###
####

Its base and height are both equal to n. It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size ."""

def staircase(n):
    return print(*[('#'*i).rjust(n, ' ') for i in range(1, n+1)], sep='\n')
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    print(staircase(n))