# Create a function that takes two numbers and a mathematical operator + - / * and will perform a calculation with the given numbers.

# Examples
# calculator(2, "+", 2) ➞ 4

# calculator(2, "*", 2) ➞ 4

# calculator(4, "/", 2) ➞ 2

def calculator(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Can't divide by 0!"
        else:	
            return num1 / num2

#Other way:

def calculator(n1, operator, n2):
	try: 
		return eval(str(n1)+operator+str(n2))# parses the expression passed to this method and runs python expression (code) within the program.
	except ZeroDivisionError: #name of error
		return "Can't divide by 0!"
