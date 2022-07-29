"""
Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
Create a Caesar's cipher
"""

from curses.ascii import isupper
import string

def caesarCipher(s, k):
    if k == 0:
        return s
    else: 
        abc = string.ascii_lowercase
        xyz = abc * k
        rotlist = xyz[k: len(abc) + k]
        sf = list(s)
        for i, letter in enumerate(s):
            if s[i].lower() in abc:
                if isupper(letter):
                    sf[i] = rotlist[abc.index(letter.lower())].upper()
                else:
                    sf[i] = rotlist[abc.index(letter.lower())]
            else:
                continue
        return ''.join(sf)
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result)