def tribonacci(signature,n):
    for x in range(n):
        signature.append(sum(signature[-3:]))
    return signature[:n]