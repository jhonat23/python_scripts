"""I not made this code, using for understand an exercise"""

from collections import OrderedDict

def merge_the_tools(string, k):
    for x in range(0,len(string),k):     
        print(''.join(list(OrderedDict.fromkeys(string[x:x+k]))))

merge_the_tools(input(), int(input()))