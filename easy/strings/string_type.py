#Evaluating is a string fills some strings conditions

if __name__ == '__main__':
    s = input()
    for meth in ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']:
        print(any(eval('c.' + meth + '()') for c in s))