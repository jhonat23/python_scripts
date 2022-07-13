"""
There is an array of strings. All strings contains similar letters except one. Try to find it!
find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo' 
others strings: ['  ', 'aaa', 'aa', '', '     ', 'aaa', 'aaaaaa']

Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 3 strings."""

def find_uniq(arr):
    let = [set(i.lower()) for i in arr]
    pos = 0
    for i in let:
        if len(i) == 0 or i == {' '}:
            pos += 1
            continue
        elif let[0] - i != set():
            return arr[pos]
        pos += 1

print(find_uniq([ 'abc', 'acb', ' ', 'foo', 'bca', 'cab', 'cba' ]))

