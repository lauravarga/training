package main

import (
	"fmt"
	"strconv"
	"strings"
)

/*
 * Complete the timeConversion function below.
 */
func timeConversion(s string) string {
	strParts := strings.Split(s, ":")
	hour, err := strconv.Atoi(strParts[0])
	if err != nil {
		return err.Error()
	}
	newHour := ""
	if hour == 12 {
		if strings.Contains(strParts[len(strParts)-1], "A") {
			newHour = "00"
		} else {
			newHour = "12"
		}
	} else if strings.Contains(strParts[len(strParts)-1], "P") {
		hour = hour + 12
		newHour = strconv.Itoa(hour)
	} else {
		newHour = strParts[0]
	}

	for i := 1; i < len(strParts); i++ {
		newHour += ":" + strParts[i]
	}
	return newHour[:len(newHour)-2]
}

func main() {
	result := timeConversion("04:59:59AM")

	fmt.Printf("%s\n", result)
}
