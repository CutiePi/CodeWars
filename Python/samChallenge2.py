# Dans un sorted array de integer > 0 et < 0
# trouve un algo qui permet de trouver si il y a une paire d'éléments
# qui sont équivalent à une somme passée en paramètre
arr = [-1, 1, 4, 8, 15, 19]

for i in range(12, 5000):
    arr.append(i + i);


def check_if_sum_present(num, arr):
    for x in range(0, len(arr)):
        first = arr[x]
        for y in range(x + 1, len(arr)):
            if (num == (arr[y] + first)):
                return True
    return False


arr = ['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']


def dirReduc(plan):
    pcop = True
    while pcop:
        pcop = False
        for x in range(0, len(plan) - 1):
            first = plan[x]
            second = plan[x + 1]
            if (first != second):
                print(first + second)
                if (first == 'NORTH' or first == 'SOUTH'):
                    if (second == 'NORTH' or second == 'SOUTH'):
                        plan[x] = 'EMPTY'
                        plan[x+1] = 'EMPTY'
                        pcop = True
                        break;
                if (first == 'EAST' or first == 'WEST'):
                    if (second == 'EAST' or second == 'WEST'):
                        plan[x] = 'EMPTY'
                        plan[x+1] = 'EMPTY'
                        pcop = True
                        break;
        plan[:] = [x for x in plan if 'EMPTY' not in x]
    return plan


opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc2(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan



s1 = "A yyyy aaaa bb rr c hh oo"
s2 = "& aaa bbb c d oo"

def mix(s1, s2):
    arrCount = []
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    s1 = ''.join(sorted([c for c in s1 if c.islower() and c.isalpha()]))
    s2 = ''.join(sorted([c for c in s2 if c.islower() and c.isalpha()]))
    print(s1)
    s1 = s1
    for x in range(0,26):
        s1Count = s1.count(alpha[x]) if s1.count(alpha[x]) > 1 else 0
        s2Count = s2.count(alpha[x]) if s2.count(alpha[x]) > 1 else 0
        arrCount.append("1:" + alpha[x]*s1Count if s1Count > s2Count else "2:" + alpha[x]*s2Count
        if s2Count > s1Count else "=:" + alpha[x]*s2Count if (s1Count == s2Count and s1Count != 0) else "")
    arrCount.sort(key=lambda  y: y[1:2])
    arrCount.sort(key=lambda y: y[2:])
    arrCount.sort(key=len, reverse=True)
    return "/".join(value for value in arrCount if value != '')




print(mix(s1,s2))