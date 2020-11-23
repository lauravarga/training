package main

import "fmt"

// Complete the miniMaxSum function below.
func miniMaxSum(arr []int64) {
	var sum, min, max int64
	sum = int64(0)
	min = arr[0]
	max = arr[0]
	for i := 0; i < len(arr); i++ {
		sum += arr[i]
		if min > arr[i] {
			min = arr[i]
		}
		if max < arr[i] {
			max = arr[i]
		}
	}
	fmt.Printf("%d %d", sum-max, sum-min)
}

func main() {

	var arr []int64
	arr = append(arr, 256741038, 623958417, 467905213, 714532089, 938071625)

	miniMaxSum(arr)
}
