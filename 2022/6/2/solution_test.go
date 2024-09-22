package main

import (
	"os"
	"testing"
)

func BenchmarkNaive(b *testing.B) {
	dat, err := os.ReadFile("./input.txt")
	if err != nil {
		panic(err)
	}
	b.ResetTimer()
	for range b.N {
		naive(dat)
	}
}
