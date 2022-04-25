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