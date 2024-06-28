package main
// [Great Total Additions of All Possible Arrays from a List.](https://www.codewars.com/kata/568f2d5762282da21d000011) (codewards kata level 4 kyu)
import (
	"fmt"
	"math"
	"math/big"
	"slices"

	"github.com/ernestosuarez/itertools"
)

func main() {
    // 328804
	fmt.Println(gta(7, []int{123489, 5, 67}))
	// 3836040
    fmt.Println(gta(8, []int{12348, 47, 3639}))
}

func gta(limit int, numbers []int) int {
	var a []int
	res := big.NewInt(0)
	for i := range limit {
		if len(a) == limit {
			break
		}
		for j := range len(numbers) {
			if len(a) == limit {
				break
			}
            // numbers length via mafs
			var numberLength int = int(math.Log10(float64(numbers[j]))) + 1
			if i < numberLength {
				var digit int = int(float64(numbers[j])/math.Pow(10.0, float64(numberLength-i-1))) % 10
				// no duplicates
				if !slices.Contains(a, digit) {
					a = append(a, digit)

				}
			}
		}

	}

	factoLimit := big.NewInt(1)
	for i := 1; i <= limit; i++ {
		factoLimit.Mul(factoLimit, big.NewInt(int64(i)))
		for v := range itertools.CombinationsInt(a, i) {
			// mafs: n! === number of possible permutations of unique digits,  sum of n! * sum of digits of combination x on all combinations of size [1,limit] === sum of all arrays
			sumCombination := new(big.Int)
			for z := 0; z < len(v); z++ {
				sumCombination.Add(sumCombination, big.NewInt(int64(v[z])))
			}
			res.Add(res, sumCombination.Mul(sumCombination, factoLimit))
		}
	}

	return int(res.Int64())
}
