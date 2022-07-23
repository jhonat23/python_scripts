"""
You are given an integer, n. Your task is to print an alphabet rangoli of size n. (Rangoli is a form of Indian folk art based on creation of patterns.)
Different sizes of alphabet rangoli are shown below:
#size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
#Size 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""
import string

def print_rangoli(size):
    abc = list(string.ascii_letters.lower())
    letter =  '-'.join(abc[:size])
    rettel = '-'.join(list(reversed(abc[:size])))
    c = '-'
    for i in range(size):
        print((c*(((size-1)*2)-i*2)) + rettel[:i*2] + abc[size-1-i] + letter[len(letter)-(i*2):] + (c*(((size-1)*2)-i*2)))
    for i in range(size-2,-1,-1):
        print((c*(((size-1)*2)-i*2)) + rettel[:i*2] + abc[size-1-i] + letter[len(letter)-(i*2):] + (c*(((size-1)*2)-i*2)))
    return

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)