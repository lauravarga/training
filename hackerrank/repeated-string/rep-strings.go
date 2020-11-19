package main

import (
	"fmt"
)

func aInString(s string) int64 {
	count := 0
	for i := 0; i < len(s); i++ {
		if "a" == string(s[i]) {
			count++
		}
	}
	return int64(count)
}

// Complete the repeatedString function below.
func repeatedString(s string, n int64) int64 {
	var count, i int64 = 0, 0
	length := int64(len(s))
	if n > length {
		count = aInString(s) * (n / length)
		n = n % length
	}

	for i = 0; int64(i) < n; i++ {
		if string(s[i]) == "a" {
			count++
		}
	}
	return count
}

func main() {
	reps := repeatedString("aba", 2)
	fmt.Printf("reps: %v", reps)
}
