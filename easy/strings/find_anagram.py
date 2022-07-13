"""
Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.
"""
from collections import Counter

def makeAnagram(a, b):
    c = Counter(a)
    c.subtract(b)
    return sum([abs(i) for i in c.values()])
    # Write your code here

print(makeAnagram('fcrxzwscanmligyxyvym', 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'))