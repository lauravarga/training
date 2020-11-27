package main

import "fmt"

// Complete the countApplesAndOranges function below.
func countApplesAndOranges(s int32, t int32, a int32, b int32, apples []int32, oranges []int32) {

	apple := 0
	orange := 0
	for i := 0; i < len(apples); i++ {
		d := a + apples[i]
		if (d >= s) && (d <= t) {
			apple++
		}
	}
	for i := 0; i < len(oranges); i++ {
		d := b + oranges[i]
		if (d >= s) && (d <= t) {
			orange++
		}
	}
	fmt.Printf("%v\n", apple)
	fmt.Printf("%v\n", orange)
}

func main() {
	s := int32(7)
	t := int32(11)
	a := int32(5)
	b := int32(15)
	var apples []int32
	apples = append(apples, int32(-2), int32(2), int32(1))
	var oranges []int32
	oranges = append(oranges, int32(5), int32(-6))

	countApplesAndOranges(s, t, a, b, apples, oranges)
}
