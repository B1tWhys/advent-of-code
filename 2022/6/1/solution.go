package main

import (
	"fmt"
	"os"
)

func main() {
	dat, err := os.ReadFile("./input.txt")
	if err != nil {
		panic(err)
	}
	for i := 0; i < len(dat); i++ {
		seen := make(map[byte]bool)
		for j := i; j < i+4; j++ {
			if _, s := seen[dat[j]]; s {
				break
			} else {
				seen[dat[j]] = true
			}
		}
		if len(seen) == 4 {
			fmt.Printf("Found start of packet at: %v", i+4)
			return
		}
	}
	fmt.Println("Never found start of packet!")
}
