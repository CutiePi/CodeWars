import math


# Find biggest number from right to left then promote once 1234567890
# 59884848459853 59884848498535 should equal 59884848483559


# algo to do
# find when next is smaller
# then take smallest previous that is bigger and replace
# take rest and order asc
def next_bigger(n):
    number = list(str(n))
    histo = []
    for x in range(len(number) - 1, 0, -1):
        histo.append(number[x])
        if int(number[x]) > int(number[x - 1]):
            for z in range(len(histo)):
                if int(histo[z]) > int(number[x - 1]):
                    temp = number[x - 1]
                    number[x - 1] = histo[z]
                    histo[z] = temp
                    histo.sort()
                    number = int(''.join(number[0:x]) + ''.join(histo))
                    return -1 if number <= n else number
    return -1


print(next_bigger(9))
print(next_bigger(111))
print(next_bigger(531))
print(next_bigger(144))  # 414
print(next_bigger(891))
print(next_bigger(12));  # 21
print(next_bigger(513));  # 531
print(next_bigger(2017));  # 2071
print(next_bigger(1234567890))  # 1234567908
