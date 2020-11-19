package main

import (
	"fmt"
)

func clouds(c []int32) int {
	if len(c) > 2 {
		if c[2] == 0 {
			return clouds(c[2:]) + 1
		}
		if c[1] == 0 {
			return clouds(c[1:]) + 1
		}

	}
	if len(c) == 2 {
		return 1
	}
	return 0
}

// Complete the jumpingOnClouds function below.
func jumpingOnClouds(c []int32) int32 {
	res := clouds(c)
	return int32(res)
}

func main() {
	var clouds []int32
	clouds = append(clouds, 0, 0, 1, 0, 0, 1, 0)
	fmt.Printf("asdfs %v", jumpingOnClouds(clouds))
}

// func main() {
// 	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

// 	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
// 	checkError(err)

// 	defer stdout.Close()

// 	writer := bufio.NewWriterSize(stdout, 1024*1024)

// 	nTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
// 	checkError(err)
// 	n := int32(nTemp)

// 	cTemp := strings.Split(readLine(reader), " ")

// 	var c []int32

// 	for i := 0; i < int(n); i++ {
// 		cItemTemp, err := strconv.ParseInt(cTemp[i], 10, 64)
// 		checkError(err)
// 		cItem := int32(cItemTemp)
// 		c = append(c, cItem)
// 	}

// 	result := jumpingOnClouds(c)

// 	fmt.Fprintf(writer, "%d\n", result)

// 	writer.Flush()
// }

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
