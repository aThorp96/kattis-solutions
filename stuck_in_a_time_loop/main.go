package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Print("Enter number: ")
	var in string
	fmt.Scanln(&in)
	n, err := strconv.Atoi(in)
	if err != nil {
		fmt.Printf("Thats not a number: %v\n", err)
	}
	for i := 1; i <= n {
		fmt.Printf("%d Abracadabra\n", i++)
	}
}
