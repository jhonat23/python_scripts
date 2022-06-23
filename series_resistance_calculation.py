# When resistors are connected together in series, the same current passes through each resistor in the chain and the total resistance, RT, of the circuit must be equal to the sum of all the individual resistors added together. That is:

# RT = R1 + R2 + R3 ...
# Create a function that takes an array of values resistance that are connected in series, and calculates the total resistance of the circuit in ohms. The ohm is the standard unit of electrical resistance in the International System of Units ( SI ).

# Examples
# series_resistance([1, 5, 6, 3]) ➞ "15 ohms"

# series_resistance([16, 3.5, 6]) ➞ "25.5 ohms"

# series_resistance([0.5, 0.5]) ➞ "1.0 ohm"
test = [1,6,3]
def series_resistance(lst):
    return "{total} ohm{l}".format(total = sum(lst), l= 's' if (sum(lst) > 1) else '')
print(series_resistance(test))