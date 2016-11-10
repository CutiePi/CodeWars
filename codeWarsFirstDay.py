import math

def permutations(n):
    n = list(n)
    if len(n) == 2:
        return [[n[0], n[1]], [n[1], n[0]]]
    else:
        result = []
        for pos in range(len(n)):
            letter = n[0]
            n.pop(0)
            for perm in permutations(n):
                result.append(letter + "".join(perm))
            n.append(letter)
        return result


def is_triangle(a, b, c):
        if (a + b > c and a + c > b and  b + c > a):
            return True
        else:
            return False

def getCount(inputStr):
    return inputStr.count("a")

def spin_words(sentence):
        arr=  sentence.split( )
        for x in range(len(arr)):
            if(len(arr[x])>4):
                arr[x]=arr[x][::-1]

        return   " ".join(arr)

def tribonacci(signature,n):
    for x in range(n):
        signature.append(sum(signature[-3:]))
    return signature[:n]


def is_square(n):
    return math.sqrt(n)%1==0 if n>-1 else False

def get_function(sequence):
    diff = sequence[1]-sequence[0]
    for x in range(len(sequence)-1):
        if(diff != sequence[x+1]-sequence[x]):
            return "epicfail"
    def datboi(gimme):
        return (diff*gimme)+sequence[0]
    return datboi

def longest(s1, s2):
    return "".join(sorted(set(s1+s2)))
