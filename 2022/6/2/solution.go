package main

import (
	"fmt"
	"os"
	"time"
)

func main() {
	start := time.Now()
	defer func() {
		end := time.Now()
		elapsed := end.Sub(start)
		fmt.Printf("Completed in: %v ns\n", elapsed.Nanoseconds())
	}()
	dat, err := os.ReadFile("./input.txt")
	if err != nil {
		panic(err)
	}
	for i := 0; i < len(dat); i++ {
		seen := make(map[byte]bool)
		for j := i; j < i+14; j++ {
			if _, s := seen[dat[j]]; s {
				break
			} else {
				seen[dat[j]] = true
			}
		}
		if len(seen) == 14 {
			fmt.Printf("Found start of message at: %v\n", i+14)
			return
		}
	}
	fmt.Println("Never found start of message!")
}
