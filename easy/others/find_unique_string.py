"""
There is an array of strings. All strings contains similar letters except one. Try to find it!
find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo' 

Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 3 strings."""

def find_uniq(arr):
    let = [set(i) for i in arr]
    #let.sort(reverse=True, key = lambda x: len(x))
    pos = 0
    for i in let:
        if let[0].isdisjoint(i):
            return arr[pos]
        pos += 1

print(find_uniq(['Tom Marvolo Riddle', 'I am Lord Voldemort', 'Harry Potter']))

