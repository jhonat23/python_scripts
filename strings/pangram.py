"""this code help you to find if a sentence is a pangram"""

import string

def is_pangram(s):
    abc = list(string.ascii_letters)
    #print(abc)
    c = ''.join(s.split())    
    count = 0
    for i in c:
        if i in abc:
            count += 1
            abc.remove(i.upper())
            abc.remove(i.lower())
    if count >= 26:
        return True
    else:
        return False

result = print(is_pangram(input()))