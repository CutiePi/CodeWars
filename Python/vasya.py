def tickets(people):
    vasya = "YES"
    change = [0, 0]
    for x in people:
        if (x == 25):
            change[0] += 1
        elif (x == 50):
            change[1] += 1
            if (change[0] >= 1):
                change[0] -= 1
            else:
                vasya = "NO"
                break
        else:
            if (change[1] >= 1 and change[0] >= 1):
                change[1] -= 1
                change[0] -= 1
            elif (change[0] >= 3):
                change[0] -= 3
            else:
                vasya = "NO"
                break

    return vasya


print(tickets([25, 25, 50]))  # => YES
print(tickets([25, 100]))  # => NO. Vasya will not have enough money to give change to 100 dollars
