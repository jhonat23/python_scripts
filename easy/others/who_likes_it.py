"""Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this

Note: For 4 or more names, the number in "and 2 others" simply increases.
"""
def likes(names):
    if not len(names):
        return 'no one likes this'
    elif len(names) == 1:
        return '{} likes this'.format(names[0])
    elif len(names) == 2:
        return '{0} and {1} like this'.format(names[0], names[1])
    elif len(names) == 3:
        return '{0}, {1} and {2} like this'.format(names[0], names[1], names[2])
    elif len(names) >= 4:
        return '{0}, {1} and {2} others like this'.format(names[0], names[1], len(names[2:]))

print(likes(["Max", "John", "Mark"]))
    