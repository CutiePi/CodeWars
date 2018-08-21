function descendingOrder(n) {
    if (n.length <= 1)
        return n
    else {
        return Number(n.toString().split('').sort().reverse().join(''));
    }
}
