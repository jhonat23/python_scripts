

def palindromeIndex(s):
    if s == ''.join(reversed(s)):
        return -1
    for i in range(len(s)):
        if s[0:i] + s[i+1:] == ''.join(reversed(s[0:i] + s[i+1:])):
            return s.index(s[i])
        

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):

        s = input()

        result = palindromeIndex(s)
    
    print(result)