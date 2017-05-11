
def perimeter(n):
    # your code
    old = 1
    new = 1
    sum = 0
    for x in range(n):
        sum+=new
        temp = old + new
        old = new
        new = temp
    return (sum + 1) * 4

print(perimeter(5))

