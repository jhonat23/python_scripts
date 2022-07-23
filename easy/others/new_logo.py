"""A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order."""

from collections import Counter

def most_common_letter(s):
    c = Counter(sorted(s))
    return print(*['{} {}'.format(i[0], i[1]) for i in c.most_common(3)], sep = '\n')
    #return dict(itertools.islice(c.items(),3))
    #return ['{} {} \n'.format(i, j) for i, j in c.items()]

if __name__ == '__main__':
    s = input()
    r = most_common_letter(s)