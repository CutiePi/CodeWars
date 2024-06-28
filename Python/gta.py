import math
import itertools
from decimal import Decimal
# Great Total Additions of All Possible Arrays from a List. -https://www.codewars.com/kata/568f2d5762282da21d000011
# Did it in Go, but could not run it on codewars since slices + itertools required 1.22 and codewars was 1.20 so I asked copilot to convert my Go to python, here's the result
# I added the go solution file as well

def gta(limit, *numbers):
    a = []
    res = Decimal(0)
    for i in range(limit):
        if len(a) == limit:
            break
        for j in range(len(numbers)):
            if len(a) == limit:
                break
            numberLength = int(math.log10(numbers[j])) + 1
            if i < numberLength:
                digit = int(numbers[j] / (10 ** (numberLength - i - 1))) % 10
                if digit not in a:
                    a.append(digit)

    # mafs: n! === number of possible permutations of unique digits,  sum of n! * sum of digits of combination x on all combinations of size [1,limit] === sum of all arrays
    factoLimit = Decimal(1)
    for i in range(1, limit + 1):
        factoLimit *= i
        for v in itertools.combinations(a, i):
            sumCombination = sum(v)
            res += sumCombination * factoLimit

    return int(res)

# 3836040
print(gta(8, 12348, 47, 3639))
# 328804
print(gta(7, 123489, 5, 67))
