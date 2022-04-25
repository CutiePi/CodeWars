def get_function(sequence):
    diff = sequence[1]-sequence[0]
    for x in range(len(sequence)-1):
        if(diff != sequence[x+1]-sequence[x]):
            return "Non-linear sequence"
    def datboi(gimme):
        return (diff*gimme)+sequence[0]
    return datboi