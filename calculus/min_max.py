def high_and_low(numbers):
    num = list(map(int,numbers.split()))
    return '{0} {1}'.format(max(num), min(num))

print(high_and_low('-655 -462 585 672 -883 637 -661 -987 877 626 685 118 -310 17 840'))