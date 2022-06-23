# Sum of Resistance in Parallel Circuits
# If two or more resistors are connected in parallel, the overall resistance of the circuit reduces. It is possible to calculate the total resistance of a parallel circuit by using this formula:

# 1/RTotal = 1/R1 + 1/R2 + 1/R3 ...

# Create a function that takes a list of parallel resistance values, and calculates the total resistance of the circuit.

# Worked Example
# parallel_resistance([6, 3, 6]) ➞ 1.5

# # 1/RTotal = 1/6 + 1/3 + 1/6
# # 1/RTotal = 2/3
# # RTotal = 3/2 = 1.5
# Examples
# parallel_resistance([6, 3]) ➞ 2

# parallel_resistance([10, 20, 10]) ➞ 4

# parallel_resistance([500, 500, 500]) ➞ 16
test = [10, 20, 10]
def parallel_resistance(lst):
    parallel_list = [1 / i for i in lst]
    Rtotal = round(1 / sum(parallel_list), 1)
    return Rtotal
print(parallel_resistance(test))