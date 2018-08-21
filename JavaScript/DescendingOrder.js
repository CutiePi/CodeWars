function descendingOrder(n) {
    if (n.length <= 1)
        return n
    else {
        return Number(n.toString().split('').sort().reverse().join(''));
    }
}

// This is safer it manages Null and parameters with no length attribute
function descendingOrder(n){
    return parseInt(String(n).split('').sort().reverse().join(''))
  }
