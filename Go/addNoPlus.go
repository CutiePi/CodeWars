package main

import "fmt"

func main() {
	fmt.Printf("%d === 4\n", add(2, 2))
	fmt.Printf("%d === 0\n", add(-120, 120))
	fmt.Printf("%d === 95\n", add(97, -2))
	fmt.Printf("%d === 330\n", add(120, 210))

}

// https://leetcode.com/problems/sum-of-two-integers/description/
func add(x int, y int) int {
	var keep = (x & y) << 1
	var res = x ^ y

	// If bitwise & is 0, then there
	// is not going to be any carry.
	// Hence result of XOR is addition.
	if keep == 0 {
		return res
	}
	return add(keep, res)
}
