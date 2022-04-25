def decipher_this(string):
    arrWord = str(string).split(" ")
    for x in range(0, len(arrWord)):
        if len(arrWord[x]) >= 2 :
            digitCount = sum(c.isdigit() for c in arrWord[x])
            arrWord[x] = chr(int(arrWord[x][:digitCount])) + arrWord[x][digitCount:]
        if len(arrWord[x]) > 2:
            arrWord[x] = arrWord[x][0] + arrWord[x][-1] + arrWord[x][2:-1] + arrWord[x][1:2]
    return " ".join(arrWord)