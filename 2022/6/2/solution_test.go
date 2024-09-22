package main

import (
	"testing"
)

func test(t *testing.T, sut func([]byte) int) {
	actual := sut(loadInput())
	expected := 3037
	if actual != expected {
		t.Errorf("sut(byte) = %v; want %v", actual, expected)
	}
}

func benchmark(b *testing.B, sut func([]byte) int) int {
	dat := loadInput()
	result := 0
	b.ResetTimer()
	for range b.N {
		result += sut(dat)
	}
	return result
}

func TestNaive(t *testing.T) {
	test(t, naive)
}

func BenchmarkNaive(b *testing.B) {
	benchmark(b, naive)
}

func TestStopEarly(t *testing.T) {
	test(t, stopEarly)
}

func BenchmarkStopEarly(b *testing.B) {
	benchmark(b, stopEarly)
}

func TestSlidingWindowAarr(t *testing.T) {
	test(t, slidingWindowArr)
}

func BenchmarkSlidingWindowAarr(b *testing.B) {
	benchmark(b, slidingWindowArr)
}

func TestSlidingWindowBitmap(t *testing.T) {
	test(t, slidingWindowBitmap)
}

func BenchmarkSlidingWindowBitmap(b *testing.B) {
	benchmark(b, slidingWindowBitmap)
}

func TestSlidingWindowBitmapFancyMask(t *testing.T) {
	test(t, slidingWindowBitmapFancyMask)
}

func BenchmarkSlidingWindowBitmapFancyMask(b *testing.B) {
	benchmark(b, slidingWindowBitmapFancyMask)
}

func TestBenny(t *testing.T) {
	test(t, benny)
}

func BenchmarkBenny(b *testing.B) {
	benchmark(b, benny)
}
