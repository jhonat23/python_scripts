"""Print Fizz for multiple of 3 numbers, Buzz for multiple of 5 and FizzBuzz for both cases"""

def fizzBuzz(n):
    lst = []
    for i in range(0, n):
        lst.append(i + 1)
    for j in lst:
        if j % 3 == 0 and j % 5 == 0:
            print('FizzBuzz')
        elif j % 3 == 0:
            print('Fizz')
        elif j % 5 == 0:
            print('Buzz')
        else:
            print(j)
fizzBuzz(15)