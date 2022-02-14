package main

import (
	"bufio"
	"fmt"
	"os"
)

/*
 * Complete the 'hourglassSum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

func hourglassSum(arr [][]int32) int32 {
	// Write your code here
	max := int32(-65)

	for i := 0; i < 6; i++ {
		for j := 0; j < 6; j++ {
			// isHourglassCenter := true
			tempSum := int32(arr[i][j])
			if (i-1) >= 0 && (j-1) >= 0 {
				tempSum = tempSum + int32(arr[i-1][j-1]) + int32(arr[i-1][j])
			} else {
				continue
			}
			if (j + 1) < 6 {
				tempSum = tempSum + int32(arr[i-1][j+1])
			} else {
				continue
			}
			if (i + 1) < 6 {
				tempSum = tempSum + int32(arr[i+1][j-1]) + int32(arr[i+1][j]) + int32(arr[i+1][j+1])
			} else {
				continue
			}
			if max < tempSum {
				fmt.Printf("indices: %v, %v \n", i, j)
				max = tempSum
				fmt.Printf("max: %v \n", max)
			}
		}
	}
	return max
}

func main() {
	// reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	// stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	stdout := os.Stdout
	// checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	var arr [][]int32
	// for i := 0; i < 6; i++ {
	// 	arrRowTemp := strings.Split(strings.TrimRight(readLine(reader), " \t\r\n"), " ")

	// 	var arrRow []int32
	// 	for _, arrRowItem := range arrRowTemp {
	// 		arrItemTemp, err := strconv.ParseInt(arrRowItem, 10, 64)
	// 		checkError(err)
	// 		arrItem := int32(arrItemTemp)
	// 		arrRow = append(arrRow, arrItem)
	// 	}

	// 	if len(arrRow) != 6 {
	// 		panic("Bad input")
	// 	}

	// 	arr = append(arr, arrRow)
	// }
	arr = append(arr, []int32{1, 1, 1, 0, 0, 0})
	arr = append(arr, []int32{0, 1, 0, 0, 0, 0})
	arr = append(arr, []int32{1, 1, 1, 0, 0, 0})
	arr = append(arr, []int32{0, 0, 2, 4, 4, 0})
	arr = append(arr, []int32{0, 0, 0, 2, 0, 0})
	arr = append(arr, []int32{0, 0, 1, 2, 4, 0})
	result := hourglassSum(arr)

	fmt.Fprintf(writer, "%d\n", result)

	writer.Flush()
}

// func readLine(reader *bufio.Reader) string {
// 	str, _, err := reader.ReadLine()
// 	if err == io.EOF {
// 		return ""
// 	}

// 	return strings.TrimRight(string(str), "\r\n")
// }

// func checkError(err error) {
// 	if err != nil {
// 		panic(err)
// 	}
// }
