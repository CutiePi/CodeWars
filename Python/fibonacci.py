import math
import numpy

def fib(n):
    x = numpy.array([[1, 1], [1, 0]], dtype=object)
    isNegative = False
    if(n<0):
        if(n%2 == 0):
            isNegative = True
        n = -n
    result = numpy.linalg.matrix_power(x,n)
    return -result[0][1] if isNegative else result[0][1]