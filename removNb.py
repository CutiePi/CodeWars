import time
def removNb(n):
    # your code
    result = []
    space = range(1,n+1)
    total = sum(space)
    for a in space:
        b = (total - a) / (a + 1)
        if b < n and (b).is_integer(): result.append((a,b))
    return result

start_time = time.time()
print(removNb(1000003))
print(removNb(101))
print(removNb(461))
print(removNb(26))
print(removNb(10))
print("--- %s seconds ---"  %  (time.time() - start_time))